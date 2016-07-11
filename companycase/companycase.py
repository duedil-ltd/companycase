# coding=utf-8
import codecs
import os
from collections import Counter

class CompanyCase:

    def __init__(self, language='en', ngram_length=2):
        self.ngram_length = ngram_length
        self.transitions = self.fetch_all_transitions(language, ngram_length)
        self.norm_transitions = self.normalize_transitions(self.transitions)

        # While most sensible parameters will capitalize the acronyms, forcing them here
        # to make sure they don't get title cased for whatever set of parameters.
        self.force_case = ['of', 'and', 'IT', 'PLC', 'LLC', 'LTD']

    def find_ngrams(self, input_list, n):
        """ Returns a list of n-grams """
        return map(lambda x: ''.join(x), zip(*[input_list[i:] for i in range(n)]))

    def fetch_all_transitions(self, language, ngram_length):
        """ Generate a dict of counts for transitions for all n-grams in the language word list """
        wordlist = os.path.join(os.path.dirname(__file__), "wordlists/{0}.txt".format(language))
        if not os.path.exists(wordlist):
            raise SystemError("Language '{0}' does not exist".format(language))

        all_grams = []
        with codecs.open(wordlist, 'r', encoding='utf-8') as f:
            for line in f:
                words = line.strip('\n').lower().split()
                ngrams = reduce(lambda x, y: x + y, map(lambda word: self.find_ngrams(word, ngram_length), words))
                all_grams += ngrams
        return dict(Counter(all_grams))

    def normalize_transitions(self, t):
        total = float(reduce(lambda x, y: x + y, t.values()))
        return dict([(x, y/total) for x, y in t.iteritems()])

    def force_case_for_words(self, l):
        """
         Add additional words to force case for
        :param l: a list of words to force the case for
        :return: None
        """
        self.force_case += l

    def score_word(self, word):
        """ Returns the mean transition likelihood score for the word """
        ngrams = self.find_ngrams(word.lower(), self.ngram_length)
        if len(ngrams) < 1:
            return 0.0
        return sum(map(lambda x: self.norm_transitions.get(x, 0), ngrams)) / len(ngrams)

    def apply(self, company_name, threshold=0.001):
        """
        Applies the case transformation on the given string
        :param company_name: string representing company name
        :param threshold: the transition score threshold to identify abbreviations
        :return: a string containing words with fixed case
        """

        if type(company_name) == unicode:
            company_name = company_name.encode('utf-8')

        fixed_name = []
        for word in company_name.split():
            fixed_word = None

            # Check if the word is to be force cased
            for x in self.force_case:
                if x.lower() == word.lower():
                    fixed_word = x
                    break

            if not fixed_word:
                # Title case if dictionary word-like
                # else, Upper case
                score = self.score_word(word)
                if score < threshold:
                    fixed_word = word.decode('utf-8').upper()
                else:
                    fixed_word = word.decode('utf-8').title()

                # Clean up any trailing 'S
                if fixed_word.endswith("'S"):
                    fixed_word = fixed_word[:-1]+'s'

            fixed_name.append(fixed_word)
        return ' '.join(fixed_name)
