class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CDLL:
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

    def reverseDisplay(self):
        runner = self.tail
        result = ""
        while runner != None:
            if runner != self.head:
                result = result + str(runner.value) + ", "
            else:
                result = result + str(runner.value)
                break
            runner = runner.prev
        print(result)

    def createCDLL(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.next = newNode
        newNode.prev = newNode
        print("The circular doubly linked list has been created")

    def addFront(self, value):
        newNode = Node(value)
        newNode.next = self.head
        newNode.prev = self.tail
        self.head.prev = newNode
        self.head = newNode
        self.tail.next = newNode

    def addBack(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        newNode.next = self.head
        self.tail.next = newNode
        self.tail = newNode
        self.head.prev = newNode

    def insert(self, value, location):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            newNode = Node(value)
            if self.head == self.tail:
                self.head.next = None
                self.tail.next = None
                self.tail = None
                self.head = None
            elif location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.head = newNode
            elif location == -1:
                newNode.prev = self.tail
                newNode.next = self.head
                self.tail.next = newNode
                self.head.prev = newNode
                self.tail = newNode
            else:
                runner = self.head
                index = 0
                while index < location -1:
                    runner = runner.next
                    index += 1
                nextNode = runner.next
                newNode.next = nextNode
                newNode.prev = runner
                runner.next = newNode
                nextNode.prev = newNode
                # newNode.next = runner.next
                # newNode.prev = runner
                # newNode.next.prev = newNode
                # runner.next = newNode
            return "The node has been successfully deleted"

    def traversal(self):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            runner = self.head
            while runner:
                print(runner.value)
                if runner == self.tail:
                    break
                runner = runner.next

    def reverseTraversal(self):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            runner = self.tail
            while runner:
                print(runner.value)
                if runner == self.head:
                    break
                runner = runner.prev

    def search(self, value):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            runner = self.head
            while runner:
                if runner.value == value:
                    return True
                if runner == self.tail:
                    return False
                runner = runner.next

    def deleteFront(self):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head

    def deleteBack(self):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail

    def deleteNode(self, location):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = None
                self.tail = None
            else:
                if location == 0:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
                elif location == -1:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    runner = self.head
                    index = 0
                    while index < location -1:
                        index += 1
                        runner = runner.next
                        if runner == self.tail:
                            print("Index is out of list range")
                            return self
                    runner.next = runner.next.next
                    runner.next.prev = runner


    def deleteCDLL(self):
        if self.head is None:
            print("The circular doubly linked list does not exist")
        else:
            self.tail.next = None
            runner = self.head
            while runner:
                runner.prev = None
                runner = runner.next
            self.head = None
            self.tail = None
            print("The CDLL has been successfully deleted")

CDLL1 = CDLL()
CDLL1.createCDLL(0)
CDLL1.addBack(1)
CDLL1.addBack(2)
CDLL1.addBack(3)
CDLL1.addBack(4)
CDLL1.insert(5,-1)
print([node.value for node in CDLL1])
# CDLL1.reverseDisplay()
# CDLL1.traversal()
# CDLL1.reverseTraversal()
# print(CDLL1.search(2))
# CDLL1.deleteBack()
CDLL1.deleteNode(2)
CDLL1.deleteCDLL()
print([node.value for node in CDLL1])