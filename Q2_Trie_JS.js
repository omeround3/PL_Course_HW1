/* 
Implemntation of the Trie data structure and
driver class to test the code 

@authors
Sam Medina
Omer Lev-Ron

*/

// The class implements a Trie node 
class TrieNode {
  
    constructor() {
        this.parent = null;
        this.children = Array(26).fill(null);
        this.ch = ' ';
        this.word = "";
        this.isLeaf = false;
   }
 }

 // The class implements the Trie data structure 
 class Trie{
    //Trie initialization
    
   constructor(){
        this.root = this.get_node();
   }
    
    // Trie Node initialization (size of node is ALPHABET_SIZE=26; defined as list)
    get_node(){
        return new TrieNode()
    }

    ord(index){
      return ascii_table[index];
    }
    
    char_to_index(char) {
        return(ord(char)-ord('a') )* -1;
    }
    
    is_word(word) {
        if (word == ''){
            return false
        }
        if (word == null){
            throw Error('A word should be a not-Null string')
        }
    }
    // This function inserts a word to the Trie
    insert_to_trie(word){
        if (this.is_word(word) == false) {
            return false;
        }
        let currentNode = this.root;

        for (let char=0; char < word.length; char++){
            let char_index = this.char_to_index(word[char]);
            // print(f"char: {char} | Char Index - {char_index}")
            if (!currentNode.children[char_index]){ 
                // If the character doesn't exist in the Trie; create it
                currentNode.children[char_index] = this.get_node();
                currentNode.children[char_index].ch = word[char];
                currentNode.children[char_index].word = currentNode.word + word[char];
                currentNode.children[char_index].parent = currentNode;
            }      
            currentNode = currentNode.children[char_index] ;
        }
  
        currentNode.isLeaf = true; // current node is the last character
    }
    // This function searches for a specific word in the Trie
    search(word){
        if (this.is_word(word) === false) {
            return false
        }
        
        let currentNode = this.root;

        for (let char=0; char < word.length; char++){
            let char_index = this.char_to_index(word[char])
            if (!currentNode.children[char_index]){
                // If the character doesn't exist in the Trie; the word doesn't exist also
                return false
            }
            currentNode = currentNode.children[char_index];
        }
     
        return (currentNode !== null && currentNode.isLeaf)
    }
    // Returns true if the current node has no children; else it returns false
    isEmptyNode(currentNode){
        for (let i =0; i< 26; i++){
            if (currentNode.children[i]){
                return false
            }
        }
        return true
    }

    //These 2 functions below deletes a word from the Trie
    delete_from_trie(word){
        if (this.is_word(word) === false) {
            return false 
         }
        this.deleteRecursive(this.root, word);
    }
    // Recursive deletion of a word
    deleteRecursive( currentNode, word, i = 0) {
      debugger
        // empty trie check
        if (currentNode === false)
            return null;
        // If the character is terminating the word
        if (i === word.length){
           //The node is no longer a leaf
            if (currentNode.isLeaf)
                currentNode.isLeaf = false;
            //The current node is not a prefix of other words
            if (this.isEmptyNode(currentNode)){
                currentNode = null;
            }
            
            return currentNode;
        }
        //Recursive call for children
        else {
            
            let char_index = this.char_to_index(word[i])
            currentNode.children[char_index] = this.deleteRecursive(currentNode.children[char_index], word, i + 1)

            //If current node doesn't have children, and it's not a leaf
            if (this.isEmptyNode(currentNode) && currentNode.isLeaf === false && currentNode.word.length > 1){
                currentNode = null;
            }
            return currentNode;
        }
    }
    }

 
function ord (string) {
  const str = string + ''
  const code = str.charCodeAt(0)
  if (code >= 0xD800 && code <= 0xDBFF) {
    const hi = code
    if (str.length === 1) {
      return code
    }
    const low = str.charCodeAt(1)
    return ((hi - 0xD800) * 0x400) + (low - 0xDC00) + 0x10000;
  }
  if (code >= 0xDC00 && code <= 0xDFFF) {
    return code
  }
  return code
}

function main() {
  
    //Strings input and results
    const words = ["sam","and","omer","are","very", "good","students", "and", "software", "engineers"]
    const result = ["The word is NOT in the trie", "The word is IN the trie"]

    //Trie construction
    const t = new Trie();
    for (let word of words){
        t.insert_to_trie(word);
    }

    //Search for different words
    console.log(`sam - ${t.search('sam') ? result[1] : result[0]}`);
    console.log(`omer - ${t.search('omer') ? result[1] : result[0]}`);
    console.log(`students - ${t.search('students') ? result[1] : result[0]}`);
    console.log(`engineers - ${t.search('engineers') ? result[1] : result[0]}`);
 
    // Remove a word
    t.delete_from_trie("sam");
    console.log(`sam - ${t.search('sam') ? result[1] : result[0]}`);
    console.log(`students - ${t.search('students') ? result[1] : result[0]}`);
}
