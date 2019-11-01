"""
deft.array :: Deft Array Manipulations
"""


def bubble_sort(lst):
    """
    A simple Python implementation of bubble sorting.
    
    Parameters
    ----------
    lst : list
        List to be sorted.

    Returns
    -------
    list
        Sorted list.
    """

    for passnum in range(len(lst) - 1, 0, -1):
        for i in range(passnum):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]

    return lst

