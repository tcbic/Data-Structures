# import sys
# sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

# Characteristics
# -linear data structure
# -flexible size
# -FIFO (First In First Out)- Think about a line of people waiting to get into 
# a movie theatre.

class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # Complexity of 1 (Constant) to add to the front or back.
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        """Add a node to the tail."""
        # The size of the queue increases by 1.
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        """Remove a node from the head."""
        if self.size > 0:
            # The size of the queue decreases by 1.
            self.size -= 1
            return self.storage.remove_from_head()
        else:
            return None

    def len(self):
        """Return the length/size of the queue."""
        return self.size