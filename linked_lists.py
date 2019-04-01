class Node(object):
    """Node for a singly linked list."""
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList(object):
    """
    Singly linked list. Can be treated as a stack or a queue, depending on functions used.

    Stacks are implemented with a single head pointer. Stacks are not sequences, so indexing and slicing are not valid functions.
    """

    def __init__(self, values=None, head=None):
        """LL inserts values like a queue. LL([1,2,3]) = 1 --> 2 --> 3."""
        self.head = head
        if values:
            for value in values:
                self.insert_end(value)

    def __iter__(self):
        """
        Makes LL iterable and a generator.

        Now accepts functions: any, all, zip, filter, enumerate, membership, list, tuple, dict, sorted, and more.
        """
        current = self.head
        while current:
            yield current.value
            current = current.next

    def __repr__(self):
        """Returns string as a visual representation of an LL, as I visualize it."""
        if self.head is None:
            return "Empty LinkedList()"
        else:
            return " --> ".join(str(value) for value in self)

    def __len__(self):
        """Returns integer length of the LL."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __add__(self, other):
        """
        Returns concatenated LL's. Pure function.

        This is identical to how x + y returns concatenated lists, if x and y are lists. This auto-implements __iadd__.
        """
        if self.head is None and other.head is None:
            return LinkedList()
        elif self.head is None:
            return other
        elif other.head is None:
            return self
        else:
            temp_self = self.copy()
            temp_other = other.copy()
            current = temp_self.head
            while current.next:
                current = current.next
            current.next = temp_other.head
            return temp_self

    def __gt__(self, other):
        """
        Returns boolean. LL with first greater element position-wise is greater. If all elements are identical, tie is broken by LL with greater length. By defining >, >=, and == functions, Python implements <, <=, and != for free.
        """
        l1_temp, l2_temp = self.copy(), other.copy()
        while l1_temp.head:
            if l2_temp.head is None or l1_temp.head.value > l2_temp.head.value:
                return True
            elif l1_temp.head.value < l2_temp.head.value:
                return False
            else:
                l1_temp.head = l1_temp.head.next
                l2_temp.head = l2_temp.head.next
        return False

    def __eq__(self, other):
        """
        Returns boolean. True if all position-wise elements are equal and the lengths of the LL's are equal.

        By defining >, >=, and == functions, Python implements <, <=, and != for free.
        """
        l1_temp, l2_temp = self.copy(), other.copy()
        while l1_temp.head:
            if l2_temp.head is not None and l1_temp.head.value == l2_temp.head.value:
                l1_temp.head = l1_temp.head.next
                l2_temp.head = l2_temp.head.next
            else:
                return False
        if l2_temp.head is not None:
            return False
        else:
            return True

    def __ge__(self, other):
        """Returns boolean. Uses > and = functions. By defining >, >=, and == functions, Python implements <, <=, and != for free."""
        return self == other or self > other

    def __lt__(self, other):
        """Since >, >= and == are defined, this function is not necessary."""
        return not self >= other

    def __le__(self, other):
        """Since >, >= and == are defined, this function is not necessary."""
        return not self > other

    def __ne__(self, other):
        """Since >, >= and == are defined, this function is not necessary."""
        return not self == other

    def __reversed__(self):
        """
        Returns sorted LL. Sorted is automatically implemented in Python, but Reversed is not.

        Debated whether this should return a list or LL. Most sequences return a list or nothing at all, so this returns a list.
        """
        return reversed(list(self))

    def traverse(self):
        """ Good proof of concept, but __iter__ takes care of this."""
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self,value):
        """Good proof of concept, but __iter__ takes care of this."""
        current = self.head
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                current = current.next
        if current is None:
            raise ValueError('Value not found in list.')
        return current

    def len_recursive(self):
        """Recursive length function. The other one is better."""
        if self.head.next is None:
            return 1
        else:
            self.head = self.head.next
            return 1 + len_rec(self)

    def reverse(self):
        """No return value. Reverses LL in-place. Directions of arrows reverse."""
        previous = None
        current = self.head
        while current:
            after = current.next
            current.next = previous
            previous = current
            current = after
        self.head = previous

    def reverse_alternate(self):
        """Additive reverse. Each node becomes the head, briefly, before following node becomes the head, and so on."""
        current = self.head
        after = self.head.next
        while after:
            current.next = after.next
            after.next = self.head
            self.head = after
            after = current.next

    def copy(self):
        """Returns copy of the LL."""
        newLL = LinkedList()
        current = self.head
        while current:
            newLL.insert_end(current.value)
            current = current.next
        return newLL

    def count(self, value):
        """Returns integer equal to number of times that value appears in the LL."""
        count = 0
        current = self.head
        while current:
            if current.value == value:
                count += 1
            current = current.next
        return count

    def extend(self, other):
        """
        No return value. In-place concatenation of one LL with another.
  
        Since __iadd__ was implemented, can just be L += L2.

        If extending with list, cast list to LL constructor.
        """
        if self.head is None:
            for value in other:
                self.insert_end(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head

    def insert(self, value):
        """No return value. Pushes new node onto LL as though LL is a stack."""
        node = Node(value, self.head)
        self.head = node

    def insert_end(self, value):
        """No return value. Inserts new node onto LL as though LL is a queue."""
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(value)

    def insert_after(self, old_value, new_value):
        """No return value. Inserts new value after given value of LL."""
        current = self.head
        while current.value != old_value:
            current = current.next
        node = Node(new_value)
        node.next = current.next
        current.next = node

    def insert_before(self, old_value, new_value):
        """No return value. Inserts new value before given value of LL."""
        if self.head.value == old_value:
            node = Node(new_value)
            node.next = self.head
            self.head = node
        else:
            current = self.head
            while current.next.value != old_value:
                current = current.next
            node = Node(new_value)
            node.next = current.next
            current.next = node

    def remove(self, value):
        """No return value. Removes value if it appears in the LL."""
        current = self.head
        previous = None
        found = False
        while current and not found:
            if current.value == value:
                found = True
            else:
                previous = current
                current = current.next
        if current is None:
            raise ValueError("Value not found in list.")
        elif previous is None:
            self.head = current.next
        else:
            previous.next = current.next

    def remove_duplicates(self, value):
        """No return value. Removes all duplicates of value in the LL."""
        current = self.head
        previous = None
        values_seen = set()
        while current:
            if current.value in values_seen:
                previous.next = current.next
                current = current.next
            else:
                values_seen.add(current.value)
                previous = current
                current = current.next

    def clear(self):
        """No return value. Removes all nodes from LL. Can be called 'remove all'."""
        while self.head:
            self.remove(self.head.value)

    def sorted_intersect(self, other):
        """ASSUMES sorted LL's. Sorts and identifies all elements that both LL's share."""
        s = set()
        p = self.sort().head
        q = other.sort().head
        while p:
            if p.value < q.value:
                p = p.next
            elif q.value < p.value:
                q = q.next
            else:
                s.add(p.value)
                p = p.next
                q = q.next
        return list(s)

    def merge(self, other):
        """
        Returns LL. For each position, values of the nodes are added together and a new node is created in a new LL.

        ESSENTIAL for other languages. Since Python has zip() and LL's are iterable, this function is not essential.
        """
        if len(self) >= len(other):
            l_max, l_min = self.copy(), other.copy()
        else:
            l_max, l_min = other.copy(), self.copy()
        current_max = l_max.head
        current_min = l_min.head
        while current_min:
            current_max.value += current_min.value
            current_max = current_max.next
            current_min = current_min.next
        return l_max

    def find_kth(self, k):
        """
        Returns kth node in the LL, if it appears. Useful for doubly/circularly linked lists.
        """
        current = self.head
        if k > len(self) - 1:
            raise IndexError("kth value does not exist.")
        for i in range(k):
            current = current.next
        return current.value

    def sort(self):
        """No return value. Interface for merge_sort()."""
        self.sorted_merge()

    def sorted_merge(self):
        """The recursive, splitting section of mergeSort."""
        if len(self) == 1:
            return self
        else:
            L,R = self.split()
            sL = L.sorted_merge()
            sR = R.sorted_merge()
            return sL.merge_sort(sR)

    def split(self):
        """Note: if a singleton is given, the left LL is None. Only the right LL has the value."""
        current= self.head
        left, right = [], []
        for i in range(len(self)):
            if i < len(self)//2:
                left.append(current.value)
                current = current.next
            else:
                right.append(current.value)
                current = current.next
        return LinkedList(left), LinkedList(right)

    def merge_sort(self, other):
        """This ASSUMES two sorted LL's. How to achieve a sorted LL? Split LL and use sorted_merge."""
        p = self.head
        q = other.head
        list_vals = []
        while p:
            if q:
                if p.value <= q.value:
                    list_vals.append(p.value)
                    p = p.next
                else:
                    list_vals.append(q.value)
                    q = q.next
            else:
                list_vals.append(p.value)
                p = p.next
        while q:
            list_vals.append(q.value)
            q = q.next
        return LinkedList(list_vals)

    def bubble_sort(self):
        """Not really bubblesort, either. Just some kind of sort."""
        ordered = False
        current = self.head
        while not ordered:
            ordered = True
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                    ordered = False
                current = current.next
            current = self.head

    def another_sort(self):
        """Returns sorted LL. Builds up new LL by inserting each value in order."""
        tempLL = LinkedList()
        for value in self:
            if tempLL.head is None:
                tempLL.insert_end(value)
            else:
                current = tempLL.head
                found = False
                while current and not found:
                    if value > current.value:
                        current = current.next
                    else:
                        found = True
                if current is None:
                    tempLL.insert_end(value)
                else:
                    tempLL.insert_before(current.value, value)
        self.clear()
        self.extend(tempLL)
