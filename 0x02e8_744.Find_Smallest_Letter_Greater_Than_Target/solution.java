class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        char smallestThanTarget = '.';
        char smallest = '.';
        for (char c : letters) {
            if (c > target) {
                if (smallestThanTarget == '.') {
                    smallestThanTarget = c;
                } else {
                    if (c < smallestThanTarget) {
                        smallestThanTarget = c;
                    }
                }
            } else {
                if (smallest == '.') {
                    smallest = c;
                } else {
                    if (c < smallest) {
                        smallest = c;
                    }
                }
            }
        }
        if (smallestThanTarget == '.') {
            return smallest;
        } else {
            return smallestThanTarget;
        }
    }
}