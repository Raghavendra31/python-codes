# class ListNode:
#     def __init__(self,val):
#         self.val = val 
#         self.next = None


# class Solution(object): # Added (object) for Python 2 compatibility
#     def addTwoNumbers(self, l1, l2):
#         dummy = ListNode(0)
#         current = dummy
#         carry = 0
        
#         while l1 or l2 or carry:
#             # Use getattr or a simple if/else for safetyy
#             v1 = l1.val if l1 else 0
#             v2 = l2.val if l2 else 0
            
#             total = v1 + v2 + carry
#             carry = total // 10
            
#             current.next = ListNode(total % 10)
            
#             current = current.next
#             if l1: l1 = l1.next
#             if l2: l2 = l2.next
            
#         return dummy.next




class Node:
    def __init__(self,data1 = None,data2 = None):
        self.head1 = data1
        self.head2 = data2
        self.nref1 = None
        self.nref2 = None


class create_Ll(l1,l2):
    def __init__(self):
        self.head1 = Node([1,2,3,4])

    def check_l1(l1):
        temp = 
        if temp.head1 is not None:
            print(temp.head1)

        while temp.head1 is not None:
            
            if temp.nref1 is not None:

                print(temp.nref1)
            temp = temp.nref1



            
             