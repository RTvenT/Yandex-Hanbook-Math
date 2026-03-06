import sys
import numpy as np


def grad(sample, y_true, w, lam, alpha):
    return sample.T @ (sample @ w - y_true) + lam * w + alpha * np.cos(w)


def L(sample, y_true, w, lam, alpha):
    return 0.5 * np.sum((sample @ w - y_true) ** 2) + 0.5 * lam * np.sum(w ** 2) + alpha * np.sum(np.sin(w))


def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)

    m = int(next(it))
    n = int(next(it))

    sample = np.array([[float(next(it)) for _ in range(n)] for _ in range(m)])
    y_true = np.array([float(next(it)) for _ in range(m)])
    w = np.array([float(next(it)) for _ in range(n)])

    lam = float(next(it))
    alpha = float(next(it))
    h = float(next(it))

    true_grad = grad(sample, y_true, w, lam, alpha)

    num_grad = np.zeros(n)

    for j in range(n):
        w_plus = w.copy()
        w_minus = w.copy()

        w_plus[j] += h
        w_minus[j] -= h

        f_plus = L(sample, y_true, w_plus, lam, alpha)
        f_minus = L(sample, y_true, w_minus, lam, alpha)

        num_grad[j] = (f_plus - f_minus) / (2 * h)

    divergence = np.max(np.abs(true_grad - num_grad))

    print(f"{divergence:.6f}")
    


if __name__ == "__main__":
    main()