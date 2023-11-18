import numpy as np
import nltk
from nltk.util import ngrams
from nltk.lm.counter import NgramCounter

class NGramsScorer:
    """
    A class for scoring textual transcripts. 

    Methods
    ---
    fit(corpus): 
        Fits the scorer to a given corpus of text.

    score(test_text):
        Returns the score of the provided text.
    """
    def __init__(self):
        self.n_grams = None
        self.__grams = []
    

    def fit(self, corpus):
        '''
        Fits the scorer to a given corpus of text.

        The method evaluates the counts of all bigrams present in the training corpus and stores the resulting bigram counts.

            Parameters:
                corpus (List[str]): List of training text strings
        '''
        for text in corpus:
            text_ngrams = self.__extract_ngrams(text, 2)
            self.__grams.append(text_ngrams)
        self.n_grams = NgramCounter(self.__grams)
    

    def score(self, test_text):
        '''
        Calculates the cohesion score of the provided text.

        The score is based on how well represented the bigrams from the text are among in the training corpus.

            Parameters:
                test_text (str): the text to be scored

            Returns:
                final_score (float): a score value between 0 and 1
        '''
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
        final_score = probs.mean()
        return final_score


    def __extract_ngrams(self, text: str, n: int = 2):
        tokens = nltk.word_tokenize(text)
        tokens = [token.lower() for token in tokens]
        grams = ngrams(tokens,n)
        return grams
