class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None
class LruCache:
    def __init__(self,capacity):
        self.capacity=capacity
        
        self.cache={}

        self.dummyLru = Node(0, 0)
        self.dummyMru = Node(0, 0)
        self.dummyLru.next = self.dummyMru
        self.dummyMru.prev = self.dummyLru
        

    def add_node(self,node):
        
       
        prev_node=self.dummyMru.prev 
        
        prev_node.next=node
        node.prev=prev_node
        node.next=self.dummyMru
        self.dummyMru.prev=node

    def remove_node(self,node):
        
        node.prev.next=node.next
        node.next.prev=node.prev
        node.next=None
        node.prev=None

    def get(self,key):
        if key in self.cache:
            node=self.cache[key]
            self.remove_node(node)
            self.add_node(node)
            return node.val
        else:
            return -1
    def put(self,key,value):
        if self.capacity==0:
            return
        if key in self.cache:
            node=self.cache[key]
            node.val=value
            self.remove_node(node)
            self.add_node(node)
            
        else:
            if len(self.cache)==self.capacity:
                lru_node=self.dummyLru.next
                self.remove_node(lru_node)
                del self.cache[lru_node.key]
                node=Node(key,value)
                self.cache[key]=node
                self.add_node(node)
            else:
                node=Node(key,value)
                self.cache[key]=node
                self.add_node(node)



        
              
    
   