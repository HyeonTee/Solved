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
    public int pairSum(ListNode head) {
        int max = 0;
        
        ListNode mid = head;
        ListNode pointer = head;
        while(pointer != null && pointer.next != null) {
            mid=mid.next;
            pointer=pointer.next.next;
        }
        
        ListNode prev = null;
        ListNode next;
        while (mid != null) {
            next = mid.next;
            mid.next = prev;
            prev = mid;
            mid = next;
        }
        
        while (prev != null) {
            max = Math.max(max, head.val + prev.val);
            head = head.next;
            prev = prev.next;
        }
        
        return max;
    }
    
}