import nltk, string
from sklearn.feature_extraction.text import TfidfVectorizer

#nltk.download('wordnet') # first-time use only

def LemTokens(tokens):
    lemmer = nltk.stem.WordNetLemmatizer()
    return [lemmer.lemmatize(token) for token in tokens]

def LemNormalize(text):
    remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def cosineSimilarity(textlist):
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english', analyzer='word')
    tfidf = TfidfVec.fit_transform(textlist)
    return (tfidf * tfidf.T).toarray()
