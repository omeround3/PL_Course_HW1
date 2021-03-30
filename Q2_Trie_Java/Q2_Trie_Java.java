/* 
Driver class to test the Trie data structure 

@authors
Sam Medina
Omer Lev-Ron

*/


public class Q2_Trie_Java {

    public static void main(String[] args) throws Exception {
        // Strings input and results
        String words[] = {"sam","and","omer","are","very", "good","students", "and", "software", "engineers"};
        String result[] = {"The word is NOT in the trie", "The word is IN the trie"};

        Trie t = new Trie();

        // Trie construction
        for (int i = 0; i < words.length; i++){
            try {
                t.insert_to_trie(words[i]);
            } catch (Exception e) {
                System.out.println("[ERROR] insert failed");
                e.printStackTrace();
            }
        }
            
        // Search for different words
        if (t.search("sam"))
            System.out.println("sam - " + result[1]);
        else
            System.out.println("sam - " + result[0]);
        if (t.search("omer"))
            System.out.println("omer - " + result[1]);
        else
            System.out.println("omer - " + result[0]);
        if (t.search("students"))
            System.out.println("students - " + result[1]);
        else
            System.out.println("students - " + result[0]);
        if (t.search("sam"))
            System.out.println("engineers - " + result[1]);
        else
            System.out.println("engineers - " + result[0]);
        
        // Remove a word
        t.delete_from_trie("sam");
        System.out.println("");
        if (t.search("sam"))
            System.out.println("sam - " + result[1]);
        else
            System.out.println("sam - " + result[0]);
        if (t.search("students"))
            System.out.println("students - " + result[1]);
        else
            System.out.println("students - " + result[0]);
        
    }
}
