class LRUCache {
    class DLinkedNode {
        int key;
        int val;
        DLinkedNode next;
        DLinkedNode prev;
        public DLinkedNode(int key1, int val1) {
            key=key1;
            val=val1;
            next=null;
            prev=null;
        }
    }
    
    class DLinkedList {
        DLinkedNode head;
        DLinkedNode tail;
        
        public DLinkedList() {
            head=null;
            tail=null;
        }
        
        // prepend a node
        public void prepend(DLinkedNode node) {
            if (head==null) {
                head=node;
                tail=node;
            } else {
                head.prev=node;
                node.next=head;
                head=node;
            }
        }
        
        // remove something found in the linkedlist
        public void remove(DLinkedNode node) {
            if (node==head && node == tail) {
                head=null;
                tail=null;
            } else if (node==head) {
                head=head.next;
                head.prev=null;
            } else if (node==tail) {
                tail=tail.prev;
                tail.next=null;
            } else {
                node.next.prev=node.prev;
                node.prev.next=node.next;
            }
        }
        
    }
    
    int cap;
    int length;
    Map<Integer,DLinkedNode> map;
    DLinkedList myList;
    
    public LRUCache(int capacity) {
        cap=capacity;
        length=0;
        map=new HashMap<Integer,DLinkedNode>();
        myList=new DLinkedList();
    }
    
    public int get(int key) {
        if (map.containsKey(key)) {
            DLinkedNode node =map.get(key);
            myList.remove(node);
            myList.prepend(node);  
            return node.val;
        } else {
            return -1;
        }
    }
    
    public void put(int key, int value) {
        if (map.containsKey(key)) {
            DLinkedNode node =map.get(key);
            node.val=value;
            myList.remove(node);
            myList.prepend(node);  
        } else {
            DLinkedNode node = new DLinkedNode(key,value);
            myList.prepend(node);
            map.put(key,node);
            
            if (length==cap) {
                map.remove(myList.tail.key);
                myList.remove(myList.tail);
            } else {
                length++;
            }
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */