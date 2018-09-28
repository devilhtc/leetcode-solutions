class Solution {
    class NodeItem {
        // inner class for tracking the priority of the node
        public int k; // node key
        public boolean v; // visited
        public int m; // moves left
        public boolean o; // on PQ
        public NodeItem(int i) {
            k = i;
            v = false;
            m = 0;
            o = false;
        }
    }

    public int reachableNodes(int[][] edges, int M, int N) {
        if (M == 0) // trivial case
            return 1;

        Map<Integer, List<Integer>> e = new HashMap(); // edges
        Map<String, Integer> ew = new HashMap(); // edge weights
        Map<String, Integer> er = new HashMap(); // edge results
        Map<Integer, NodeItem> tracker = new HashMap(); // node key to node item
        PriorityQueue<NodeItem> pq = new PriorityQueue<NodeItem>((a, b) -> (
            b.m - a.m
        )); // for deciding traveling order, get the node with the most moves left
        
        NodeItem ni;
        Integer m, n;
        String key1, key2;
        
        for (int i = 0; i < N; i++)
            tracker.put(i, new NodeItem(i));

        for (int i = 0; i < edges.length; i++) {
            m = edges[i][0];
            n = edges[i][1];
            key1 = toKey(m, n);
            key2 = toKey(n, m);
            if (!e.containsKey(m))
                e.put(m, new ArrayList());
            if (!e.containsKey(n))
                e.put(n, new ArrayList());
            e.get(m).add(n);
            e.get(n).add(m);
            ew.put(key1, edges[i][2]);
            ew.put(key2, edges[i][2]);
            er.put(key1, 0);
            er.put(key2, 0);
        }

        NodeItem start = tracker.get(0);
        start.m = M;
        start.o = true;
        pq.add(start);

        while (pq.size() > 0) {
            NodeItem cur = pq.poll();
            int ml = cur.m; // current moves left
            cur.v = true; // marking visited only at popping
            if (!e.containsKey(cur.k))
                continue;

            for (Integer k : e.get(cur.k)) {
                NodeItem child = tracker.get(k);
                String edgeKey = toKey(cur.k, k);
                int w = ew.get(edgeKey); // weight

                // update the result of traveled nodes
                // on that edge
                er.put(
                    edgeKey, 
                    Math.min(
                        w, Math.max(ml, er.get(edgeKey))
                    )
                );
                
                if (!child.v && ml > w) {
                    // child to be visited
                    if (child.o) {
                        if (child.m < ml - w - 1) {
                            // child had less moves, udpate
                            pq.remove(child);
                            child.m = ml - w - 1;
                            pq.add(child);
                        }
                    } else {
                        // not yet on pq, add to pq
                        child.o = true;
                        child.m = ml - w - 1;
                        pq.add(child);
                    }
                }
            }
        }

        int res = 0;
        for (int i = 0; i < N; i++)
            if (tracker.get(i).v)
                res++;
        
        for (int i = 0; i < edges.length; i++) {
            m = edges[i][0];
            n = edges[i][1];
            key1 = toKey(m, n);
            key2 = toKey(n, m);      
            res += Math.min(
                er.get(key1) + er.get(key2),
                ew.get(key1)
            );
        }

        return res;
    }

    private String toKey(Integer m, Integer n) {
        return Integer.toString(m) + "," + Integer.toString(n);
    }
}