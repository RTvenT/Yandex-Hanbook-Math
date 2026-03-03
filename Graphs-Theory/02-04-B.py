import sys
from collections import deque


def adj_mat_to_adj_list(mat):
    adj_list = [[] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                adj_list[i].append(j)

    return adj_list


def shortest_path(G, N, start, end):
    used = [0]*N
    dist = [0]*N
    prev = [-1]*N

    d = deque()
    d.appendleft(start)

    used[start] = 1

    while d:
        v = d.pop()

        for to in G[v]:
            if not used[to]:
                used[to] = 1
                dist[to] = dist[v] + 1
                d.appendleft(to)
                prev[to] = v

    v = end
    path = []
    while prev[v] != -1:
        path.append(v)
        v = prev[v]

    path.append(start)
    
    return path[::-1]


def main():
    N = int(input())
    adj_mat = [list(map(int, input().split())) for _ in range(N)]
    R, V = map(int, input().split())

    adj_list = adj_mat_to_adj_list(adj_mat)
    path = shortest_path(adj_list, N, R, V)

    if len(path) == 1:
        print('NO PATH')
    else:
        print(*path, sep=' ')


if __name__ == '__main__':
    main()