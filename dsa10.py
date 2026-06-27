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

    def length(self):
        count=0
        current=self.head
        while current is not None:
            count+=1
            current=current.next

        return count

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
print(ll.length())  # should print 3