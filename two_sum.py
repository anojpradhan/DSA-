def two_sum(s, target):
    for idx, num in enumerate(s):
        for idx2, num2 in enumerate(s):
            if (num + num2 == target) and (idx != idx2):
                print(idx, idx2)
                return
            
def main():
    two_sum([3, 4, 2], 6)


if __name__ == "__main__":
    main()
