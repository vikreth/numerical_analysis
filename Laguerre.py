import cmath

def laguerre(poly, x0, eps=1e-16, max_iter=100):
    """
    Finds a root of a polynomial using the Laguerre method.
    
    Parameters:
        poly (list): The coefficients of the polynomial in decreasing order.
        x0 (complex): Initial guess of the root.
        eps (float): The desired accuracy.
        max_iter (int): The maximum number of iterations to perform.
        
    Returns:
        complex: The estimated root of the polynomial.
    """
    n = len(poly) - 1
    for i in range(max_iter):
        # Evaluate polynomial and its derivatives at x0
        f = poly[n]
        df = 0
        ddf = 0
        for j in range(n-1, -1, -1):
            ddf = df + x0 * ddf
            df = f + x0 * df
            f = poly[j] + x0 * f
        
        # Check if we have reached the desired accuracy
        if abs(f) < eps:
            return x0
        
        # Calculate G, H, and R
        G = df / f
        H = G**2 - ddf/f
        R = cmath.sqrt((n-1)*(n*H - G**2))
        
        # Choose the larger denominator for stability
        den1 = G + R
        den2 = G - R
        if abs(den2) > abs(den1):
            den1 = den2
        
        # Update estimate
        x1 = x0 - n/den1
        x0 = x1
        
        # Display iteration information
        print(f"Iteration {i+1}: x = {x0:.16f}, f(x) = {f:.16f}")
    
    # Did not converge within the maximum number of iterations
    raise Exception("Laguerre method did not converge.")

if __name__ == '__main__':
    poly = [1,-9,34,-20,-261,949,-1014]
    x0 = 0
    laguerre(poly=poly, x0=x0)
