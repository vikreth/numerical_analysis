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
    print("{:<7s} {:<20s} {:<20s}".format("i", "p", "f(p)"))
    print("{:<7d} {:<20f} {:<20e}".format(i-2, p0, q0))
    print("{:<7d} {:<20f} {:<20e}".format(i-1, p1, q1))

    # Perform iterations
    while i <= No:
        p = p1 - q1*(p1-p0)/(q1-q0)
        fp = f(p)
        
        # Display intermediate results
        print("{:<7d} {:<20f} {:<20e}".format(i, p, fp))
        
        # Check for convergence
        if abs(fp) < tol:
        #if abs(fp) < 1.0e-4:
        #if abs(p-pa) < 1.0e-4:
            return p
        
        # Update variables for next iteration
        i += 1
        p0 = p1
        p1 = p
        q0 = q1
        q1 = fp
    
    # Display error message if maximum number of iterations is reached
    print("After {} iterations, could not find root within tolerance.".format(No))

# Test the function with example parameters
def f(x):
    from math import exp
    return exp(x) - 2*x - 2

root = SectM(f=f, pa=1, pb=2, tol=1.0e-16, No=1000)
if root:
    print("\nRoot found at x = {}".format(root))
