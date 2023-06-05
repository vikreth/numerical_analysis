def polyEval(a:list, x:float, d:int):
    N = len(a)
    n = N - 1
    v = [0]*(d+1)
    v[0] = a[n]
    for k in range(1, N, 1):
        for l in range(d, 0, -1):
            v[l] = l*v[l-1]+x*v[l]
        v[0] = a[n-k]+x*v[0]
    return v


if __name__ == '__main__':
    # Define the coefficients of the polynomial
    a = [4, 1, 5, -2, 3]

    # Evaluate the polynomial at x=2, computing its first two derivatives
    x = 2
    d = 2
    result = polyEval(a, x, d)

    # Print the results
    print(result)
