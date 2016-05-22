# 6.00 Problem Set 2
#
# Successive Approximation
#
# Name          : Markell
# Collaborators : N/A
# Time spent    : 1.5 hrs
#
def evaluate_poly(poly, x):
    """
    Computes the polynomial function for a given value x. Returns that value.

    Example:
    >>> poly = (0.0, 0.0, 5.0, 9.3, 7.0)    # f(x) = 7x^4 + 9.3x^3 + 5x^2
    >>> x = -13
    >>> print evaluate_poly(poly, x)  # f(-13) = 7(-13)^4 + 9.3(-13)^3 + 5(-13)^2
    180339.9

    poly: tuple of numbers, length > 0
    x: number
    returns: float
    """
    # TO DO ... 
    # highest power = len(poly) - 1
    # coefficients = tuple(i)
    value = 0
    for power in xrange(len(poly)):
        coefficient = poly[power]
        value += coefficient * (x**power)
        
    return value


def compute_deriv(poly):
    """
    Computes and returns the derivative of a polynomial function. If the
    derivative is 0, returns (0.0,).

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    # x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> print compute_deriv(poly)        # 4x^3 + 9x^2 + 35^x
    (0.0, 35.0, 9.0, 4.0)

    poly: tuple of numbers, length > 0
    returns: tuple of numbers
    """
    # TO DO ... 
    # can use same procedure as in evaluate_poly function
    # only now we just need to multiply the coefficient and power
    # and then subtract from the power of each
    
    # tricky here since tuples are immutable... can use tuple += (number,)
    # first check for the zero derivative
    if len(poly) == 1:
        return (0.0,)

    derivative = tuple()
    for power in xrange(1, len(poly)):
        coefficient = poly[power]
        new_coefficient = coefficient*power
        derivative += (new_coefficient,)
    
    return derivative	
	
   
def compute_root(poly, x_0, epsilon):
    """
    Uses Newton's method to find and return a root of a polynomial function.
    Returns a tuple containing the root and the number of iterations required
    to get to the root.

    Example:
    >>> poly = (-13.39, 0.0, 17.5, 3.0, 1.0)    #x^4 + 3x^3 + 17.5x^2 - 13.39
    >>> x_0 = 0.1
    >>> epsilon = .0001
    >>> print compute_root(poly, x_0, epsilon)
    (0.80679075379635201, 8.0)

    poly: tuple of numbers, length > 1.
         Represents a polynomial function containing at least one real root.
         The derivative of this polynomial function at x_0 is not 0.
    x_0: float
    epsilon: float > 0
    returns: tuple (float, int)
    """
    # TO DO ... 
    # first check poly at x_0 and see if difference is within epsilon
    # if it is return x_0 as root, else make an approximation using root = x_0 - f(x_0)/f'(x_0)
    # check if root is within epsilon, if it is return, else repeat
    
    count = 1
    root = x_0
    while abs(evaluate_poly(poly, root)) >= epsilon: 
        root = (root - evaluate_poly(poly, root) / evaluate_poly(compute_deriv(poly), root))
        count += 1
    return (root, count)
	

def main():

	# Run all tests for each function with the main function.
	
	## evaluate_poly(poly, x) ##
	poly = (0.0, 0.0, 5.0, 9.3, 7.0)
	x = -13
	print evaluate_poly(poly, x)	# f(-13) = 180339.9
	
	## compute_deriv(poly) ##
	poly = (-13.39, 0.0, 17.5, 3.0, 1.0)	# x^4 + 3x^3 + 17.5x^2 - 13.39 
	print compute_deriv(poly)				# (0.0, 35.0, 9.0, 4.0)
	print compute_deriv((1.0,))
	
	## compute_root(poly, x_0, epsilon)
	poly = (-13.39, 0.0, 17.5, 3.0, 1.0)	# x^4 + 3x^3 + 17.5x^2 - 13.39
	x_0 = 0.1
	epsilon = .0001
	print compute_root(poly, x_0, epsilon)	# (0.80679075379635201, 8)


if __name__ == '__main__':
	main()