import sys


def main():
    num_vertices = int(input())
    vertices = input().split()

    num_edges = int(input())
    edge_list = [input().split() for _ in range(num_edges)]

    vertex_mult = {vertex: 0 for vertex in vertices}

    for u, v in edge_list:
        vertex_mult[u] += 1
        vertex_mult[v] += 1

    if 1 in vertex_mult.values() and num_vertices - num_edges == 1:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()