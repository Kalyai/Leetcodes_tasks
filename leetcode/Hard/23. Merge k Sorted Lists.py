# Definition for singly-linked list.
#class ListNode(object):
#    def __init__(self, val=0, next=None):
#        self.val = val
#        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return

        node1 = lists[0]
        result = list()
        while node1 is not None:
            result.append(node1.val)
            node1 = node1.next

        for i in range(1, len(lists)):
            node = lists[i]
            now_list = list()
            while node is not None:
                now_list.append(node.val)
                node = node.next
            result = self.merge_sort(result, now_list)

        res_list_node = ListNode(0)
        for r in result:
            cur = res_list_node
            while cur.next is not None:
                cur = cur.next
            cur.next = ListNode(r)
        return res_list_node.next

    def merge_sort(self, l1, l2):
        res = list()
        i, j = 0, 0
        while i < len(l1) and j < len(l2):
            if l1[i] <= l2[j]:
                res.append(l1[i])
                i += 1
            else:
                res.append(l2[j])
                j += 1

        if i < len(l1):
            res.extend(l1[i:])

        if j < len(l2):
            res.extend(l2[j:])

        return res
