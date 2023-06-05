from collections.abc import Callable
import numpy as np
import pandas as pd


def Richardson(f:Callable[[float], float],
               x:float,
               h:float,
               n:int,
               rtol:float = 1.e-10) -> tuple[float, pd.DataFrame]:
    
    N = n + 1
    D = np.full(shape=(N, N), fill_value=np.nan, dtype=np.float64)
    D[0, 0] = (f(x + h) - f(x - h))/(2*h)
    for i in range(1, N, 1):
        h = h/2
        D[i, 0] = (f(x + h) - f(x - h))/(2*h)
        I = i + 1
        p = 1
        for j in range(1, I, 1):
            p = 4*p
            D[i, j] = D[i, j - 1] + (D[i, j - 1] - D[i - 1, j - 1])/(p - 1)
        if abs(D[i, i] - D[i - 1, i - 1]) < rtol:
            break
    d = D[i, i]
    columns = [f'O(h^{2*(k+1)})' for k in range(0, I, 1)]
    D = pd.DataFrame(data=D[:I, :I], columns=columns)
    return (d, D)

if __name__ == "__main__":
    from Richardson import Richardson, pd
    from math import exp, sin, cos, log
    pd.options.display.width = 1000
    pd.options.display.float_format = "{:.10f}".format
    def f(x): return x*exp(x)
    d, D = Richardson(f=f, x=2, h=0.2, n = 1000)
    print(f"d = {d:.10f}")
    print(D)   