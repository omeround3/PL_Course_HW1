public class Trie {
    
    // Define Variables
    static TrieNode root;
    static String exceptionWord = "A word should be a not-Null string";

    // Trie Node initialization (size of node is N=26; defined as list)
    Trie() {
        root = get_node();
    }

    TrieNode get_node() { return new TrieNode(); }


    static boolean is_word(String word) {
        if (word.isBlank())
            return false;
        return true;
    }

    // This function inserts a word to the Trie
    static void insert_to_trie(String word) throws Exception {
        // Check that the word is not empty
        if (!is_word(word))
            throw new Exception(exceptionWord);

        TrieNode currentNode = root;
        for (int i = 0; i < word.length(); i++) {
            int char_index = word.charAt(i) - 'a';
            if (currentNode.children[char_index] == null) {
                currentNode.children[char_index] = new TrieNode();
                currentNode.children[char_index].setCh(word.charAt(i));
                currentNode.children[char_index].setWord(currentNode.getWord() 
                    + word.charAt(i));
                currentNode.children[char_index].setParent(currentNode);
            }
            currentNode = currentNode.children[char_index];
        }
        currentNode.isLeaf = true; // current node is the last character
    }
    
    // This function searches for a specific word in the Trie
    static boolean search(String word) throws Exception {
        // Check that the word is not empty
        if (!is_word(word))
            throw new Exception(exceptionWord);

        TrieNode currentNode = root;
        for (int i = 0; i < word.length(); i++) {
            int char_index = word.charAt(i) - 'a';
            if (currentNode.children[char_index] == null)
                return false;
            currentNode = currentNode.children[char_index];
        }
        return (currentNode != null && currentNode.isLeaf);
    }

    // Returns true if the current node has no children; else it returns false
    static boolean isEmpty(TrieNode currentNode) {
        for (int i = 0; i < TrieNode.ALPHABET_SIZE; i++) {
            if (currentNode.children[i] != null)
                return false;
        }
        return true;
    }

    // These 2 functions below deletes a word from the Trie
    static void delete_from_trie(String word) throws Exception {
        // Check that the word is not empty
        if (!is_word(word))
            throw new Exception(exceptionWord);
        deleteRecursive(root, word, 0);
    }
    // Recursive deletion of a word
    static TrieNode deleteRecursive(TrieNode currentNode, String word, int i) {
        // empty trie check
        if (currentNode == null)
            return null;
        // If the character is terminating the word
        if (i == word.length()) {
            // The node is no longer a leaf
            if (currentNode.isLeaf)
                currentNode.isLeaf = false;
            // The current node is not a prefix of other words
            if (isEmpty(currentNode)) 
                currentNode = null;
            return currentNode;
        }
        // Recursive call for children
        else {
            int char_index = word.charAt(i) - 'a';
            currentNode.children[char_index] = deleteRecursive(currentNode.children[char_index], word, i + 1);
        
            // If current node doesn't have children, and it's not a leaf
            if (isEmpty(currentNode) && !currentNode.isLeaf)
                currentNode = null;
            return currentNode;
        }
    }

}
