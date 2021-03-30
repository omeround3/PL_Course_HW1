""" 
The class implements a Trie node

@authors
Sam Medina
Omer Lev-Ron

"""
ALPHABET_SIZE = 26 # Size of the alphabet

class TrieNode:
    def __init__(self):
        self.parent = None
        self.children = [None]*ALPHABET_SIZE
        self.ch = ' '
        self.word = ""
        self.isLeaf = False
        
