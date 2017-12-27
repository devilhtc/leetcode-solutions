class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int prev = image[sr][sc];
        fill(image, sr, sc, prev, newColor);
        return image;
    }
    
    private void fill(int[][] image, int i, int j, int prev, int next) {
        if (i<0 || j<0 || i>=image.length || j>=image[0].length) return;
        if (image[i][j] != prev) return;
        if (image[i][j] == next) return;
        image[i][j] = next;
        fill(image, i-1, j, prev, next);
        fill(image, i+1, j, prev, next);
        fill(image, i, j-1, prev, next);
        fill(image, i, j+1, prev, next);
    }
}