// A* implementation of problem 753 Open the Lock

class Solution {
    class LockConfig {
        String s; // string config e.g. "1234"
        int d; // distance from the seed "0000"
        int h; // heuristic distance - shortest dis from target
        int t; // total distance = d + h, used in priority queue
        public LockConfig(int dis, int heuristic, String config) {
            s = config;
            d = dis;
            h = heuristic;
            t = d + h;
        }
    }
    String tg; 
    
    public int openLock(String[] deadends, String target) {
        tg = target;
        Map<String, LockConfig> m = new HashMap();
        Set<String> de = new HashSet();
        for (String ode : deadends) {
            if (ode.equals("0000")) return -1;
            de.add(ode);
        }
        PriorityQueue<LockConfig> pq = new PriorityQueue<>( (a, b) -> { return a.t - b.t; } ); // a priority queue based on 
        String seedStr = "0000";
        LockConfig seed = new LockConfig(0, 0, seedStr);
        m.put(seedStr, seed);
        pq.add(seed);
        while (pq.size() > 0) {
            LockConfig cur = pq.poll();
            if (!de.contains(cur.s)) { // test for dead end
                String[] neighbors = getNeighbors(cur.s);
                int nextDis = cur.d + 1;
                for (String nb : neighbors) {
                    // total 4 cases for each neighbor
                    // 1. equals target : return dis
                    // 2. already visited but < : remove and add new
                    // 3. already visited but >= : do nothing
                    // 4. unvisited : add to pq
                    if (nb.equals(target)) {
                        return nextDis;
                    }
                    if (m.containsKey(nb)) {
                        if (nextDis < m.get(nb).d) {
                            pq.remove(m.get(nb));
                            pq.add(new LockConfig(nextDis, estimateDis(nb), nb));
                        } 
                    } else {
                        LockConfig next = new LockConfig(nextDis, estimateDis(nb), nb);
                        m.put(nb, next);
                        pq.add(next);
                        
                    }
                }
            }
        }
        return -1;
    }
    
    // generate neighbor of a configuration, e.g. 1234 -> [0234, 2234, 1134, 1334, .... 1235]
    private String[] getNeighbors(String config) {
        String[] out = new String[8];
        char[] configArray = config.toCharArray();
        for (int i = 0; i < 4; i++) {
            char originalChar = configArray[i];
            char[] changedChars = tweek(originalChar);
            for (int j = 0; j < 2; j ++) {
                configArray[i] = changedChars[j];
                String nb = new String(configArray);
                out[2*i + j] = nb;
            }
            configArray[i] = originalChar;
        }
        return out;
    }
    
    // tweek a character by one turn on the wheel
    private char[] tweek(char c) {
        if (c == '9') { return new char[] {'0', '8'};}
        if (c == '0') { return new char[] {'9', '1'};}
        return new char[] {(char)((int)c - 1), (char)((int)c + 1)};
    }
    
    // estimate the distance from config to the target 
    private int estimateDis(String config) {
        int total = 0;
        for (int i = 0; i < 4; i++) {
            int dif = Math.abs((int)(config.charAt(i)) - (int)(tg.charAt(i)));
            total += Math.min(dif, 10 - dif);
        }
        return total;
    }
}