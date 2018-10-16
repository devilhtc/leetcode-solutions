/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        PriorityQueue<ListNode> q=new PriorityQueue<ListNode>(1000, new Comparator<ListNode>() {  
                public int compare(ListNode a, ListNode b) {                         
                    return a.val-b.val;  
                }      
            });
        for (ListNode node:lists) if (node!=null) q.add(node);
        ListNode fakeHead=new ListNode(0);
        ListNode tail=fakeHead;
        while (!q.isEmpty()) {
            ListNode next=q.poll();
            if (next.next!=null) q.add(next.next);
            tail.next=next;
            tail=tail.next;
        }
        return fakeHead.next;
    }
}