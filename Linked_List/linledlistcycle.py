class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None


    


    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.value, end=" --> ")
            curr=curr.next
        print("None")


    def contain_cycle(self):
        slow=fast=self.head
        
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next

            if fast is slow:
                return True

        return False


    


l1=Linkedlist()
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)
node5=Node(50)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=None
l1.head=node1
print(l1.contain_cycle())

