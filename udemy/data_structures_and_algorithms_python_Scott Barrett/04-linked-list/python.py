# Appending to back of a SLL = 0(1) - doesnt matter how many nodes it will be the same number of operations
# Remove from back of a SLL = 0(n) - iterate through SLL to find the right pointer
# Appending to the front of a SLL = 0(1) - doesnt matter how many nodes it will be the same number of operations
# Remove from front of a SLL = 0(1) - doesnt matter how many nodes it will be the same number of operations
# Adding item to the middle of a SLL = 0(n) - iterate through the list to find where we want to add new node
# Remove from middle of a SLL = 0(n) - doesnt matter how many nodes it will be the same number of operations
# Look up by value or index = 0(n) - iterate through the list to find the node with the value we are looking for


head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value":7,
                "next": None
            }
        }
    }
}

# print(head["next"]["next"]["value"])

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # initalize list and create new Node
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    # create new Node
    # add Node to end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # create new Node
    # add Node to beggining
    def prepend(self, value):
        pass

    # create new Node
    # insert Node
    def insert(self, index, value):
        pass
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(f"value: {temp.value}")
            temp = temp.next
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next != None):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

my_linked_list = LinkedList(4)
my_linked_list2 = LinkedList(11)
my_linked_list2.append(3)
my_linked_list2.append(23)
my_linked_list2.append(7)
my_linked_list2.append(4)
my_linked_list2.pop()
print(my_linked_list2.print_list())