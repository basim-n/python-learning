class Node:
    def __init__(self, val, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Linkedlist:
    def __init__(self):
        self.head=None

    def copy_list(self,h1):
        
        
        if h1==None:
            return None
        
        head1=Node(h1.val)
        
        curr=h1.next
        prev=head1
        while curr is not None:
            copy_node=Node(curr.val)
            prev.next=copy_node
            prev=prev.next
            curr=curr.next
        dict_node=dict()
        p1=h1
        p2=head1
        while p1 is not None:
            dict_node[p1]=p2
            p1=p1.next
            p2=p2.next
        current=head1
        p2=h1
        while current is not None:
            if p2.random is not None:
                current.random=dict_node[p2.random]
                current=current.next
                p2=p2.next
            else:
                current.random=None
                current=current.next
                p2=p2.next
        return head1

    
        




l1=Linkedlist()
node1=Node(10)
node2=Node(20)
node3=Node(30)
node1.next=node2
node2.next=node3
node3.next=None
l1.head=node1
node1.random=node3
node2.random=None
node3.random=node3
result=l1.copy_list(l1.head)
curr=result

while curr is not None:
    print(curr.val)

    if curr.random is not None:
        print(curr.random.val)
    else:
        print(None)

    curr = curr.next


