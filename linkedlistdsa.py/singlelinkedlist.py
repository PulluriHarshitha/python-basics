#creating linkedlist
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
#Implementation of Simple 4 Nodes Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
# Create nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)
# Link nodes
node1.next = node2
node2.next = node3
node3.next = node4  
head = node1  # Head points to the first node
# Traverse and print the linked list
current = head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

#singlelinkedlist
# constructor to initialize a new node with data
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
# Create the first node (head of the list)
head = Node(10)
# Link the second node
head.next = Node(20)
# Link the third node
head.next.next = Node(30)
# Link the fourth node
head.next.next.next = Node(40)
# printing linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next

#insertion 
# Constructor to initialize a new node
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
# Create the linked list
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
# Insert 50 at the end
newnode = Node(50)
temp = head
while temp.next is not None:
    temp = temp.next
temp.next = newnode
# Print the linked list
temp = head
while temp is not None:
    print(temp.data, end=" ")
    temp = temp.next

#delete the element  "30" at position
