import numpy as np
from scipy.special.orthogonal import p_roots

def gauss_legendre(n):
    """Generate the weights and points for a Gaussian quadrature rule
    using the Legendre polynomial of degree n.
    
    Returns:
        cs (list): The weights for the quadrature rule.
        xs (list): The points for the quadrature rule.
    """
    xs, ws = p_roots(n)
    cs = 0.5 / (1 - xs**2) * ws
    return cs.tolist(), xs.tolist()



MAX_N = 10

cs_dict = {}
xs_dict = {}

for n in range(1, MAX_N+1):
    c, x = gauss_legendre(n)
    cs_dict[n] = c
    xs_dict[n] = x

print("cs =", cs_dict)
print("xs =", xs_dict)
