def max_subarray(arr):
    current_sum = arr[0]
    maximum = arr[0]

    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        maximum = max(maximum, current_sum)
    return maximum


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
