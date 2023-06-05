def bisection_method(func, a, b, tol):
    """
    func: the function of equation that u want to find the root
    a: the initial lower root boundary
    b: the initial upper root boundary
    tol: the acceptable error
    
    """
    
    def f(x):
        f = eval(func)
        return f
    
    error = abs(a-b)
    
    while error < tol:
        c = (a+b)/2
        
        if f(a)*f(b) >= 0:
            print('There is no root between these interval [a,b]')
            quit()
        
        elif f(a)*f(c) <0:
            b = c
            error = abs(a-b)
                
        elif f(b)*f(c) <0:
            a = c
            error = abs(a-b)
        else:
            print('you are idiot')
            quit()
            
        print(f"a = {a} and b = {b}")
        
    print(f'the error is {error}')
    
bisection_method('4*x**2 + 3*x -2', 0, 1, 0.000001)