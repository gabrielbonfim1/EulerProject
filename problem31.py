from itertools import product
from typing import Dict, List


def partial_solutions(bounds: Dict[int, int], threshold: int) -> List[int]:
    """ Produce the set of combinations of coins that doesn't exceed `threshold` pence

    The coins that may be used are specified in `bounds` which is a dictionary mapping denominations to the upper bound
    in the search space for that denomination.

    :param bounds: dictionary mapping denominations to search space upper bounds
    :param threshold: the sum-total threshold
    :return: the list of totals given by combinations of coins not exceeding `threshold`
    """

    rv = []
    for x in product(*(range(bounds[y] + 1) for y in bounds.keys())):
        subtotal = sum([ai * bi for ai, bi in zip(x, bounds.keys())])
        if subtotal <= threshold:
            rv.append(subtotal)
    rv.sort()
    return rv


def solve():
    """ Compute the answer to Project Euler's problem #31 """

    target = 200  # in pence
    subset1, subset2 = [2, 20, 50], [5, 10, 100, 200]  # 1p is not included
    bounds1 = {pence: target // pence for pence in subset1}
    bounds2 = {pence: target // pence for pence in subset2}

    # Independently compute partial solutions based on each non-trivial subset
    partial_solutions1 = partial_solutions(bounds1, target)
    partial_solutions2 = partial_solutions(bounds2, target)

    # Consider the cross-product of partial solutions and identify any combination not exceeding two points
    answer = 0
    for ps1 in partial_solutions1:
        for ps2 in partial_solutions2:
            if ps1 + ps2 <= target:
                answer += 1  # 1p coins can increase this to target as required
            else:
                break  # ps1 + ps2 for all further ps2 will now exceed target due to sorting
    return answer

print(solve())