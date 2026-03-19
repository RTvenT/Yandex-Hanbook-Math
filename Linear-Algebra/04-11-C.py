import sys 
import numpy as np

from sklearn.linear_model import Ridge, Lasso


def main():
    n, d = map(int, input().split())
    X = np.array([list(map(float, input().split())) for _ in range(n)])
    y = np.array(list(map(float, input().split())))
    a_r, a_l = map(float, input().split())
    
    ridge_model = Ridge(fit_intercept=False, alpha=a_r)
    lasso_model = Lasso(fit_intercept=False, alpha=a_l)
    
    ridge_model.fit(X, y)
    lasso_model.fit(X, y)
    w_r = ridge_model.coef_.round(4)
    w_l = lasso_model.coef_.round(4)
    
    print(*w_r, sep=' ')
    print(*w_l, sep=' ')
    
    
if __name__ == '__main__':
    main()