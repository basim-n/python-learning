class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def append(self,value):
        new_node=Node(value)

        if self.head==None:
            self.head=new_node
            return

        current=self.head
        while current.next is not None:
            current=current.next
        current.next=new_node

    def search(self,value):
        current=self.head
        while current is not None:
            if current.value==value:
                return True
            else:
                current=current.next

        return False
    
ll = Linkedlist()
ll.append(10)
ll.append(20)
ll.append(30)

print(ll.search(20))  # True
print(ll.search(50))  # False





        