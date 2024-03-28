# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        result_list = ListNode(-1)
        transfer = result_list
        while list1 or list2:
            if list1 and not(list2):
                transfer.next = ListNode(list1.val)
                transfer = transfer.next
                list1 = list1.next
            
            elif list2 and not(list1):
                transfer.next = ListNode(list2.val)
                transfer = transfer.next
                list2 = list2.next

            elif list1.val <= list2.val:
                transfer.next = ListNode(list1.val)
                transfer = transfer.next
                list1 = list1.next
            
            else:
                transfer.next = ListNode(list2.val)
                transfer = transfer.next
                list2 = list2.next

        return result_list.next
        
