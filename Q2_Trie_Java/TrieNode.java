/* 
The class implements a Trie node 

@authors
Sam Medina
Omer Lev-Ron

*/


public class TrieNode {

    static final int ALPHABET_SIZE = 26; // Size of the alphabet
    // Declare variables
    private TrieNode parent = null;
    private char ch;
    private String word = "";

    TrieNode[] children = new TrieNode[ALPHABET_SIZE];
    boolean isLeaf;

    TrieNode() {
        for (int i = 0; i < children.length; i++) 
            children[i] = null;
        isLeaf = false;
    }

    public TrieNode getParent() {
        return this.parent;
    }

    public void setParent(TrieNode parent) {
        this.parent = parent;
    }

    public char getCh() {
        return this.ch;
    }

    public void setCh(char ch) {
        this.ch = ch;
    }

    public String getWord() {
        return this.word;
    }

    public void setWord(String word) {
        this.word = word;
    }
}
