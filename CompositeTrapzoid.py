from collections.abc import Callable

def CompositeTrapzoid(f: Callable[[float], float], a: float, b: float, n: int) -> float:
    h = (b - a)/n
    f0 = f(a) - f(b)
    fi = 0
    x = a
    for _ in range(1, n, 1):
        x = x + h
        fi = fi + f(x)
    A = h * (0.5 * f0 + fi)
    return A

if __name__ == '__main__':
    from math import exp
    def f(x): return exp(x) 
    I = CompositeTrapzoid(f=f, a=0, b=1, n = 1000)
    print(f'the integral = {I:.10f}')