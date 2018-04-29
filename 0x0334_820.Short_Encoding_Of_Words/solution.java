class Solution {
    class TrieNode {
        public char c;
        public int count;
        public int wordlen;
        public TrieNode[] children;
        
        public TrieNode(char cur) {
            c = cur;
            wordlen = 0;
            children = new TrieNode[26];
            count = 0;
        }
    }
    
    private void addWord2Trie(TrieNode node, String s, int i) {
        char cur = s.charAt(i);
        int index = (int)(cur - 'a');
        
        if (node.children[index] == null) {
            node.children[index] = new TrieNode(cur);
        }
        
        node = node.children[index];
        node.count = node.count + 1;
        
        if (i == 0) {
            node.wordlen = s.length();
        } else {
            addWord2Trie(node, s, i-1);
        }
    }
    
    private int countEnds(TrieNode node) {
        if (node.wordlen > 0 && node.count == 1) return 1 + node.wordlen;
        int count = 0;
        for (TrieNode child : node.children) {
            if (child != null) count += countEnds(child);
        }
        return count;
    }
    
    public int minimumLengthEncoding(String[] words) {
        TrieNode root = new TrieNode(' ');
        Set<String> s = new HashSet<String>();
        for (String w : words) {
            if (!s.contains(w)) {
                s.add(w);
                addWord2Trie(root, w, w.length() - 1);
            }
        }
        return countEnds(root);
    }
}