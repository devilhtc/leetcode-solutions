/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode newHead=head;
        if (head!=null && head.next!=null) {
            newHead=head.next;
        } else {
            return head;
        }
        swap(null,head);
        return newHead;
    }
    
    private void swap(ListNode prev,ListNode node) {
        if (node==null) {
            prev.next=null; 
            return;
        }
        if (node.next==null) {
            prev.next=node;
            return;
        }
        ListNode next=node.next;
        if (prev!=null) {
            prev.next=next;
            //System.out.println(prev.val);
        }
        ListNode temp=next.next;
        next.next=node;
        swap(node,temp);
        return;
    }
}