import sys


def adj_list_to_adj_mat(adj_list, nodes_num):
    adj_mat = [[0]*nodes_num for _ in range(nodes_num)]
    
    for i in range(nodes_num):
        for j in adj_list[i]:
            adj_mat[i][j] = 1

    return adj_mat


def main():
    N = int(input())
    adj_list = [list(map(int, input().split())) for _ in range(N)]
    adj_mat = adj_list_to_adj_mat(adj_list, N)

    for s in adj_mat:
        print(*s)


if __name__ == '__main__':
    main()