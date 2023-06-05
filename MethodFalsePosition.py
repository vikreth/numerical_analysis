from typing import Callable

def method_false_position(f: Callable[[float], float], p0: float, p1: float, tol: float, N: int = 100) -> float:
    i = 2
    q0 = f(p0)
    q1 = f(p1)

    while i <= N:
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        print(f"Iteration {i}: x0={p0:.16f}, x1={p1:.16f}, p_{i}={p:.16f}, f(p_{i})={f(p):.16f}")
        if abs(p - p1) < tol:
            return p
        i += 1
        q = f(p)

        if q * q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print('No root found')

if __name__ == '__main__':
    import math

    def f(x):
        return math.cos(x) - x

    root = method_false_position(f, p0=0, p1=math.pi/2, tol=1.0e-10)
    print(f"Approximate root: {root:.16f}")
