from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, info):
        newNode = Node(info)
        if self.head is not None:
            newNode.link = self.head
            self.head = newNode
        else:
            self.head = newNode

    def insertAtEnd(self, info):
        newNode = Node(info)
        if self.head is not None:
            current = self.head
            while current.link is not None:
                current = current.link
            current.link = newNode
        else:
            self.head = newNode

    def display(self):
        current = self.head
        while current is not None:
            print(current.info)
            current = current.link

    def search(self, findNode):
        if self.head == None:
            print("List is empty")
        current = self.head
        while current is not None:
            if findNode == current.info:
                print("Found")
                return
            current = current.link


    def delete(self, deleteNode):
        if self.head == None:
            print("List is empty")
        current = self.head
        while current is not None:
            if deleteNode == current.info:
                temp = current.link
                current.link = temp.link
                temp = None
                return
            current = current.link


ll = LinkedList()
ll.insertAtBegin(10);
ll.insertAtEnd(20)
ll.display()
ll.search(20)
ll.delete(10)
ll.display()

ll.delete(20)
print("List is empty")

ll.display()

