"""
heapsort
binary search
"""

from random import randint

def quicksort(x,left=0,right=len(x)-1):
    def swap(i, j):
        x[i], x[j] = x[j], x[i]
    if len(x) <= 1:
        return x
    else:
        r = random.randint(0, len(x)-1)
        pivot = x[r]
        while left < right:
            while x[left] < pivot:
                left += 1
            while x[right] > pivot:
                right -= 1
            if x[left] > x[right]:
                swap(left, right)
                left += 1
                right -= 1
        swap(r,left-1)
        return quicksort(x,0,right) + quicksort(x,right,len(x)-1)

"""

def insertion_sort(x):
    """Defines inner method that swaps adjacent elements. Insertion sort is O(n^2)."""
    def swap(x, j):
        x[j-1], x[j] = x[j], x[j-1]
    for i in range(1,len(x)):
        for j in range(i,0,-1):
            if x[j-1] > x[j]:
                swap(x, j)

def insertion_sort_recursive(x, n):
    if n <= 1:
        return
    else:
        # Sort the "lower" array.
        insertion_sort_recursive(x, n-1)
        # With lower array sorted, move all values in sorted array forward until the final value can be inserted in that array.
        final_position = n-1
        j = final_position - 1
        while j >= 0 and x[j] > x[final_position]:
            x[j+1] = x[j]
            j -= 1
        x[j+1] = x[final_position]

def selection_sort(x):
    """Start at 0th element, swap it with lowest element in array. Start at 1st element, swap it with lowest element in array beyond the 1st element. And so on."""
    i = 0
    while i <= len(x)-1:
        lowest = x[i]
        min_i = i
        for j in range(i+1,len(x)-1):
            if x[j] < lowest:
                min_i = j
        x[i], x[min_i] = x[min_i], x[i]
        i += 1

def shell_sort(x):
    gap = len(x)//2
    while gap > 0:
        while j < len(x):
            i = j - gap
            j = gap
            if x[j] < x[i]:
                x[i], x[j] = x[j], x[i]
            j += 1
        gap //= 2

def shell_sort(x):
    """Generalized insertion sort. Gap > 1, but is cut in half until gap is finally 1."""
    def swap(i, j):
        x[i], x[j] = x[j], x[i]
    gap = len(x)//2
    while gap > 0:
        for j in range(gap,len(x)):
            for i in range(j-gap,-1,-gap):
                if x[i] > x[i+gap]:
                    swap(i, i+gap)
        gap //= 2

def bubble_sort(x):
    def swap(x, j):
        x[j-1], x[j] = x[j], x[j-1]
    for j in range(len(x), 2, -1):
        for i in range(1,j):
            if x[i-1] > x[i]:
                swap(x,i)

def quicksort(x):
    """This is easy because it's not an in-place sort."""
    less = []
    eq = []
    more = []
    if len(x) <= 1:
        return x
    else:
        # Better alternative: pivot = random.choice(x) chooses a random value from x.
        pivot = x[random.randint(0,len(x)-1)]
        for value in x:
            if value < pivot:
                less.append(value)
            elif value == pivot:
                eq.append(value)
            else:
                more.append(value)
        return quicksort(less) + eq + quicksort(more)

def quicksort_2(x):
    """Short and pythonic."""
    if len(x) <= 1:
        return x
    else:
        pivot = random.choice(x)
        return quicksort_2([v for v in x if v < pivot]) + [v for v in x if v == pivot] + quicksort_2([v for v in x if v > pivot])

def quicksort_inplace(array):
    """Uses helper function for recursive calls."""
    _quicksort(array, 0, len(array) - 1)
 
def _quicksort(array, start, stop):
    """If right goes to left of start or if left goes to right of stop, then no more recursive calls need be made."""
    if start < stop:
        right, left = partition(array, start, stop)
        # All elements between R and L pointers are sorted, don't need to be in recursive quicksort calls.
        _quicksort(array, start, right)
        _quicksort(array, left, stop)

def partition(array, left, right):
    """L and R pointers advance forward until out-of-order pair is found (oriented around the pivot). Swap until L > R."""
    pivot = random.choice(array)
    while left <= right:
        while array[left] < pivot:
            left += 1
        while array[right] > pivot:
            right -= 1
        if left <= right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1
    return right, left

def _merge(x):
    if len(x) == 1:
        return x
    else:
        i_middle = len(x)//2
        left_list = x[:i_middle]
        right_list = x[i_middle:]
        left_list = _merge(left_list)
        right_list = _merge(right_list)
        return merge_sort(left_list, right_list)

def merge_sort(x,y):
    """Takes sorted lists and merges them into the correct order."""
    z = []
    # While there is an element in at least one of the lists.
    while len(x) > 0 or len(y) > 0:
        if len(x) > 0 and len(y) > 0:
            if x[0] <= y[0]:
                z.append(x[0])
                x = x[1:]
            else:
                z.append(y[0])
                y = y[1:]
        elif len(x) > 0:
            z.extend(x)
            x.clear()
        else:
            z.extend(y)
            y.clear()
    return z
