class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, value):
        newNode = Node(value)
        newNode.prev = None
        newNode.next = None
        self.head = newNode
        self.tail = newNode
        return "The DLL is created successfully"

    def addFront(self, value):
        if self.head is None:
            print("The node cannot be inserted in an empty list")
        newNode = Node(value)
        newNode.prev = None
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def addBack(self, value):
        if self.head is None:
            print("The node cannot be inserted in an empty list")
        newNode = Node(value)
        newNode.next = None
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode

    def insert(self, value, location):
        if self.head is None:
            print("The node cannot be inserted in an empty list")
        newNode = Node(value)
        index = 0
        runner = self.head
        while index < location - 1:
            runner = runner.next
            index += 1
        newNode.next = runner.next
        newNode.prev = runner
        runner.next.prev = newNode
        runner.next = newNode

    def display(self):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            runner = self.head
            result = ""
            while runner != None:
                if runner != self.tail:
                    result = result + str(runner.value) + ", "
                else:
                    result = result + str(runner.value)
                runner = runner.next
            print(result)

    def reverseDisplay(self):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            runner = self.tail
            result = ""
            while runner != None:
                if runner != self.head:
                    result = result + str(runner.value) + ", "
                else:
                    result = result + str(runner.value)
                runner = runner.prev
            print(result)

    def search(self, searchValue):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            runner = self.head
            while runner != None:
                if runner.value == searchValue:
                    return runner.value
                runner = runner.next
            return "The node does not exist in the DLL"

    def deleteFront(self):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def deleteBack(self):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None

    def deleteNode(self, deleteNode):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            if deleteNode == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif deleteNode == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                runner = self.head
                index = 0
                while index < deleteNode -1:
                    if runner.next == self.tail and deleteNode - index > 1:
                        print("Index is out of range, no nodes were deleted")
                        return self.display()
                    index += 1
                    runner = runner.next
                runner.next = runner.next.next
                runner.next.prev = runner
            return self.display()

    def deleteDLL(self):
        if self.head is None:
            print("The doubly linked list does not exist")
        else:
            runner = self.head
            while runner != None:
                runner.prev = None
                runner = runner.next
            self.head = None
            self.tail = None
            return "The DLL has been deleted"


DLL1 = DLL()
DLL1.createDLL(5)
DLL1.addFront(12)
DLL1.addBack(8)
DLL1.insert(6,2)
DLL1.addFront(9)
DLL1.addBack(2)
DLL1.insert(7,3)
# DLL1.display()
# DLL1.deleteBack()
# DLL1.reverseDisplay()
# print(DLL1.search(9))
# DLL1.deleteFront()
# DLL1.deleteBack()
# DLL1.deleteNode(5)
DLL1.deleteDLL()
DLL1.display()
DLL1.reverseDisplay()