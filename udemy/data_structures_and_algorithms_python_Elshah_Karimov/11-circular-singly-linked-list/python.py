class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class CSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):
        # Create new node
        newNode = Node(nodeValue)

        # The node references itself because it is the only node
        newNode.next = newNode

        # Set head and tail to node like regular SLL
        self.head = newNode
        self.tail = newNode
        return "The CSLL has been created"

    def addFront(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode

    def addBack(self, value):
        newNode = Node(value)
        if self.head is None:
            newNode.next = newNode
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
            newNode.next = self.head

    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:
            return "The head reference is None"
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                runner = self.head
                index = 0
                while index < location -1:
                    index += 1
                    runner = runner.next
                nextNode = runner.next
                runner.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted"

    def display(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            runner = self.head
            result = ""
            while runner != None:
                if runner != self.tail:
                    result = result + str(runner.value) + ", "
                else:
                    break
                runner = runner.next
            print(result[:-2])

    def search(self, value):
        if self.head is None:
            print("The linked list does not exist")
        else:
            runner = self.head
            while runner:
                if runner.value == value:
                    return True
                if runner == self.tail:
                    return "The value does not exist in the linked list"
                runner = runner.next

    def deleteFront(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
            print("The first node was succesffuly deleted")

    def deleteBack(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                runner = self.head
                while runner.next != self.tail:
                    runner = runner.next
                self.tail = runner
                self.tail.next = self.head
                print("The last node was succesffuly deleted")

    def deleteNode(self, location):
        if self.head is None:
            print("The linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.tail.next = self.head
                    print("The first node was successfully deleted")
                elif location == -1:
                    runner = self.head
                    while runner.next != self.tail:
                        runner = runner.next
                    self.tail = runner
                    self.tail.next = self.head
                    print("The last node was successfully deleted")
                else:
                    runner = self.head
                    index = 0
                    while index < location -1:
                        if runner == self.tail:
                            break
                        index += 1
                        runner = runner.next
                    runner.next = runner.next.next
                    print("The node was successfully deleted")

    def deleteCSLL(self):
        if self.head is None:
            print("The linked list does not exist")
        else:
            self.head = None
            self.tail.next = None
            self.tail = None
            print("The CSLL has been deleted")


CSLL1 = CSLL()
CSLL1.createCSLL(1)
CSLL1.insert(0,0)
CSLL1.insert(2,-1)
CSLL1.insert(3,-1)
CSLL1.insert(4,-1)
CSLL1.insert(5,-1)
CSLL1.display()
# CSLL1.deleteFront()
# CSLL1.deleteBack()
# CSLL1.deleteNode(0)
CSLL1.deleteCSLL()
CSLL1.display()
# print(CSLL1.search(4))
print([node.value for node in CSLL1])