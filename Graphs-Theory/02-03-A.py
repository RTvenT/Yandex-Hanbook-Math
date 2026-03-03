import sys


def main():
    N = int(input())

    edges_num = N * (N-1) / 2

    print(int(edges_num))


if __name__ == '__main__':
    main()