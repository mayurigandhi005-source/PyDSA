def solution():

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None

    class LinkedList:
        def __init__(self):
            self.head = None

        def append(self, data):
            new_node = Node(data)

            if self.head is None:
                self.head = new_node
                return

            current = self.head

            while current.next is not None:
                current = current.next

            current.next = new_node

        def display(self):
            current = self.head

            while current is not None:
                print(current.data, end=" ")
                current = current.next

            print()

        def insert(self, data, position):
            new_node = Node(data)

            if position < 1:
                return

            if position == 1:
                new_node.next = self.head
                self.head = new_node
                return

            current = self.head
            count = 1

            while current is not None and count < position - 1:
                current = current.next
                count += 1

            if current is None:
                return

            new_node.next = current.next
            current.next = new_node

        def middle(self):
            slow = self.head
            fast = self.head

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

            if slow is not None:
                print(slow.data)

        def delete(self, value):
            current = self.head

            if current is not None and current.data == value:
                self.head = current.next
                return

            while current is not None and current.next is not None:
                if current.next.data == value:
                    current.next = current.next.next
                    return

                current = current.next

        def reverse(self):
            previous = None
            current = self.head

            while current is not None:
                next_node = current.next
                current.next = previous
                previous = current
                current = next_node

            self.head = previous

        def consecutive_sum(self):
            current = self.head

            while current is not None and current.next is not None:
                total = current.data + current.next.data
                print(total, end=" ")
                current = current.next

            print()
    ll = LinkedList()

    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)
    ll.append(50)
    ll.display()
    ll.insert(25, 3)
    ll.display()
    ll.middle()
    ll.delete(30)
    ll.display()
    ll.reverse()
    ll.display()
    ll.consecutive_sum()
solution()
            