def two_largest(arr):
    largest = float("-inf")
    second_largest = float("-inf")

    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    if second_largest == float("-inf"):
        return None
    return largest, second_largest


arr = [10, 5, 20, 8, 2, 15]
print(two_largest(arr))
