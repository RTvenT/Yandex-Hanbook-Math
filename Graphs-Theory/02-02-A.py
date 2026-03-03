import sys


def get_nodes_with_loops(adj_mat):
    nodes_with_loops = []

    for n in range(len(adj_mat)):
        if adj_mat[n][n]:
            nodes_with_loops.append(n)

    return nodes_with_loops
    

def main():
    adj_mat = [list(map(int, row.split())) for row in sys.stdin]
    
    nodes_with_loops = get_nodes_with_loops(adj_mat)

    if nodes_with_loops:
        print(*nodes_with_loops, sep='\n')
    else:
        print("NO LOOPS")


if __name__ == '__main__':
    main()
