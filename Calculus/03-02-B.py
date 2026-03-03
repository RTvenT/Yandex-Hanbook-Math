import sys


def iscontinuous(f, x0, delta, eps):
   
   left_lim = abs(f(x0 - delta) - f(x0)) < eps
   right_lim = abs(f(x0 + delta) - f(x0)) < eps

   return left_lim and right_lim


def main():
    K = 5
    func = input()
    f = lambda x: eval(func, {"x": x})
    x0 = float(input())
    delta = float(input())
    eps = K * delta

    if iscontinuous(f, x0, delta, eps):
        print("CONTINUOUS")
    else:
        print("DISCONTINUOUS")


if __name__ == '__main__':
    main()