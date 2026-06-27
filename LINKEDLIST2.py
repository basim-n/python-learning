class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)        # create new paper
        
        if self.head is None:         # if list is empty
            self.head = new_node      # new paper is the first one
            return
        
        current = self.head           # start at first paper
        while current.next is not None:  # keep going until last paper
            current = current.next    # follow directions
        current.next = new_node       # attach new paper at the end

    def display(self):
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next

    def delete(self,value):
        current=self.head
        prev=None

        while current is not None:
            if current.value==value:
                if prev ==None:
                    self.head=current.next
                    return
                else:
                    prev.next=current.next
                    return
            else:
                prev=current
                current=current.next

        return 'Value not found'
    
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)



ll.display()    # 10 20 30
ll.delete(10)   # delete head
ll.display()    # should show 20 30
ll.delete(30)   # delete last node
ll.display()    # should show 20
print(ll.delete(99))  # Value not found
            



