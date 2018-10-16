/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // if is null, return null
        if (head==null) return head;
        if (k==1) return head;
        if (head.next==null) return head;
        // take at most k steps, find the end node
             
        int l=1;
        ListNode node=head;
        while (node.next!=null && l<k) {
            node=node.next;
            l+=1;
        }
        ListNode newHead=node;
        
        // if there is more recurse on the remaining nodes
        ListNode remain=null;
        if (l<k) return head;
        if (l>=k) {
            remain=node.next;
        }
        remain=reverseKGroup(remain,k);
           
        // reverse current segment 
        ListNode prev=head;
        ListNode cur=head.next;
       
        ListNode tail=head;
        tail.next=null;
        while (cur.next != null && cur!=newHead) {
            ListNode next=cur.next;
            cur.next=prev;
            prev=cur;
            cur=next;
        }
        cur.next=prev;
        
        // concat them and return head
        tail.next=remain;
        return newHead;    
    }
}