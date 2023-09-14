from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency


# ------------------------------------------------------------------------
# This class is required TO BE IMPLEMENTED. Hash-table-based dictionary.
#
# __author__ = 'John B'
# __copyright__ = 'Copyright 2022'
# ------------------------------------------------------------------------

class HashTableDictionary(BaseDictionary):

    dict_obj = {}
    def build_dictionary(self, words_frequencies: [WordFrequency]):
        """
        construct the data structure to store nodes
        @param words_frequencies: list of (word, frequency) to be stored
        """
        for word in words_frequencies:
            self.add_word_frequency(word)

    def search(self, word: str) -> int:
        """
        search for a word
        @param word: the word to be searched
        @return: frequency > 0 if found and 0 if NOT found
        """
        try:
            return self.dict_obj[word]
        except Exception as e:
            return 0

    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        try:
            self.dict_obj[word]
        except Exception as e:
            self.dict_obj[word_frequency.word] = word_frequency.frequency
            return True
        return False

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        
        
        try:
            self.dict_obj.pop(word)
            return True
        except Exception as e:
            return False
        

    def autocomplete(self, word: str) -> [str]:
        """
        return a list of 3 most-frequent words in the dictionary that have 'word' as a prefix
        @param word: word to be autocompleted
        @return: a list (could be empty) of (at most) 3 most-frequent words with prefix 'word'
        """
        ac = []
        for wordI in self.dict_obj.keys():
            if word in wordI:
                w = WordFrequency(wordI, self.dict_obj[wordI])
                ac.append(w)
        return ac
