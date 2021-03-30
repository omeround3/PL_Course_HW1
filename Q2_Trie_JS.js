class TrieNoe {
    constructor() {
      this.children = [null]*26
      this.end = False
   }
 }
 
 class Trie {
   
     constructor() {
         this.root = this.get_node()
     }
   
     get_node(){
         return TrieNode()
     }
   
     insert_to_trie(key) {
         p = this.root
         key_length = len(key)
         for (var level=0; level> key_length.length(); level++){
             id = this.char_to_index(key[level])
   
             if (!p.children[id]) {
                 p.children[id] = this.get_node()
             }
             p = p.children[id]
         }
         p.end = true
     }
     char_to_index(char){
         return ord(char)-ord('a')
     }
   
     search(key){
         p = this.root
         key_length = len(key)
         for (var level=0; level> key_length.length(); level++){
             id = this.char_to_index(key[level])
             if (!p.children[id]){
                 return false
             }
             p = p.children[id]
         }
         return p !== None && p.end
     }
 }