# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        transfer = list()
        while head is not None:
            transfer.append(head.val)
            head = head.next

        result = ListNode(-1)
        fake = result
        for trans in transfer[::-1]:
            fake.next = ListNode(trans)
            fake = fake.next
        return result.next
