# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Characteristics
# -linear data structure
# -flexible size
# LIFO (Last In First Out)- Think about a stack of plates.

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        #
        self.storage = DoublyLinkedList()

    def push(self, value):
        """Add a new node to the top of the stack."""
        # Size of the stack increases by 1.
        self.size += 1
        self.storage.add_to_head(value)

    def pop(self):
        """Removes a node from the top of the stack."""
        if self.size > 0:
            # Size of the stack decreases by 1.
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        """Return the length/size of the stack."""
        return self.size