def pallindrome(s: str):
    reverse = s[::-1]
    if s == reverse:
        print(s, "is pallindrome")
    else:
        print(s, "is not pallindrome")


def main():
    pallindrome("121")
    print("main started")


if __name__ == "__main__":
    main()
