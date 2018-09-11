class FreqStack {
    class FSItem {
        public int v;
        public List o;
        
        public FSItem(int val) {
            v = val;
            o = new LinkedList<Integer>();
        }
    }
    
    PriorityQueue<FSItem> pq; 
    Map<Integer, FSItem> tracker;
    int idx;
    
    public FreqStack() {
        pq = new PriorityQueue<FSItem>(10, (a, b) -> {
            int l = a.o.size();
            if (a.o.size() != b.o.size()) {
                return b.o.size() - a.o.size();
            } else {
                return (int) b.o.get(l-1) - (int) a.o.get(l-1);
            }
        });
        tracker = new HashMap<Integer, FSItem>();
        idx = 0;
    }
    
    public void push(int x) {
        FSItem item;
        if (tracker.containsKey(x)) {
            item = tracker.get(x);
            pq.remove(item);
        } else {
            item = new FSItem(x);
            tracker.put(x, item);
        }
        item.o.add(idx++);
        pq.add(item);
    }
    
    public int pop() {
        FSItem item = pq.poll();
        item.o.remove(item.o.size() - 1);
        if (item.o.size() == 0) {
            tracker.remove(item.v);
        } else {
            pq.add(item);
        }
        return item.v;
    }
}

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack obj = new FreqStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 */