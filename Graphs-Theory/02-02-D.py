import sys
from collections import deque


def adj_mat_to_adj_list(mat):
    adj_list = [[] for _ in range(len(mat))]
    for i in range(len(mat)):
        for j in range(len(mat)):
            if mat[i][j]:
                adj_list[i].append(j)

    return adj_list


def shortest_path_len(graph, start, end):
    used = [0]*len(graph)
    dist = [0]*len(graph)

    d = deque()
    d.appendleft(start)

    used[start] = 1

    while d:
        v = d.pop()

        for to in graph[v]:
            if not used[to]:
                used[to] = 1
                dist[to] = dist[v] + 1
                d.appendleft(to)

    return dist[end] if dist[end] != 0 and end != start else -1


# def show_graph(adj_mat: list):
#     import numpy as np
#     import networkx as nx
#     import matplotlib.pyplot as plt

#     adj_mat_np = np.array(adj_mat)
#     graph = nx.from_numpy_array(adj_mat_np)

#     nx.draw(graph, with_labels=True)
#     plt.show()


def main():
    N = int(input())
    adj_mat = [list(map(int, input().split())) for _ in range(N)]
    start, end = map(int, input().split())

    adj_list = adj_mat_to_adj_list(adj_mat)

    print(shortest_path_len(adj_list, start, end))
    # show_graph(adj_mat)
    


if __name__ == '__main__':
    main()
    
