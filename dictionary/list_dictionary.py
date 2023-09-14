from dictionary.word_frequency import WordFrequency
from dictionary.base_dictionary import BaseDictionary


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. List-based dictionary implementation.
#
# __author__ = 'John'
# __copyright__ = 'Copyright 2022'
# ------------------------------------------------------------------------

class ListDictionary(BaseDictionary):
    dict=[]

    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word in words_frequencies:
            self.add_word_frequency(word)

    def search(self, word: str) -> int:
        for wordI in self.dict:
            if wordI.word == word:
                return wordI.frequency
        return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        if word_frequency not in self.dict:
            self.dict.append(word_frequency)
            return True
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        for wordI in self.dict:
            if wordI.word == word:
                self.dict.remove(wordI)
                return True
        return False

    def autocomplete(self, prefix_word: str) -> [str]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'prefix_word' as a prefix
        @param prefix_word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'prefix_word'
        """
        ac = []
        for wordI in self.dict:
            if prefix_word in wordI.word:
                ac.append(wordI)
        return ac
