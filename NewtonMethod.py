def newton_raphson(f, df, po, tol, max_iter):
    i = 1
    while i <= max_iter:
        p = po - f(po) / df(po)
        if abs(p - po) < tol:
            return p
        i += 1
        po = p
        print(f'iteration = {i-1} p = {p}')
    print('The method failed after', max_iter, 'iterations')

if __name__ == '__main__':
    from math import cos, sin
    # Define the function and its derivative
    f = lambda x:  cos(x) - x
    df = lambda x: -sin(x) - 1

    # Find a solution with an initial guess of 1.5, tolerance of 0.0001, and max of 20 iterations
    solution = newton_raphson(f, df, 1.5, 1.0e-16, 20)

    print(solution) # Output: 1.4142135623746899 (approx. sqrt(2))
