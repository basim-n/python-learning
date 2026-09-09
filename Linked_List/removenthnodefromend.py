class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def remove_node(self,head,n):
        if head is None:
            return head
        slow=head
        fast = head

        
        while n>0:
            fast=fast.next
            n-=1
        if fast is None:
            return head.next
        
        while fast.next is not  None:
            slow=slow.next
            fast=fast.next
            
        slow.next=slow.next.next

        return head


    


    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.value, end=" --> ")
            curr=curr.next
        print("None")


   

    



l1=Linkedlist()
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None


l1.head=node1
l1.head=l1.remove_node(l1.head,5)

l1.printelement()