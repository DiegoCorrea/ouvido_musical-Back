# -*- coding: utf-8 -*-
import logging
import string
from multiprocessing.dummy import Pool as ThreadPool

import nltk
import numpy as np
import pandas as pd
from django.utils import timezone
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer, TfidfTransformer

from apps.kemures.kernel.config.global_var import MAX_THREAD
from apps.kemures.similarities.Cosine.runtime.models import CosineSimilarityRunTime


class CosineController:
    def __init__(self, song_set_df, round_instance):
        """
            Construtor da classe CosineController, onde o valor é calculado a partir dos dados no argumento song_set_df
            Args:
                song_set_df (DataFrame): Um DataFrame com as informações das músicas.
        """
        self.__logger = logging.getLogger(__name__)
        self.__round_instance = round_instance
        self.__song_set_df = song_set_df
        self.__song_similarity_df = pd.DataFrame()

    def get_song_similarity_df(self):
        return self.__song_similarity_df

    def run_similarity(self):
        self.__logger.info("[Start Run Cosine Similarity]")
        __started_at = timezone.now()
        self.__song_similarity_df = self.__start_cosine()
        __finished_at = timezone.now()
        self.__logger.info(
            "Cosine Run Time: Start at - "
            + str(__started_at)
            + " || Finished at - "
            + str(__finished_at)
        )
        CosineSimilarityRunTime.objects.create(
            round=self.__round_instance,
            started_at=__started_at,
            finished_at=__finished_at
        )
        self.__logger.info("[Finish Run Cosine Similarity]")

    def __start_cosine(self):
        matrix_data = [self.__song_set_df[column].tolist() for column in self.__song_set_df.columns if column != 'id']
        pool = ThreadPool(MAX_THREAD)
        feature_matrix_similarity = pool.map(CosineController.find_similarity, matrix_data)
        pool.close()
        pool.join()
        similarity_matrix = np.zeros(self.__song_set_df['id'].count())
        for matrix in feature_matrix_similarity:
            similarity_matrix = np.add(similarity_matrix, matrix)
        similarity_matrix = similarity_matrix / len(feature_matrix_similarity)
        return pd.DataFrame(data=similarity_matrix, index=self.__song_set_df['id'].tolist(),
                            columns=self.__song_set_df['id'].tolist())

    @classmethod
    def __lem_tokens(cls, tokens):
        lemmer = nltk.stem.WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    @classmethod
    def __lem_normalize(cls, text):
        remove_punct_dict = dict(
            (ord(punct), None)
            for punct in string.punctuation
        )
        return cls.__lem_tokens(
            nltk.word_tokenize(
                text.lower().translate(remove_punct_dict)
            )
        )

    @classmethod
    def find_similarity(cls, text_list):
        tfidf_vec = TfidfVectorizer(
            tokenizer=cls.__lem_normalize,
            stop_words='english',
            analyzer='word'
        )
        tfidf = tfidf_vec.fit_transform([str(txt) for txt in text_list])
        return (tfidf * tfidf.T).toarray()

    @classmethod
    def test_similarity(cls, text_list):
        LemVectorizer = CountVectorizer(tokenizer=cls.__lem_normalize, stop_words='english')
        LemVectorizer.fit_transform(text_list)
        print(LemVectorizer.vocabulary_)
        tf_matrix = LemVectorizer.transform(text_list).toarray()
        print(tf_matrix)
        tfidfTran = TfidfTransformer(norm="l2")
        tfidfTran.fit(tf_matrix)
        print(tfidfTran.idf_)
        tfidf_matrix = tfidfTran.transform(tf_matrix)
        for t in tfidf_matrix.toarray():
            print(t)
        print("")
        print("*")
        print("")
        cos_similarity_matrix = (tfidf_matrix * tfidf_matrix.T).toarray()
        for c in cos_similarity_matrix:
            print(c)
