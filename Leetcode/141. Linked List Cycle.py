'''
в итоге все равно fast и  slow встретяться 

Time O(n)
Space O(1)
'''

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast, slow = head,head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
