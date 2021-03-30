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
    }
}
