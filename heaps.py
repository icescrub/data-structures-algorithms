"""
Note 1: decrease_key can be implemented by just...changing the value of the element, then heapifying again. Need to know the index, as though you know the location of an object. This is like a priority queue.
"""

def heapify(x, min=True):
    """
    This assumes a MIN-heap structure, but is easily converted to MAX-heap. Gives a list the additional heap structures.

    This is the in-place, O(n) version of heapify.

    The O(nlogn) version inserts values from a list into another list and bubbles up to maintain heap structure.
    """
    if min is False:
        x[:] = [-v for v in x]
    for i in range(len(x)//2, -1, -1):
        bubble_down(x, i)
    if min is False:
        x[:] = [-v for v in x]

def insert(heap, value):
    """Always need an insert operation."""
    heap.append(value)
    bubble_up(heap)

def remove(heap, value):
    """Tried to be tricky with swaps, but it wasn't worth it. Just remove value and heapify."""
    heap.remove(value)
    heapify(heap)

def bubble_up(heap, i=-1):
    """Makes smaller elements bubble up to the top."""
    if i == -1:
        i_child = len(heap)-1
    else:
        i_child = i
    violated = True
    while violated:
        i_parent = (i_child-1)//2
        if heap[i_child] < heap[i_parent]:
            heap[i_child], heap[i_parent] = heap[i_parent], heap[i_child]
            i_child = i_parent
            if i_child == 0:
                violated = False
        else:
            violated = False

def pop(heap):
    heap[0], heap[len(heap)-1] = heap[len(heap)-1], heap[0]
    min = heap.pop()
    bubble_down(heap)
    return min

def bubble_down(heap, i=0, length=-1):
    """Makes larger elements bubble down to the bottom."""
    if length == -1:
        length = len(heap)
    i_parent = i
    while has_left_child(heap, i_parent, length):
        i_min = min_child(heap, i_parent, length)
        if heap[i_parent] > heap[i_min]:
            heap[i_parent], heap[i_min] = heap[i_min], heap[i_parent]
            i_parent = i_min
        else:
            break

def min_child(heap, i, length):
    i_left = 2*i + 1
    i_right = 2*i + 2
    i_min = i_left
    if has_right_child(heap, i, length) and heap[i_right] < heap[i_left]:
        i_min = i_right
    return i_min

def has_left_child(heap, i, length):
    if 2*i+1 < length:
        return True
    else:
        return False

def has_right_child(heap, i, length):
    if 2*i + 2 < length:
        return True
    else:
        return False

def heapsort(x):
    """Easy to understand, but not in-place."""
    x_sorted = []
    heapify(x)
    while x:
        x_sorted.append(pop(x))
    x[:] = x_sorted
    return x

def heapsort_2(x):
    """In-place algorithm for heapsort."""
    x[:] = [-v for v in x]
    heapify(x)
    for i in range(len(x)-1, 0, -1):
        x[0], x[i] = x[i], x[0]
        bubble_down(x, length=i-1)
    return [-v for v in x]

def k_smallest(heap, k):
    """We assume we don't want to mutate the heap. This is dependent on implementation."""
    h = heap.copy()
    return heapsort(h)[:k]

def k_largest(heap, k):
    """
    We assume we don't want to mutate the heap. This is dependent on implementation.

    This would be done differently if we had a MAX-heap.
    """
    h = heap.copy()
    return heapsort(h)[len(heap)-k:]

def max_value(heap):
    """Since half of all values occur in the last "row" of the heap. Splits time by a factor of 2."""
    return max(heap[len(heap)//2:])

def multi_heap(*lists):
    """List of heaps."""
    heaps = []
    for heap in lists:
        heapify(heap)
        heaps.append(heap)
    return heaps

def multi_pop(multi):
    """Filters for non-empty heaps. Compares minimum values and pops minimum off the relevant heap."""
    valid_multi = filter(lambda x: len(x) > 0, multi)
    min_heap = min(valid_multi, key=lambda x: x[0])
    return pop(min_heap)

def multi_heapsort(multi):
    """Takes a multi-heap and sorts values."""
    list = []
    while any(multi):
        list.append(multi_pop(multi))
    return list
