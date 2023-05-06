# Create node class
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

# Create Single Linked List class
class SLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def insert(self, value, location):
        newNode = Node(value)
        # Checking to see if the SLL is empty or not
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                # Need to start from head to traverse
                tempNode = self.head
                # Starting traversal index
                index = 0
                # While loop to find the correct index needed
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                # Inserting new node into SLL
                # nextNode is a temp variable
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
                if tempNode == self.tail:
                    self.tail = newNode

    def search(self, value):
        if self.head is None:
            return "The list does not exist"
        else:
            runner = self.head
            while runner is not None:
                if runner.value == value:
                    return True
                runner = runner.next
            return "The value does not exist in this list"

    def delete(self, location):
        if self.head is None:
            return "The list does not exist"
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    runner = self.head
                    while runner is not None:
                        if runner.next == self.tail:
                            runner.next = None
                            self.tail = runner
                        runner = runner.next
            else:
                runner = self.head
                index = 0
                while index < location -1:
                    runner = runner.next
                    index += 1
                nextNode = runner.next
                runner.next = nextNode.next
    
    def deleteSLL(self):
        if self.head is None:
            return "The list does not exist"
        else:
            self.head = None
            self.tail = None



SLL1 = SLL()
SLL1.insert(1,1)
SLL1.insert(2,1)
SLL1.insert(3,1)
SLL1.insert(4,1)
SLL1.insert(0,0)
SLL1.insert(0,4)
print(SLL1.search(3))
print([node.value for node in SLL1])
SLL1.delete(2)
SLL1.deleteSLL()
print([node.value for node in SLL1])