import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree.
    def insert(self, value):
        # Start at the root node which is represented by self.value.
        # Check if the value is less than the current node.
        if value < self.value:
            # See if there is a value on the left.
                # If there is not a value on the left...
                if self.left is None:
                # Create a new node in that position.
                    self.left = BinarySearchTree(value)
                else:
                    # We need to repeat. Best way to do this is recursion.
                    self.left.insert(value)
        else:
            # Repeat the same logic as above except for the right side.
            # If it's not less than we know the value is greater.
                if self.right is None:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    # Return True if the tree contains the value, and
    # False if it does not.
    def contains(self, target):
        # If the target is equal to the root node, return True.
        if target == self.value:
            return True
        # If the target is smaller, go left.
        elif target < self.value:
            # If there is no value to the left.
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree.
    def get_max(self):
        """The value that is the furthest right will be the max value."""
        # If we can't go right, we're at the max value.
        if self.right is None:
            return self.value
        # If we can go right, go right until we can't go right anymore.
        else:
            max_val = self.right.get_max()
            return max_val

        # Iterative approach
        # max_val = self.value
        # current_tree_root = self
        # while current_tree_root.right:
        #   current_tree_root = current_tree_root.right
        # return current_tree_root.value        

    # Call the function `cb` on the value of each node.
    # You may use a recursive or iterative approach.
    def for_each(self, cb):
        # Call cb on self.value.
        cb(self.value)
        # If there are nodes on the left or right, recurse.
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

        # Iterative approach

        # stack = Stack()
        # stack.push(self)
        # So long as there is something in the stack...
        # while stack.length > 0:
        #   current_node = stack.pop()
        #   if current_node.right:
        #       stack.push(current_node.right)
        #   if current_node.left:
        #       stack.push(current_node.left)
        #   cb(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
