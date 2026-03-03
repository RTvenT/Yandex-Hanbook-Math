import sys


def main():
    N = int(input())
    adj_mat = [list(map(int, input().split())) for _ in range(N)]

    leaves = []

    for i in range(N):
        if sum(adj_mat[i]) == 1: leaves.append(i)

    if leaves:
        print(*leaves, sep='\n')
    else:
        print('NO LEAVES')


if __name__ == '__main__':
    main()