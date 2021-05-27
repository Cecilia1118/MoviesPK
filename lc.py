# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """

#         p1, p2 = headA, headB                       # 初始化两个运动结点p1和p2
#         while p1 != p2:                             # 只要两个结点还未相遇
#             p1 = headB if p1 is None else p1.next   # 如果p1走到了链表A的末尾，则换到链表B上
#             p2 = headA if p2 is None else p2.next   # 如果p2走到了链表B的末尾，则换到链表A上

#         return p1 

def reverseList(self, head):
       
        p = head
        newList = []
        while p:
            newList.insert(0, p)
            p = p.next

        p = head
        for v in newList:
            p = v
            p = p.next
        return head

res = reverseList([1,2,3],1)
print(res)