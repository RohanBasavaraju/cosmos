class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        counter = 1
        current = self.head
        while current:
            if counter == position:
                return current
            else:
                current = current.next
                counter += 1
        return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        counter = 1
        current = self.head
        if position == 1:
            new_element.next = self.head.next
            self.head = new_element
        else:
            while current:
                if counter == position-1:
                    new_element.next = current.next
                    current.next = new_element
                    break
                else:
                    current = current.next
                    counter += 1


    def delete(self, value):
        """Delete the first node with a given value."""
        current = self.head
        if current.value == value:
            self.head = current.next
        else:
            while current.next:
                if current.next.value == value:
                    current.next = current.next.next
                    break
                else:
                    current = current.next

