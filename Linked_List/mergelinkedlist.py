class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def merge_list(self,list1,list2):
        curr1=list1
        curr2=list2
        head=None
        prev=None

        while curr1 is not None or curr2 is not None:
            if curr1 is None:
                 if prev is None:
                      
                      head=curr2
                      
                      break
                 else:
                      prev.next=curr2
                      break
                 

                 
            elif curr2 is None:
                 if prev is None:
                      
                      head=curr1
                      break
                      
                 else:
                    prev.next=curr1
                    break
                 
                 
            else:
                 if curr1.value<=curr2.value:

                    if head == None:
                        head = curr1
                        prev = head
                        curr1=curr1.next
                    else:
                        prev.next=curr1
                        prev=curr1
                        curr1=curr1.next
                 elif curr1.value>curr2.value:
                                if head == None:
                                    head = curr2
                                    prev = head
                                    curr2=curr2.next
                                else:
                                    prev.next=curr2
                                    prev=curr2
                                    curr2=curr2.next
        return head    
l1=Linkedlist()

l2=Linkedlist()
node7=Node(10)
node8=Node(15)
node9=Node(50)
node7.next=node8
node8.next=node9
node9.next=None


l2.head=node7

result=l1.merge_list(l1.head,l2.head)
curr=result
while curr:
     print(curr.value)
     curr=curr.next

            

            







    


    

    


    


