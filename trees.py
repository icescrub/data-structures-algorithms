"""


2. RB/AVL trees
3. Parse Trees for NLP or polish notation
 
a=Node(1)
b=Node(2)
c=Node(3)
d=Node(4)
e=Node(5)
f=Node(6)
a.left = b
a.right = c
b.left = d
b.right = e
c.left = f


"""

from collections import deque

class Node(object):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        """This needs work. If L or R values don't exist, it doesn't work."""
        if self is None:
            return "Empty Tree()"
        else:
            return "(" + str(self.value) + ", L = " + str(self.left.value) + "..., R = " + str(self.right.value) + "..." + ")"

def min_depth(self):
    if self is None:
        return 0
    elif self.left is None and self.right is None:
        return 1
    elif self.left is None:
        return min_depth(self.right) + 1
    elif self.right is None:
        return min_depth(self.left) + 1
    else:
        return min(min_depth(self.left), min_depth(self.right)) + 1

def max_depth(self):
    if self is None:
        return 0
    elif self.left is None and self.right is None:
        return 1
    elif self.left is None:
        return max_depth(self.right) + 1
    elif self.right is None:
        return max_depth(self.left) + 1
    else:
        return max(max_depth(self.left), max_depth(self.right)) + 1

def merge(t1, t2):
    if t1 is None:
        return t2
    elif t2 is None:
        return t1
    else:
        t1.value += t2.value
        t1.left = merge(t1.left, t2.left)
        t1.right = merge(t1.right, t2.right)

def length(self):
    """
    Number of nodes.

    Can't implement __len__, possibly because iter isn't implemented?
    """
    if self is None:
        return 0
    elif self.left is None and self.right is None:
        return 1
    elif self.left is None:
        return length(self.right) + 1
    elif self.right is None:
        return length(self.left) + 1
    else:
        return length(self.left) + length(self.right) + 1

def traverse_in(self):
    """The in/pre/post-order traversals are variants of DFS."""

    stack = []
    traversal = []
    current = self
    done = False
    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                traversal.append(current.value)
                current = current.right
            else:
                done = True
    return traversal

def traverse_pre(self):
    """The in/pre/post-order traversals are variants of DFS."""
    stack = []
    traversal = []
    current = self
    done = False
    while not done:
        if current:
            stack.append(current)
            traversal.append(current.value)
            current = current.left
        else:
            if len(stack) > 0:
                current = stack.pop()
                current = current.right
            else:
                done = True
    return traversal

def traverse_post(self):
    """
    The in/pre/post-order traversals are variants of DFS.

    This one uses two stacks, so it is significantly different than the other two.
    """

    if self is None:
        return

    s1 = []
    s2 = []
    traversal = []

    s1.append(self)

    while s1:
        current = s1.pop()
        s2.append(current.value)

        if current.left:
            s1.append(current.left)
        if current.right:
            s1.append(current.right)

    while s2:
        traversal.append(s2.pop())
    
    return traversal

def traverse_level(self):
    """This is BFS. Uses a queue."""

    traversal = []
    queue = deque()
    queue.appendleft(self)

    while queue:
        current = queue.pop()
        traversal.append(current.value)

        if current.left:
            queue.appendleft(current.left)
        if current.right:
            queue.appendleft(current.right)

    return traversal

def in_order(self):
    if self:
        in_order(self.left)
        print(self.value)
        in_order(self.right)

def pre_order(self):
    if self:
        print(self.value)
        pre_order(self.left)
        pre_order(self.right)

def post_order(self):
    if self:
        post_order(self.left)
        post_order(self.right)
        print(self.value)

def last(self):
    last = self.value
    current = self
    while current:
        last = current.value
        current = current.right
    return last

def count(self, value):
    if self is None:
        return 0
    else:
        if self.value == value:
            return count(self.left, value) + count(self.right, value) + 1
        else:
            return count(self.left, value) + count(self.right, value)

def invert(self):
    if self:
        self.left, self.right = self.right, self.left
        invert(self.left)
        invert(self.right)
