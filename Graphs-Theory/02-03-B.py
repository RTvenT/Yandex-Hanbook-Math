import sys


def main():
    users = input().split()
    movies = input().split()
    
    g = [input().split()[1:] for _ in range(len(users))]

    is_comp_bipartite = True

    for m in g:
        user_n_movies = int(m[0])
        user_movies = m[1:]
        if user_n_movies == len(movies) and user_movies == movies:
            continue
        else:
            is_comp_bipartite = False
            break
            
    if is_comp_bipartite:
        print('YES')
    else:
        print('NO')

        
    

if __name__ == '__main__':
    main()