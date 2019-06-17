

class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        
        n = []
        node = self.head
        while node is not None:
            if node.value == val:
                n += [node]
            node = node.next
        return n


    def delete(self, val, all=False):
        
        if all:
            
            if self.head is None:
                return

            while self.head is not None and self.head.value == val:
                self.head = self.head.next
            if self.head is not None:
                current = self.head
                while current.next is not None:
                    if current.next.value == val:
                        current.next = current.next.next
                    else:
                        current = current.next
                               

        if self.head is None:
            return
        
        cur_node = self.head
        
        if cur_node and cur_node.value == val:
            self.head = cur_node.next
            cur_node = None
            return
        
        prev = None
        while cur_node and cur_node.value != val:
            prev = cur_node
            cur_node = cur_node.next
        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None              

    def clean(self):
        self.__init__()

    def len(self):
        
        count = 0
        current_node = self.head

        while current_node is not None:
            
            count = count + 1

            current_node = current_node.next

        return count
    

    def insert(self, afterNode, newNode):
        
        if afterNode and self.head is None: 
            
            self.head = newNode
        else:    
            
            newNode.next = afterNode.next 
            
            afterNode.next = newNode 









