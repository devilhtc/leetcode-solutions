class WordFilter {
    Trie forward;
    Trie backward;
    
    public WordFilter(String[] words) {
        forward = new Trie();
        backward = new Trie();
        for (int w = words.length-1; w >= 0 ; w--) {
            forward.addWord(words[w], w);
            backward.addWord(reverseString(words[w]), w);
        }
    }
    
    public int f(String prefix, String suffix) {
        List<Integer> l1 = forward.query(prefix);
        List<Integer> l2 = backward.query(reverseString(suffix));
        return findCommon(l1, l2);
    }

    private void printList(List<Integer> l) {
        for (int i =0 ;i<l.size();i++) {
            System.out.print(l.get(i));
            System.out.print(" ");
        }
        System.out.println();
    }
    
    private int findCommon(List<Integer> l1, List<Integer> l2) {
        if (l1.size() == 0 || l2.size() == 0) {
            return -1;
        }
        int i = 0, j = 0;
        while (i < l1.size() && j < l2.size()) {
            if ( ((int)l1.get(i)) ==  ((int)l2.get(j))  ) return l1.get(i);
            if (  ((int)l1.get(i)) < ((int)l2.get(j))  ) j+=1;
            else i+=1;
        }
        return -1;
    }
    
    private String reverseString(String word) {
        char[] wc = word.toCharArray();
        int i = 0, j = wc.length - 1;
        while (j > i) {
            char temp = wc[i];
            wc[i] = wc[j];
            wc[j] = temp;
            i++;
            j--;
        }
        return new String(wc);
    }
}

class Trie {
    TrieNode root;
    public Trie() {
        root = new TrieNode('.');
    }
    
    public void addWord(String word, int w) {
        TrieNode cur = root;
        cur.addWeight(w);
        for (int i = 0; i<word.length(); i++) {
            int index = (int)(word.charAt(i) - 'a');
            TrieNode[] curChildren = cur.children;
            if (curChildren[index] == null) {
                curChildren[index] = new TrieNode(word.charAt(i));
            }
            TrieNode node = curChildren[index];
            node.addWeight(w);
            cur = node;
        }
    }
    
    public List<Integer> query(String prefix) {
        List<Integer> empty = new ArrayList();
        TrieNode cur = root;
        for (int i = 0; i<prefix.length(); i++) {
            int index = (int)(prefix.charAt(i) - 'a');
            TrieNode[] curChildren = cur.children;
            if (curChildren[index] == null) {
               return empty;
            }
            TrieNode node = curChildren[index];
            cur = node;
        }
        return cur.getWeights();
    }
}

class TrieNode {
    char c;
    List<Integer> weights;
    public TrieNode[] children;
    
    public TrieNode(char ch) {
        c = ch;
        weights = new ArrayList();
        children = new TrieNode[26];
    }
    
    public void addWeight(int w) {
        weights.add(w);
    }
    
    public List<Integer> getWeights() {
        return weights;
    } 
}


/**
 * Your WordFilter object will be instantiated and called as such:
 * WordFilter obj = new WordFilter(words);
 * int param_1 = obj.f(prefix,suffix);
 */