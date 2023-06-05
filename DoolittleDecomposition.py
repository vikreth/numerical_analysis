import numpy as np

def DoolitleDecomposition(a: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    n = a.shape[0]
    l = np.eye(n)
    u = a.copy()
    stop = n - 1
    for k in range(0, stop, 1):
        start = k + 1
        for i in range(start, n, 1):
            r = u[i, k] / u[k, k]
            l[i, k] = r
            u[i, k] = 0
            for j in range(start, n, 1):
                u[i, j] = u[i, j] - r*u[k, j]
    return (l, u)


if __name__ == '__main__':
    a = np.array([
        [2,0,0,0],
        [-1,3,0,0],
        [-2,2,-3,0],
        [1,-2,2,4]
    ], dtype=np.float64)
    l,u = DoolitleDecomposition(a)
    
print(f'l = {l}')
print(f'u = {u}')
print(f'a = {np.matmul(l,u)}')