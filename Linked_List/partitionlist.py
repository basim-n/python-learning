class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def partition_list(self,head,x):
        curr=head
        less_head=None
        greater_head=None

        while curr is not None:
            if curr.val<x:
                if less_head==None:
                    less_head=curr
                    less=curr
                    curr=curr.next
                else:
                    less.next=curr
                    less=less.next
                    curr=curr.next
            else:
                if greater_head==None:
                    greater_head=curr
                    greater=curr
                    curr=curr.next
                else:
                    greater.next=curr
                    greater=greater.next
                    curr=curr.next
        if greater_head != None and less_head != None:
            less.next=greater_head
            greater.next=None
            return less_head
        elif greater_head != None and less_head != None:
                    return None
        elif less_head==None:
            greater.next=None
            return greater_head
        elif greater_head==None:
            less.next=None
            return less_head
        else:
            return None


    
    def printelement(self):
        curr=self.head
        while curr !=None:
            print(curr.val, end=" --> ")
            curr=curr.next
        print("None")


   

    



l1=Linkedlist()
node1 = Node(1)
node2 = Node(5)
node3 = Node(2)

node4 = Node(4)
node5 = Node(3)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = None



l1.head=node1

l1.head=l1.partition_list(l1.head,3)



l1.printelement()