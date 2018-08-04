import nltk
import string
from sklearn.feature_extraction.text import TfidfVectorizer
import logging
logger = logging.getLogger(__name__)
# nltk.download('wordnet') # first-time use only


def LemTokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens]


def LemNormalize(text):
    remove_punct_dict = dict(
        (ord(punct), None)
        for punct in string.punctuation
    )
    return LemTokens(
        nltk.word_tokenize(
            text.lower().translate(remove_punct_dict)
        )
    )


def CosineSimilarity(textlist):
    logger.info("[Start Cosine Similarity]")
    TfidfVec = TfidfVectorizer(
        tokenizer=LemNormalize,
        stop_words={'english'},
        analyzer='word'
    )
    tfidf = TfidfVec.fit_transform(textlist)
    logger.info("[Finished Cosine Similarity]")
    return (tfidf * tfidf.T).toarray()
