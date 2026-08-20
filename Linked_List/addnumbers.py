class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None


    def addnumbers(self,head1,head2):
        
        p1=head1
        p2=head2
        carry=0
        head=None
        prev= None
        while p1 is not None or p2 is not None:
            
            
            
            if p2 is None:
                 total=p1.value+carry
                 digit,carry=  total%10,total//10
            elif p1 is None:
                total=p2.value+carry
                digit,carry=total%10,total//10
            else:
                total=p1.value+p2.value+carry
                digit,carry=total%10,total//10

            
            
            new_node=Node(digit)
            if head is None:
                head=new_node
            if prev == None:
                prev=new_node
            else:
                prev.next=new_node
                prev=new_node

            
            
            if p1 is not None and p2 is not None:
                p1=p1.next
                p2=p2.next
            elif p2 is not None:
                p2=p2.next
            else:
                p1=p1.next
        if carry == 1:
            new_node=Node(carry)
            prev.next=new_node
            
        return head
       


    


    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.value, end=" --> ")
            curr=curr.next
        print("None")


   

    


l1=Linkedlist()
node1=Node(9)
node2=Node(9)


node1.next=node2
node2.next=None


l1.head=node1
l2=Linkedlist()
node7=Node(1)

node7.next=None



l2.head=node7

result=l1.addnumbers(l1.head,l2.head)
curr=result

while curr is not None:
        print(curr.value)
        curr=curr.next

