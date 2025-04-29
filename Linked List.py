class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Insert at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Delete a node by value
    def delete(self, key):
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current is None:
            print("Node not found.")
            return

        prev.next = current.next

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

# Example usage
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.prepend(5)
ll.append(30)
ll.display()        # Output: 5 -> 10 -> 20 -> 30 -> None
ll.delete(20)
ll.display()        # Output: 5 -> 10 -> 30 -> None
