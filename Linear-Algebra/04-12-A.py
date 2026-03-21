import sys 

import numpy as np
from sklearn.svm import SVC


def main():
    n, d, c = map(float, input().split())
    X_train = np.array([list(map(float, input().split())) for _ in range(int(n))])
    y_train = np.array(list(map(int, input().split())))
    t = int(input())
    X_test = np.array([list(map(float, input().split())) for _ in range(t)])
    
    model = SVC(kernel='linear', C=c)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    
    print(*y_pred, sep=' ')
    
    
if __name__ == '__main__':
    main()