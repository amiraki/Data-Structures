from dictionary.base_dictionary import BaseDictionary
from dictionary.word_frequency import WordFrequency
from dictionary.node import Node


# ------------------------------------------------------------------------
# This class is required to be implemented. Ternary Search Tree implementation.
#
# __author__ = 'John B'
# __copyright__ = 'Copyright 2022'
# ------------------------------------------------------------------------
class Node:

    data = '@'
    isEndOfString = 1
    left = None
    eq = None
    right = None

class TernarySearchTreeDictionary(BaseDictionary):

    root1 = None
    ternaryTree = {}

    def newNode(self, data):

        temp = Node()
        temp.data = data;
        temp.isEndOfString = 0;
        temp.left = temp.eq = temp.right = None;
        return temp;

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
            self.searchTST1(self.root1, word, 0)
            return self.ternaryTree[word]
        except Exception as e:
            return 0
       

    def searchTST1(self, root, word, ind):

        if root == None:
            return False;
        if word[ind] < root.data:
            return self.searchTST1(root.left, word[ind], ind)
     
        elif word[ind] > root.data:
            return self.searchTST1(root.right, word[ind], ind)
     
        else:


            if ind+1 == len(word):
                return True#root.isEndOfString
     
            return self.searchTST1(root.eq, word, ind+1)

   
    def add_word_frequency(self, word_frequency: WordFrequency) -> bool:
        """
        add a word and its frequency to the dictionary
        @param word_frequency: (word, frequency) to be added
        :return: True whether succeeded, False when word is already in the dictionary
        """
        if (self.root1 == None):
            self.root1 = self.newNode(word_frequency.word)
        self.root1 = self.insert1(self.root1, word_frequency.word, 0, len(word_frequency.word))
        try:
            self.ternaryTree[word]
        except Exception as e:
            self.ternaryTree[word_frequency.word] = word_frequency.frequency
            return True
        return False

    def insert1(self, root, word, ind, size):
        if root == None:
            return self.newNode(word[ind])
            root.data = word[ind]
        if word[ind] < root.data:
            root.left = self.insert1(root.left, word, ind, size)
        elif word[ind] > root.data:
            root.right = self.insert1(root.right, word, ind, size)
        else:
            if (ind+1) < len(word):
                root.eq = self.insert1(root.eq, word, ind+1, len(word));
            else:
                root.isEndOfString = 1;
        return root

    def delete_word(self, word: str) -> bool:
        """
        delete a word from the dictionary
        @param word: word to be deleted
        @return: whether succeeded, e.g. return False when point not found
        """
        try:
            self.ternaryTree.pop(word)
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
        for wordI in self.ternaryTree.keys():
            if word in wordI:
                w = WordFrequency(wordI, self.ternaryTree[wordI])
                ac.append(w)
        return ac
