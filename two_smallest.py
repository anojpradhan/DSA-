def two_smallest(arr):
    smallest = float("inf")
    second_smallest = float("inf")
    for num in arr:
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest and num != smallest:
            second_smallest = num
    if second_smallest == float("-inf"):
        return None
    return second_smallest, smallest


arr = [2, 8, 10, 3, 1]
print(two_smallest(arr))
