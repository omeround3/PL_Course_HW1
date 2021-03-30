
N = 26 # Size of the alphabet

class Trie:

    def __init__(self):
        self.root = self.getNode()
  
    def get_node(self):
        return TrieNode()
  
    def insert_to_trie(self,word):
        p = self.root
        word_length = len(word)
        for level in range(word_length):
            id = self.char_to_index(word[level])
  
            if not p.children[id]:
                p.children[id] = self.get_node()
            p = p.children[id]
  
        p.end = True
        
    def char_to_index(self,char):
        return ord(char)-ord('a')
  
    def search(self, word):
        p = self.root
        word_length = len(word)
        for level in range(word_length):
            id = self.char_to_index(word[level])
            if not p.children[id]:
                return False
            p = p.children[id]
  
        return p is not None and p.end
  
# The class implements a Trie node
class TrieNode:
    def __init__(self):
        self.children = []*N
        self.end = False
  

# driver function
def main():
  
    # Input words (use only 'a' through 'z' and lower case)
    words = ["the","a","there","anaswe","any",
            "by","their"]
    output = ["Not present in trie",
              "Present in trie"]
  
    # Trie object
    t = Trie()
  
    # Construct trie
    for word in words:
        t.insert_to_trie(word)
  
    # Search for different words
    print("{} ---- {}".format("the",output[t.search("the")]))
    print("{} ---- {}".format("these",output[t.search("these")]))
    print("{} ---- {}".format("their",output[t.search("their")]))
    print("{} ---- {}".format("thaw",output[t.search("thaw")]))
  
if __name__ == '__main__':
    main()
  