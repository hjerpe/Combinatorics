from __future__ import division
import numpy as np
# Set of combinatoric functions used for various selection problems.


def product_of_numbers_in_range(start_int, end_int):
    """Returns the product of all integer numbers between start_int and end_int.
    Valid only when (end_int >= start_int)
    """
    product = 1
    for number in xrange(start_int, end_int+1):
        product *= number
        
    return product

    
def n_choose_k(n, k):
    """Returns the number of ways to choose k items from a set of n items.
    
    ARGS:
    n - Number of items to choose from
    k - Number of items to choose
    Valid only when (n >= k)
    RETURNS:
    The number of ways to choose k items from n items, equally, the number of
    ways to form k-subsets from a n-set"""
    return product_of_numbers_in_range(n-k+1, n) / product_of_numbers_in_range(1, k)

    
def number_of_injections(n, k):
    """Returns the number of function injections from a set of k elements to a
    set of n elements,
    i.e. the number of injective functions f: X -> Y where |X| = k and |Y| = n.
    
    ARGS:
    n - The number of elements in the target set Y
    k - The number of elements in the domain set X
    Valid only when (n >= k)
    RETURNS:
    The number of injective maps from a k-set to a n-set"""
    return product_of_numbers_in_range(n-k+1, n)

    
def number_of_surjections(n, k):
    """Returns the number of function surjections from a set of n elements to a
    set of k elements, also called The Stirling Number of the Second Kind,
    i.e. the number of surjective functions f: X -> Y, where |X| = n and |Y| = k.
    The calculated number is also equal to the number of partitions of a n-set
    into k parts.
    
    ARGS:
    n - The number of elements in the domain set X
    k - The number of elements in the target set Y
    Valid only when (n >= k)
    RETURNS:
    The number of surjective maps from a n-set to a k-set"""
    
    def calculate_S(n, k):
        """Helper method that returns the number S(n, k)"""
        if k == 0 or k == n:
            return 1
        else:
            return S[n-1, k-1] + ((k+1) * S[n-1, k])

    # The numbers follow the recursion S(n, k) = S(n-1, k-1) + k * S(n-1, k)
    # with S(n, n) = S(n, 1) = 1
    # Instance and fill memorizing table
    S = np.ones((n, k))
    for n_ind in xrange(2, n+1):
        for k_ind in xrange(2, n_ind):
            S[n_ind-1, k_ind-1] = calculate_S(n_ind-1, k_ind-1)

    return S[n-1, k-1]