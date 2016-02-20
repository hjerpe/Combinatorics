from __future__ import division
from itertools import permutations, combinations
import numpy as np
# Set of combinatoric functions used for various selection problems.

def contain_neg_number(list_numbers):
    return next((True for number in list_numbers if number < 0), False)


def product_of_numbers_in_range(start_int, end_int):
    """Returns the product of all integer numbers between the two positive
    integers start_int and end_int."""
    
    return reduce(lambda x, y: x * y, xrange(start_int, end_int+1))


def n_choose_k(n, k):
    """Returns the number of unordered selections of k items from a set of n
    items without repetition.
    
    ARGS:
    n - Number of items to choose from.
    k - Number of items to choose.
    """

    # Base cases
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    return product_of_numbers_in_range(n-k+1, n) / product_of_numbers_in_range(1, k)


def number_of_injections(n, k):
    """Returns the number of ordered selections of k items from a set of n items
    without repetition.
    
    ARGS:
    n - Number of items to choose from.
    k - Number of items to choose.
    """

    # Base cases
    if k > n:
        return 0
    elif k == n or k == 0:
        return 1
    return product_of_numbers_in_range(n-k+1, n)


def number_of_parts(n, k):
    """Returns the number of partitions of an n-set X into k parts, the numbers
    is also called the Stirling numbers of the second kind.

    ARGS:
    n - The number of elements in the set X to be partitioned.
    k - The number of sets in the partitioning of X.
    
    COMMENTS:
    A partition of X is a family of sets such that the union of all parts equals
    X and such that each pair of parts are disjoint.
    """
    
    def stirling_second_kind(n, k):
        """Helper method that returns the StirlingII number S(n, k)"""
        if k == 0 or k == n:
            return 1
        else:
            return S[n-1, k-1] + ((k+1) * S[n-1, k])

    # Base cases    
    if k > n:
        return 0
    elif k == n or k == 0 or k == 1:
        return 1
    # The numbers follow the recursion S(n, k) = S(n-1, k-1) + k * S(n-1, k)
    # with S(n, n) = S(n, 1) = 1
    # Instance and fill memoizing table
    S = np.ones((n, k))
    for n_ind in xrange(2, n+1):
        k_hb = np.min((n_ind, k))
        for k_ind in xrange(2, k_hb):
            S[n_ind-1, k_ind-1] = stirling_second_kind(n_ind-1, k_ind-1)
    return S[n-1, k-1]


def number_of_surjections(n, k):
    """Returns the number of surjective functions from an n-set X onto a k-set Y.

    ARGS:
    n - Number of elements in the domain X
    k - Number of elements in the set Y
    """

    k_factorial = product_of_numbers_in_range(1, k)
    return k_factorial * number_of_parts(n, k)


def order_increment_array(arr_ord_numbers, sum_condition):
    '''Mutates the array of numbers A = [a1,..,an] such that all numbers satisfy
    a1 <= a2 <= .. <= an and sum(ai) = sum_condition. The increment is the 
    smallest increment such that the total order is satisfied.
    arr_ord_numbers must start at a valid configuration (a1<=a2<=..<=an).
    
    Value: bool
    True if the input array is mutated and the increment is valid, and else 
    False.'''


    ind_dec = 0
    ind_inc = 0
    # Get increase and decrease indices starting from tail and going to head
    for i in xrange(len(arr_ord_numbers)-1, 0, -1):
        if arr_ord_numbers[i] > arr_ord_numbers[i-1]:
            ind_dec = i
            break
    for j in xrange(ind_dec-1, -1, -1):
        ind_inc = j
        if arr_ord_numbers[ind_dec] - arr_ord_numbers[ind_inc] > 1:
            break

    # Check if relation a1 <= a2 <=... <= an holds after increment
    if ind_inc == 0:
        value_first_numbers = arr_ord_numbers[0]+1
        last_value = sum_condition - \
                (value_first_numbers * (len(arr_ord_numbers)-1))

        if value_first_numbers > last_value:
            return False

    arr_ord_numbers[ind_inc] += 1
    arr_ord_numbers[ind_dec] -= 1
    # Shortcut since we decrease from tail and start increase from tail-1
    if arr_ord_numbers[ind_inc] + arr_ord_numbers[ind_dec] == sum_condition: 
        return True
    
    # (If no shortcut). Change all numbers to the left of the increased position
    # to the smallest total order configuration (a1<=..<=an)

    s = sum(arr_ord_numbers[0:ind_inc])
    for i in range(ind_inc+1, len(arr_ord_numbers)):
        s += arr_ord_numbers[ind_inc]
        if i == len(arr_ord_numbers)-1:
            arr_ord_numbers[i] = sum_condition - s
        else:
            arr_ord_numbers[i] = arr_ord_numbers[ind_inc]
    return True


def ordered_selection_without_repetition(n, k):
    '''Yield all possible k-sized selections out of the n elements {0,..,n-1}.  
    Each selection is represented as a tuple of length k with values in 
    {0,1,..,n-1}.
    '''


    possible_permutations = combinations(xrange(n), k)
    for perm in possible_permutations:
        for p in permutations(perm):
            yield p
