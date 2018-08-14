# -*- coding: utf-8 -*-
# Python and Pip Modules Calls
import nltk
import string
import logging
import numpy as np
import pandas as pd
from django.utils import timezone
from multiprocessing import Pool as ThreadPool
from sklearn.feature_extraction.text import TfidfVectorizer
# Application Calls
from apps.kemures.similarities.Cosine.runtime.models import CosineSimilarityRunTime
from apps.kemures.kernel_var import MAX_THREAD


class CosineController:
    def __init__(self, song_set_df):
        self.__logger = logging.getLogger(__name__)
        self.__song_model_size = song_set_df.count()
        self.__song_set_df = song_set_df
        self.__song_similarity_df = pd.DataFrame()

    def get_song_similarity_df(self):
        return self.__song_similarity_df

    def run_similarity(self):
        self.__logger.info("[Start Run Cosine Metadata]")
        started_at = timezone.now()
        self.__song_similarity_df = self.__start_cosine()
        finished_at = timezone.now()
        CosineSimilarityRunTime.objects.create(
            song_model_size=self.__song_model_size,
            started_at=started_at,
            finished_at=finished_at
        )
        self.__logger.info(
            "Cosine Run Time: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        self.__logger.info("[Finish Run Cosine Metadata]")

    def __lem_tokens(self, tokens):
        lemmer = nltk.stem.WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    def __lem_normalize(self, text):
        remove_punct_dict = dict(
            (ord(punct), None)
            for punct in string.punctuation
        )
        return self.__lem_tokens(
            nltk.word_tokenize(
                text.lower().translate(remove_punct_dict)
            )
        )

    def find_similarity(self, metadata_list):
        self.__logger.info("[Start Cosine Similarity]")
        tfidf_vec = TfidfVectorizer(
            tokenizer=self.__lem_normalize,
            stop_words={'english'},
            analyzer='word'
        )
        tfidf = tfidf_vec.fit_transform([str(txt) for txt in metadata_list])
        self.__logger.info("[Finished Cosine Similarity]")
        return (tfidf * tfidf.T).toarray()

    def __start_cosine(self):
        matrix_metadata = [self.__song_set_df[column].tolist() for column in self.__song_set_df.columns if
                           column != 'id']
        pool = ThreadPool(MAX_THREAD)
        feature_matrix_similarity = pool.map(self.find_similarity, matrix_metadata)
        pool.close()
        pool.join()
        similarity_matrix = np.zeros(self.__song_set_df['id'].count())
        for matrix in feature_matrix_similarity:
            similarity_matrix = np.add(similarity_matrix, matrix)
        return pd.DataFrame(data=similarity_matrix, index=self.__song_set_df['id'].tolist(),
                            columns=self.__song_set_df['id'].tolist())
