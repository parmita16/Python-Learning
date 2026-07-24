# =====================================================================
# ALL SORTING METHODS - built from scratch, no sorted()/.sort()
# Useful beyond "basic sorting" - if a Medium/Hard question needs
# sorting as a sub-step (like the greedy activity question), you can
# drop in whichever one fits the size/shape of the data.
# =====================================================================

# ---------------------------------------------------------------------
# 1. BUBBLE SORT
# Idea: repeatedly swap adjacent elements if they're in the wrong order.
# Time: O(n^2) worst/average, O(n) best (already sorted, with early exit)
# Space: O(1)
# Stable: Yes (equal elements keep their relative order)
# When to use: teaching/small n only - it's the slowest in practice
# ---------------------------------------------------------------------
def bubble_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


# ---------------------------------------------------------------------
# 2. SELECTION SORT
# Idea: find the smallest remaining element, put it at the front,
# repeat for the rest of the list.
# Time: O(n^2) always (even if already sorted - it still scans)
# Space: O(1)
# Stable: No (can swap equal elements out of original order)
# When to use: when swaps are expensive but comparisons are cheap
# (it does the minimum possible number of swaps: n-1)
# ---------------------------------------------------------------------
def selection_sort(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        smallest_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


# ---------------------------------------------------------------------
# 3. INSERTION SORT
# Idea: build up a sorted section at the front one element at a time,
# inserting each new element into its correct spot (like sorting cards
# in your hand).
# Time: O(n^2) worst/average, O(n) best (nearly-sorted data)
# Space: O(1)
# Stable: Yes
# When to use: small arrays, or data that's already "almost sorted"
# (it's the fastest of the simple sorts in that case)
# ---------------------------------------------------------------------
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # shift everything bigger than key one step to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# ---------------------------------------------------------------------
# 4. MERGE SORT
# Idea: split the array in half recursively until pieces have 1
# element, then merge sorted halves back together.
# Time: O(n log n) always - this is the big advantage over the above
# Space: O(n) - needs extra arrays to merge into
# Stable: Yes
# When to use: large datasets, when you need guaranteed O(n log n)
# and stability, and extra memory is not a concern
# ---------------------------------------------------------------------
def merge_sort(arr):
    if len(arr) <= 1:
        return arr.copy()

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return _merge(left_half, right_half)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:   # <= keeps it stable
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    # add any leftovers
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result


# ---------------------------------------------------------------------
# 5. QUICK SORT
# Idea: pick a "pivot", partition the array into elements smaller and
# bigger than the pivot, recursively sort each side.
# Time: O(n log n) average, O(n^2) worst case (rare, bad pivot choices)
# Space: O(log n) for the recursion stack (in-place partitioning)
# Stable: No
# When to use: general-purpose default in practice - usually the
# fastest in real-world average cases despite the worst-case risk
# ---------------------------------------------------------------------
def quick_sort(arr):
    arr = arr.copy()
    _quick_sort_helper(arr, 0, len(arr) - 1)
    return arr

def _quick_sort_helper(arr, low, high):
    if low < high:
        pivot_index = _partition(arr, low, high)
        _quick_sort_helper(arr, low, pivot_index - 1)
        _quick_sort_helper(arr, pivot_index + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]  # choosing the last element as pivot
    i = low - 1        # boundary of "smaller than pivot" section
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ---------------------------------------------------------------------
# 6. COUNTING SORT
# Idea: count how many times each value appears, then rebuild the
# array in order from the counts. Only works for integers in a known,
# reasonably small range (not comparison-based at all).
# Time: O(n + k) where k is the range of values (e.g. 0 to 100)
# Space: O(k)
# Stable: Yes (if built carefully, as done here)
# When to use: when values are integers in a small known range - e.g.
# exam scores 0-100, ages, small IDs - it beats every comparison sort
# ---------------------------------------------------------------------
def counting_sort(arr, max_value=None):
    if len(arr) == 0:
        return []
    if max_value is None:
        max_value = arr[0]
        for num in arr:
            if num > max_value:
                max_value = num

    counts = [0] * (max_value + 1)
    for num in arr:
        counts[num] += 1

    # turn counts into cumulative counts (tells us final positions)
    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    result = [0] * len(arr)
    # walk the original array backwards to keep it stable
    for i in range(len(arr) - 1, -1, -1):
        num = arr[i]
        counts[num] -= 1
        result[counts[num]] = num

    return result


# ---------------------------------------------------------------------
# QUICK REFERENCE TABLE (as comments)
# ---------------------------------------------------------------------
# Algorithm       | Best      | Average   | Worst     | Space   | Stable
# ----------------|-----------|-----------|-----------|---------|-------
# Bubble Sort     | O(n)      | O(n^2)    | O(n^2)    | O(1)    | Yes
# Selection Sort  | O(n^2)    | O(n^2)    | O(n^2)    | O(1)    | No
# Insertion Sort  | O(n)      | O(n^2)    | O(n^2)    | O(1)    | Yes
# Merge Sort      | O(n log n)| O(n log n)| O(n log n)| O(n)    | Yes
# Quick Sort      | O(n log n)| O(n log n)| O(n^2)    | O(log n)| No
# Counting Sort   | O(n+k)    | O(n+k)    | O(n+k)    | O(k)    | Yes


# ---------------------------------------------------------------------
# TEST ALL OF THEM ON THE SAME INPUT
# ---------------------------------------------------------------------
if __name__ == "__main__":
    test_data = [64, 25, 12, 22, 11, 90, 5]

    print("Original:      ", test_data)
    print("Bubble sort:   ", bubble_sort(test_data))
    print("Selection sort:", selection_sort(test_data))
    print("Insertion sort:", insertion_sort(test_data))
    print("Merge sort:    ", merge_sort(test_data))
    print("Quick sort:    ", quick_sort(test_data))
    print("Counting sort: ", counting_sort(test_data))
