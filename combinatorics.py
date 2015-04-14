from __future__ import division
import numpy as np
# Set of combinatoric functions used for various selection problems.

def contain_neg_number(list_numbers):
    return next((True for number in list_numbers if number < 0), False)


def product_of_numbers_in_range(start_int, end_int):
    """Returns the product of all integer numbers between the two positive
    integers start_int and end_int."""
    if contain_neg_number([np.abs(end_int) - np.abs(start_int)]):
        raise ValueError('arg_1 <= arg_2')
        
    return reduce(lambda x, y: x * y, xrange(start_int, end_int+1))


def n_choose_k(n, k):
    """Returns the number of ways to choose k items from a set of n items.
    ARGS:
    n - Number of items to choose from
    k - Number of items to choose
    RETURNS:
    The number of ways to choose k items from n items, equally, the number of
    ways to form k-subsets from a n-set"""
    if contain_neg_numbers([n, k]):
        raise ValueError('Function not implemented for negative values')
    # Base cases
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    return product_of_numbers_in_range(n-k+1, n) / product_of_numbers_in_range(1, k)


def number_of_injections(n, k):
    """Returns the number of function injections from a set of k elements to a
    set of n elements.
    That is the number of injective functions f: X -> Y where |X| = k and |Y| = n.
    ARGS:
    n - The number of elements in the target set Y
    k - The number of elements in the domain set X
    RETURNS:
    The number of injective maps from a k-set to a n-set"""
    if contain_neg_numbers([n, k]):
        raise ValueError('Function not implemented for negative values')
    # Base cases
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    return product_of_numbers_in_range(n-k+1, n)


def number_of_parts(n, k):
    """Returns the number of partitions of an n-set X into k parts, the number
    is also called the Stirling number of the second kind.
    (A partition is a family of sets such that the union of all parts equals X
    and such that each pair of parts are disjoint)
    ARGS:
    n - The number of elements in the set X to be partitioned
    k - The number of sets in the partitioning of X.
    RETURNS:
    The number of possible partitions of an n-set X into k parts"""
    
    def stirling_second_kind(n, k):
        """Helper method that returns the StirlingII number S(n, k)"""
        if k == 0 or k == n:
            return 1
        else:
            return S[n-1, k-1] + ((k+1) * S[n-1, k])

    if contain_neg_numbers([n, k]):
        raise ValueError('Function not implemented for negative values')
    # Base cases    
    if k > n:
        return 0
    elif k == n or k == 0 or k == 1:
        return 1
    # The numbers follow the recursion S(n, k) = S(n-1, k-1) + k * S(n-1, k)
    # with S(n, n) = S(n, 1) = 1
    # Instance and fill memorizing table
    S = np.ones((n, k))
    for n_ind in xrange(2, n+1):
        k_hb = np.min((n_ind, k))
        for k_ind in xrange(2, k_hb):
            S[n_ind-1, k_ind-1] = stirling_second_kind(n_ind-1, k_ind-1)
    return S[n-1, k-1]


def number_of_surjections(n, k):
    """Returns the number of surjections from an n-set X onto a k-set Y.
    That is the number of surjective mappings f: X -> Y,
    where |X| = n and |Y| = k.
    ARGS:
    n - Number of elements in the domain X
    k - Number of elements in the set Y
    RETURNS:
    The number of surjective mappings from an n-set X onto a k-set Y"""
    k_factorial = product_of_numbers_in_range(1, k)
    return k_factorial * number_of_parts(n, k)