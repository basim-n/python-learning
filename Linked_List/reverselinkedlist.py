class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def reverse_list(self,head,left,right):
         before=None
         curr=head
         next=None
         after=None
         position=1
         reverse_tail=None
         while curr is not None:
              
             
              if position != left:
                   position+=1
                   before=curr
                   curr=curr.next
                   
              else:
                   reverse_tail=curr
                   after=curr.next
                   while position<right:
                       
                       
                       next=after
                       after=next.next
                       next.next=curr
                       curr=next
                       
                       
                       position+=1


                   reverse_tail.next=after
                   if before is not None:
                       before.next=next
                   else:
                       head=curr
                       break
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
node6 = Node(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = None
l1.head=node1
l1.reverse_list(l1.head,3,5)
l1.printelement()