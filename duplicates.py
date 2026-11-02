def duplicates(arr):
    checked = set()
    duplicates = set()

    for num in arr:
        if num in checked:
            duplicates.add(num)
        else:
            checked.add(num)
    return list(checked)


arr = [1, 1, 2, 3, 5, 9, 2, 1, 7]
print(duplicates(arr))
