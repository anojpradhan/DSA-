def second_largest_with_sort(s):
    s.sort()
    print("Second largest element in", s, "is", s[-2])


def second_largest_without_sort(s):
    first = max(s)
    second = max([i for i in s if i != first])
    print(second)


def main():
    second_largest_with_sort([1, 2, 3, 4, 10, 0, 9, 2, 8, 12, 35, 46])
    second_largest_without_sort([2, 2, 2, -2])
    print("thsi is a main")


if __name__ == "__main__":
    main()
