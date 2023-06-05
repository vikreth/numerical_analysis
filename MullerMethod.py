from typing import Callable

def method_muller(f: Callable[[float], float], x0: float, x1: float, x2: float, tol: float, N: int = 100) -> float:
    i = 2
    h1 = x1 - x0
    h2 = x2 - x1
    d1 = (f(x1) - f(x0)) / h1
    d2 = (f(x2) - f(x1)) / h2
    d = (d2 - d1) / (h2 + h1)
    
    while i <= N:
        b = d2 + h2 * d
        D = (b**2 - 4*f(x2)*d)**0.5
        
        if abs(b-D) < abs(b+D):
            E = b + D
        else:
            E = b - D
            
        h = -2*f(x2)/E
        p = x2 + h
        
        print(f"Iteration {i}: x0={x0:.10f}, x1={x1:.10f}, x2={x2:.10f}, p_{i}={p:.10f}, f(p_{i})={f(p):.10f}")
        
        if abs(h) < tol:
            return p
        
        x0 = x1
        x1 = x2
        x2 = p
        
        h1 = x1 - x0
        h2 = x2 - x1
        d1 = (f(x1) - f(x0)) / h1
        d2 = (f(x2) - f(x1)) / h2
        d = (d2 - d1) / (h2 + h1)
        
        i += 1
        
    print('No root found')

import math

def main():
    def f(x):
        return x**4 - 3*x**3 + x**2 + x + 1

    x0, x1, x2 = -0.5, 0, 0.5
    tol = 1e-10

    root = method_muller(f, x0, x1, x2, tol)

    print(f"Approximate root: {root:.10f}")

if __name__ == '__main__':
    main()
