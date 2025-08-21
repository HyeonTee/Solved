/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        ListNode tmp = head;
        int n = 0;
        
        while (tmp != null) {
            tmp = tmp.next;
            n++;
        }
        
        if (n < 2) {
            return null;
        }
        
        tmp=head;
        n/=2;
        
        while (n - 1 > 0) {
            n--;
            tmp=tmp.next;
        }
        
        tmp.next=tmp.next.next;
        return head;
    }
}