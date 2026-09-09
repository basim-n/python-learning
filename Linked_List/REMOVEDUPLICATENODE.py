class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def remove_node(self,head):
        curr=head
        prev=None
        while curr is not None and curr.next is not None:
            if curr.val == curr.next.val:
                if curr == head:
                    dup=curr.val
                    while curr is not None and curr.val==dup :
                        curr=curr.next
                    head=curr
                else:
                     dup=curr.val
                     while curr is not None and curr.val==dup :
                        
                            curr=curr.next
                        
                     prev.next=curr
                     
                     
                     
            else:
                prev=curr
                curr=curr.next

        return head


            


    


    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.val, end=" --> ")
            curr=curr.next
        print("None")


   

    



l1=Linkedlist()
node1 = Node(1)
node2 = Node(1)
node3 = Node(2)

node4 = Node(2)
node5 = Node(3)
node6=Node(4)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next=None


l1.head=node1
l1.head=l1.remove_node(l1.head)


l1.printelement()