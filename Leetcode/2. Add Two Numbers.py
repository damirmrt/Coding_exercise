'''
Всегда помним о остатке и то что он переносится на следующую ноду
Для этого заносим остаток в условие while.
В остальном обычное сложение двух чисел из разных списков
'''

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        addition = 0

        while l1 or l2 or addition:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + addition
            addition = val // 10
            val = val % 10
            cur.next = ListNode(val)

            cur = cur.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next   