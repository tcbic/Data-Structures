"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        # This is a pointer.
        self.prev = prev
        # This is a pointer.
        # If we just had this pointer, we would know that it's a singly linked list.
        self.next = next
        # Two pointers indicate it's a doubly linked list.

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        # Create a new node.
        new_node = ListNode(value, None, None)
        # The length of the list increases by 1 when we add a new node.
        self.length += 1
        # If there is no head or tail, we know that the list must be empty.
        # Therefore, the new node is the head and the tail.
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # The current head becomes the new node's next node.
            new_node.next = self.head
            # The new node is now before (previous) to the old head.
            self.head.prev = new_node
            # The new node is now the head of the list.
            self.head = new_node

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        # Grab the value.
        value = self.head.value
        self.delete(self.head)
        return value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        # Create a new node.
        new_node = ListNode(value, None, None)
        # The length of the list increases by 1 when we add a new node.
        self.length += 1
        # If there is no head or tail, we know that the list must be empty.
        # Therefore, the new node is the head and the tail.
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            # The current tail becomes the new node's previous node.
            new_node.prev = self.tail
            # The next node from the old tail is now the new node.
            self.tail.next = new_node
            # The new node is now the tail of the list.
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        # Grab the value.
        value = self.tail.value
        # Delete the current tail value using the delete method.
        self.delete(self.tail)
        return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
            value = node.value
            self.delete(node)
            self.add_to_head(value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
            value = node.value
            self.delete(node)
            self.add_to_tail(value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail."""
    def delete(self, node):
        # We are deleting a node, hence the length of the list decreases by 1.
        self.length -= 1
        # What are the special cases we need to consider...
        # If the linked list is empty...
        if not self.head and not self.tail:
            # TODO: Error handling
            return
        # If the node is the head and the tail...
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        # If the node is the head...
        elif self.head == node:
            # The current head becomes the next node.
            self.head = self.head.next
            # Delete the node.
            node.delete()
        # If the node is the tail...
        elif self.tail == node:
            # The current tail becomes the previous node.
            self.tail = self.tail.prev
            # Delete the node.
            node.delete()
        # Otherwise...
        else:
            node.delete()
        
    """Returns the highest value currently in the list."""
    def get_max(self):
        # If self.head doesn't exist...
        if not self.head:
            return None
        else:
            max_value = self.head.value
            current_val = self.head
            while current_val:
                # If current value is greater than the max value, we found a new 
                # max value.
                if current_val.value > max_value:
                    max_value = current_val.value
                # Move to the next value.
                current_val = current_val.next
            return max_value
