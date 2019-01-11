class Solution {
    class Keypoint {
        int h;
        int x;
        boolean s;
        
        public Keypoint(int h2, int x2, boolean s2) {
            h = h2;
            x = x2;
            s = s2;
        }
    }
    
    public List<int[]> getSkyline(int[][] buildings) {
        PriorityQueue<Integer> hs = new PriorityQueue<Integer>((a, b) -> { return b - a; });
        hs.add(0);
        int ph = 0;
        int ch = 0;
        List<int[]> out = new ArrayList();
        List<Keypoint> kps = new ArrayList();
        
        for (int[] b : buildings) {
            kps.add(new Keypoint(b[2], b[0], true));
            kps.add(new Keypoint(b[2], b[1], false));
        }
        
        kps.sort((a, b) -> {
            return a.x - b.x;
        });
        
        for (int i = 0; i < kps.size(); i ++) {
            Keypoint k = kps.get(i);
            if (k.s) {
                hs.add(k.h);
            } else {
                hs.remove(k.h);
            }
            if (i < kps.size() - 1 && kps.get(i + 1).x == k.x) {
                continue;
            }
            ch = hs.peek();
            if (ch != ph) {
                out.add(new int[]{k.x, ch});
            }
            ph = ch;
        }
        return out;
    } 
}