class Solution {
    public String shortestCompletingWord(String licensePlate, String[] words) {
        String lower = licensePlate.toLowerCase();
        int[] licenseCounts = word2counts(lower);
        int j = -1;
        for (int i = 0; i<words.length; i++) {
            if (covers(licenseCounts,word2counts(words[i]))) {
                if (j == -1) {
                    j = i;
                } else if (words[j].length() > words[i].length()) {
                    j = i;
                }
            }
        }
        return words[j];
    }
    
    private int[] word2counts(String word){
        int[] counts = new int[26];
        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            int index = (int) (c - 'a');
            if (index >= 0 && index < 26) {
                counts[index] ++;
            }
        }
        return counts;
    }
    
    private boolean covers(int[] licenseCounts, int[] wordCounts) {
        for (int i = 0; i<26; i++) {
            if (licenseCounts[i]>wordCounts[i]) return false;
        }
        return true;
    }
}