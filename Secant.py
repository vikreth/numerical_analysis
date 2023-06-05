def SectM(f, pa, pb, tol, No):
    # This program is to find root using Secant method
    # INPUTS:
    # f represents the function that you want to find the root
    # pa represents initial point 1 of the search
    # pb represents initial point 2 of the search
    # tol represents the tolerance 
    # No represents the total number of iteration to be performed
    # OUTPUTS:
    # i represents current number of iteration
    # p represents the computed root
    
    # Initialize variables
    i = 2
    p0 = pa
    p1 = pb
    q0 = f(p0)
    q1 = f(p1)

    # Display table header
    print("{:<7s} {:<25s} {:<25s}".format("i", "p", "f(p)"))
    print("{:<7d} {:<25.15f} {:<25.15e}".format(i-2, p0, q0))
    print("{:<7d} {:<25.15f} {:<25.15e}".format(i-1, p1, q1))

    # Perform iterations
    while i <= No:
        p = p1 - q1*(p1-p0)/(q1-q0)
        fp = f(p)
        
        # Display intermediate results
        print("{:<7d} {:<25.15f} {:<25.15e}".format(i, p, fp))
        
        # Check for convergence
        if abs(fp) < tol:
            return p
        
        # Update variables for next iteration
        i += 1
        p0 = p1
        p1 = p
        q0 = q1
        q1 = fp
    
    # Display error message if maximum number of iterations is reached
    print("After {} iterations, could not find root within tolerance.".format(No))

if __name__ == '__main__':
    from math import exp, pi, cos
    # Test the function with example parameters
    def f(x):
        return cos(x) - x
    root = SectM(f=f, pa=0, pb=pi/2, tol=1.0e-10, No=1000)
    if root:
        print("\nRoot found at x = {:.15f}".format(root))
