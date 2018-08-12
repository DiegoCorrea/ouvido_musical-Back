# -*- coding: utf-8 -*-
# O.S. and Python/Django Calls
import string
import logging
from django.utils import timezone
from multiprocessing import Pool as ThreadPool
# Modules Calls
import nltk
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
# Application Calls
from apps.kemures.similarities.Cosine.runtime.models import CosineSimilarityRunTime
from apps.kemures.kernel_var import MAX_THREAD

logger = logging.getLogger(__name__)


class CosineController:
    def __init__(self, song_model_size, song_model_df):
        self.song_model_size = song_model_size
        self.metadata_df = song_model_df
        self.similarity_metadata_df = np.zeros(self.metadata_df['id'].count())

    def run_cosine_metadata(self):
        logger.info("[Start Run Cosine Metadata]")
        started_at = timezone.now()
        self.similarity_metadata_df = self.__start_cosine()
        finished_at = timezone.now()
        CosineSimilarityRunTime.objects.create(
            song_model_size=self.song_model_size,
            started_at=started_at,
            finished_at=finished_at
        )
        logger.info(
            "Benchmark: Start at - "
            + str(started_at)
            + " || Finished at -"
            + str(finished_at)
        )
        logger.info("[Finish Run Cosine Metadata]")

    def get_similarity_metadata_df(self):
        return self.similarity_metadata_df

    def get_metadata_df(self):
        return self.metadata_df

    def __LemTokens(self, tokens):
        lemmer = nltk.stem.WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    def __LemNormalize(self, text):
        remove_punct_dict = dict(
            (ord(punct), None)
            for punct in string.punctuation
        )
        return self.__LemTokens(
            nltk.word_tokenize(
                text.lower().translate(remove_punct_dict)
            )
        )

    def CosineSimilarity(self, metadata_list):
        logger.info("[Start Cosine Similarity]")
        TfidfVec = TfidfVectorizer(
            tokenizer=self.__LemNormalize,
            stop_words={'english'},
            analyzer='word'
        )
        tfidf = TfidfVec.fit_transform([str(txt) for txt in metadata_list])
        logger.info("[Finished Cosine Similarity]")
        return (tfidf * tfidf.T).toarray()

    def __start_cosine(self):
        matrix_metadata = [self.metadata_df[column].tolist() for column in self.metadata_df.columns if column != 'id']
        pool = ThreadPool(MAX_THREAD)
        feature_matrix_similarity = pool.map(self.CosineSimilarity, matrix_metadata)
        pool.close()
        pool.join()
        similarity_matrix = np.zeros(self.metadata_df['id'].count())
        for matrix in feature_matrix_similarity:
            similarity_matrix = np.add(similarity_matrix, matrix)
        return pd.DataFrame(data=similarity_matrix, index=self.metadata_df['id'].tolist(), columns=self.metadata_df['id'].tolist())

    def save_matrix_similarity_metadata(self):
        pass
