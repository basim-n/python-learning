class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def rotate_list(self,head,k):
       if head is None:
           return head
       curr=head
       length=1
       while curr.next is not None:
           curr=curr.next
           length+=1
       last_node=curr
       k=k%length
       if k == 0:
           return head

       new_tail_position=length-k
       position=1
       curr=head
       while curr is not None:
           if position == new_tail_position:
               last_node.next=head
               head=curr.next
               curr.next=None
               break
           else:
               
               curr=curr.next
               position+=1
       return head  

    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.val, end=" --> ")
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
l1.head=l1.rotate_list(l1.head,2)


l1.printelement()