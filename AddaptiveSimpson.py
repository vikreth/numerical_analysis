from collections.abc import Callable

def AddaptiveSimpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol_factor: int = 10,
    tol: float = 1.0e-10) -> float:
    h = 0.5 * (b - a)
    x0 = a
    x1 = a + 0.5 * h
    x2 = a + h
    x3 = a + 1.5 * h
    x4 = b
    f0 = f(x0)
    f1 = f(x1)
    f2 = f(x2)
    f3 = f(x3)
    f4 = f(x4)
    s1 = h * (f0 + 4 * f2 + f4)/3
    s2 = h * (f0 + 4 * f1 + 2 * f2 + 4 * f3 + f4)/6
    if abs(s2 - s1)>= tol_factor * tol:
        s = AddaptiveSimpson(f=f, a=x0, b=x2, tol=0.5*tol) + AddaptiveSimpson(f=f, a=x2, b=x4, tol=0.5*tol)
    else:
        s = s2 + (s2 - s1)/15
    return s

if __name__ == '__main__':
    from math import exp 
    def f(x): return exp(x)
    
    s = AddaptiveSimpson(f=f, a=0, b=1, tol=1.e-10)
    print(f's = {s:.10f}')