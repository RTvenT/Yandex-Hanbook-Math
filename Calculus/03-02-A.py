import sys


def a(n):
    return n / (n + 1)


def main():
    n = int(input())

    print(round(a(n), 6))


if __name__ == '__main__':
    main()