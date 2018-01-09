/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        if (l1==null) return l2;
        if (l2==null) return l1;
        ListNode newhead=new ListNode(Math.min(l1.val,l2.val)-1);
        ListNode node=newhead;
        while (l1!=null || l2!=null) {
            if (l1==null) {
                node.next=l2;
                l2=l2.next;
            } else if (l2==null) {
                node.next=l1;
                l1=l1.next;
            } else if (l1.val<l2.val) {
                node.next=l1;
                l1=l1.next;
            } else {
                node.next=l2;
                l2=l2.next;
            }
            node=node.next;
        }
        return newhead.next;
    }
}