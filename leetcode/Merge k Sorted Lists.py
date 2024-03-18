# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        if len(lists) == 0:
            return

        heap = list()
        for l in lists:
            while l is not None:
                elem = l.val
                self.heapify(heap, elem)
                l = l.next
        if len(heap) == 0:
            return
        res = []
        for i in range(len(heap)):
            res.append(self.pop_left(heap))

        res_list_node = ListNode(res[0])
        for i in range(1, len(res)):
            new_node = ListNode(res[i])
            cur = res_list_node
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        return res_list_node

    def heapify(self, heap, elem):
        heap.append(elem)
        pos = len(heap) - 1
        parent = (pos - 1) // 2
        while parent >= 0:
            if heap[parent] > heap[pos]:
                heap[parent], heap[pos] = heap[pos], heap[parent]
                pos = parent
                parent = (pos - 1) // 2
            else:
                break

    def pop_left(self, heap):
        elem_which_delete = heap[0]
        heap[0] = heap[-1]
        heap.pop()
        pos = 0
        while (pos * 2 + 2) < len(heap):
            pos = pos * 2 + 1
            if heap[pos + 1] < heap[pos]:
                pos += 1
            if heap[pos] < heap[(pos - 1) // 2]:
                heap[pos], heap[(pos - 1) // 2] = heap[(pos - 1) // 2], heap[pos]
            else:
                break

        if pos * 2 + 2 == len(heap):
            if heap[pos * 2 + 1] < heap[pos]:
                heap[pos * 2 + 1], heap[pos] = heap[pos], heap[pos * 2 + 1]

        return elem_which_delete
