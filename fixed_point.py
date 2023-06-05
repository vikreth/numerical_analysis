def fixed_point_method(func, p_0, tol):
    """
    Implements the fixed point method to find a root of the given function.

    Args:
        func (function): The function to find the root of.
        a (float): The starting value for the iteration.
        b (float): The ending value for the iteration.
        tol (float): The tolerance for the solution.

    Returns:
        float: The approximate root of the function.
    """
    # Initialize variables
    x0 = p_0  # Initial guess
    iter_count = 0  # Iteration count

    # Iterate until convergence
    while True:
        x1 = func(x0)
        iter_count += 1
        print(f"Iteration {iter_count}: x = {x1} f(x) = {my_func(x1)}")
        if abs(x1 - x0) < tol:
            break
        x0 = x1

        # Check for divergence
        if iter_count >= 1000:
            print("Method didn't converge after 1000 iterations.")
            return None

    return x1

if __name__ == '__main__':
    # Define your function f(x)
    def my_func(x):
        return ( 3*x**2 + 3 )**(1/4)

    # Call the fixed point method with your inputs
    fixed_point_method(my_func, 1, 1e-2)
