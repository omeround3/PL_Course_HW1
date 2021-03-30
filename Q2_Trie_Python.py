""" 
Trie data structure imcurrentNodelementation on the English language alcurrentNodehabet.

@authors
Sam Medina
Omer Lev-Ron

"""
import Q2_TrieNode_Python as TrieNode

class Trie:
    # Trie initialization
    def __init__(self):
        self.root = self.get_node()
    
    # Node initialization (size of node is N=26; defined as list)
    def get_node(self):
        return TrieNode.TrieNode()
        
    def char_to_index(self,char):
        return ord(char)-ord('a')
    
    def is_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('A word should be a not-Null string')

    # This function insert a word to the Trie
    def insert_to_trie(self, word):
        if self.is_word(word)is False:
            return False
        
        currentNode = self.root

        for char in range(len(word)):
            char_index = self.char_to_index(word[char])
            # print(f"char: {char} | Char Index - {char_index}")
            if not currentNode.children[char_index]: 
                # If the character doesn't exist in the Trie; create it
                currentNode.children[char_index] = self.get_node()
                currentNode.children[char_index].ch = word[char]
                currentNode.children[char_index].word = currentNode.word + word[char]
                currentNode.children[char_index].parent = currentNode

            currentNode = currentNode.children[char_index] 
  
        currentNode.isLeaf = True # current node is the last character

    # This function searches for a specific word in the Trie
    def search(self, word):
        if self.is_word(word)is False:
            return False
        
        currentNode = self.root

        for char in range(len(word)):
            char_index = self.char_to_index(word[char])
            if not currentNode.children[char_index]:
                # If the character doesn't exist in the Trie; the word doesn't exist also
                return False
            currentNode = currentNode.children[char_index]

        return currentNode is not None and currentNode.isLeaf

    # THIS FUNCTION DOESN"T REALLY DELETES
    def deleteString(self, word):
        currentNode = self.root
        if self.search(word):
            for char in range(len(word)):
                char_index = self.char_to_index(word[char])
                currentNode = currentNode.children[char_index]

            currentNode.isLeaf = False

    # # This function deletes a word from the 
    def delete_from_trie(self, word):
        if self.is_word(word)is False:
            return False
        self.deleteRecursive(self.root, word)
    
    def deleteRecursive(self, currentNode, word, i = 0):
        # empty trie
        if not currentNode: 
            return None
        # If the character is terminating the word
        if i == len(word):
            # The node is no longer a leaf
            if currentNode.isLeaf:
                currentNode.isLeaf = False
            # The current node is not a prefix of other words
            if self.isEmptyNode(currentNode):
                del(currentNode)
                currentNode = None
            return currentNode
        # Recursive call for child
        else:
            char_index = self.char_to_index(word[i])
            currentNode.children[char_index] = self.deleteRecursive(currentNode.children[char_index], word, i + 1)

            # If current node doesn't have children, and it's not a leaf
            if self.isEmptyNode(currentNode) and not currentNode.isLeaf:
                del(currentNode)
                currentNode = None
            return currentNode

    # Returns true if the current node has no children; else it returns false
    def isEmptyNode(self, currentNode):
        for i in range(TrieNode.N):
            if currentNode.children[i]:
                return False
        return True

    # def __str__(self):
    #     s = ''
    #     currentNode = self.root
    #     if currentNode.children == []: return ' | '
    #     for i in currentNode.children:
    #         s = s +  ' | ' + ' '.join(currentNode.children)
    #     return s 


# driver function
def main():
  
    # Strings incurrentNodeut
    words = ["sam","and","omer","are","very", "good","students", "and", "software", "engineers"]
    result = ["The word is NOT in the trie", "The word is IN the trie"]
  
    t = Trie()
    for word in words:
        t.insert_to_trie(word)
    

    # Search for different words
    print(f"sam - {result[t.search('sam')]}")
    print(f"omer - {result[t.search('omer')]}")
    print(f"students - {result[t.search('students')]}")
    print(f"engineers - {result[t.search('engineers')]}\n")

    # currentNoderint trie
    # currentNoderint(t)

    # Remove a word
    t.delete_from_trie("sam")
    print(f"sam - {result[t.search('sam')]}")
    print(f"students - {result[t.search('students')]}")

if __name__ == '__main__':
    main()
  