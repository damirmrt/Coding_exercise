'''
Сощдаем пустую ноду перед head. Далее двигаем right на знеачение n.
Двигаем left и right пока right не будет на последней ноде.
Меняем next для левой так как left.next это ноджа которую надо удалитью
Djpdhfoftv dummy.next потому что он стоит до head
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy 
        right = head

        while n > 0:
            right = right.next
            n -= 1
        
        while right:
            left = left.next
            right = right.next
        
        left.next = left.next.next
        return dummy.next