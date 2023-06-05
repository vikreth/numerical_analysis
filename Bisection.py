def bisection(fun, a, b, tol=1e-6, max_iter=10000):
    """
    Find the root of a function using the bisection method.

    Parameters:
        fun (function): The function whose root needs to be found.
        a (float): Left boundary of the initial bracketing interval.
        b (float): Right boundary of the initial bracketing interval.
        tol (float): Tolerance level for convergence (default: 10^-6).
        max_iter (int): Maximum number of iterations (default: 100).

    Returns:
        p (float): Approximate root of the function within the given tolerance.
    """
    # Evaluate the function at the end points of the interval
    fa = func(a)
    fb = func(b)

    # Check if the interval brackets a root
    assert fa*fb < 0, "The initial interval does not bracket a root."

    # Set the initial values for iteration
    i = 0
    p = (a+b)/2
    fp = func(p)

    # Start iterating until convergence or maximum iteration limit is reached
    #while abs(b-a) > tol and i < max_iter:
    while abs(fp) >= 1.0e-8 and i < max_iter:
        i += 1
        p = (a+b)/2
        fp = fun(p)
        print(f"Iteration {i}: x0={a:.16f}, x1={b:.16f}, p_{i}={p:.16f}, f(p_{i})={fp:.16f}")

        # Update the interval by checking the sign of the function value at midpoint
        if fp == 0:  # Root has been found
            return p
        elif fa*fp < 0:  # Root lies between a and p
            b = p
            fb = fp
        else:  # Root lies between b and p
            a = p
            fa = fp

    print(f"Terminated after {i} iterations with tolerance={abs(b-a):.16f}")
    return p

if __name__ == '__main__':
    
    import math as m
    def func(x):
        return m.sqrt(x) - m.cos(x)

    root = bisection(func, 0, 1)
    print(f"The root is approximately {root:.6f}")