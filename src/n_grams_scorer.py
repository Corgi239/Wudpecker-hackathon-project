import numpy as np
import nltk
from nltk.util import ngrams
from nltk.lm.counter import NgramCounter

class NGramsScorer:
    def __init__(self):
        self.n_grams = None
        self.__grams = []
    

    def fit(self, corpus):
        for text in corpus:
            text_ngrams = self.__extract_ngrams(text, 2)
            self.__grams.append(text_ngrams)
        self.n_grams = NgramCounter(self.__grams)
    

    def score(self, test_text):
        tokens = nltk.word_tokenize(test_text)
        tokens = [token.lower() for token in tokens]
        l = len(tokens)
        probs = np.empty(l - 1)
        for i in range(l - 1):
            first = tokens[i]
            second = tokens[i+1]
            fdict = self.n_grams[[first]]
            if (fdict.N() == 0):
                probs[i]=0
            else:
                probs[i] = fdict[second] / fdict.N()
        return probs.mean()


    def __extract_ngrams(self, text: str, n: int = 2):
        tokens = nltk.word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        grams = ngrams(tokens,n)
        return grams
