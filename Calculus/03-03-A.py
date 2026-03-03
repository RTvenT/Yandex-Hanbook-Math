import sys


def find_critical_points(coefs, p, q):
    a, b, c = coefs
    d = b**2 - 4 * a * c
    in_interval = lambda x: p <= x <= q
    critical_points = [] 

    if a == 0 and b != 0: 
        x = -c/b
        if in_interval(x):
            critical_points.append(x)
    elif d == 0 and a != 0:
        x = (-b)/(2*a)
        if in_interval(x):
            critical_points.append(x)
    elif d > 0:
        critical_points = list(filter(in_interval, [(-b + d**0.5)/(2*a), (-b - d**0.5)/(2*a)]))
    
    return critical_points


def point_type(second_deriv, x):
    if second_deriv(x) > 0:
        return 'Local minimum'
    elif second_deriv(x) < 0:
        return 'Local maximum'
    else:
        return 'Saddle point'


def main():
    a, b, c, d = map(float, input().split())

    f = lambda x: a * x**3 + b * x**2 + c * x + d
    f_d_1_coefs = [3*a, 2*b, c]
    f_d_2 = lambda x: 6 * a * x + 2 * b

    p, q = map(float, input().split())

    critical_points = find_critical_points(f_d_1_coefs, p, q)

    if not critical_points: 
        print('No critical points found.')
        return
    
    critical_points.sort()
    
    for x in critical_points:
        print(
            f'{point_type(f_d_2, x)} at x = {round(x, 5)}',
            f'f(x) = {f(x)}',
            sep='\n'
        )
    

if __name__ == '__main__':
    main()
