import sys


def adj_mat_to_adj_list(mat):
    adj_list = [[] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                adj_list[i].append(j)

    return adj_list


def main():
    adj_mat = [list(map(int, s.split())) for s in sys.stdin]
    adj_list = adj_mat_to_adj_list(adj_mat)
    
    for s in adj_list:
        print(*s)


if __name__ == '__main__':
    main()