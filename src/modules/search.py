def binary_search(values, key):
    """Returns index of key within values or -1 if not found.

    args:
        - values: list to search
        - key: value to find
    """
    return _binary_search_helper(values, key, 0, len(values) - 1)


def _binary_search_helper(values, key, i_min, i_max):
    """Helper function for binary_search.

    args:
        - values: list to perform binary search on
        - key: value to find
        - i_min: lower index bound
        - i_max: upper index bound

    note: bounds are inclusive
    """
    if i_max < i_min:
        return -1

    i_mid = (i_max - i_min) // 2 + i_min

    if values[i_mid] > key:
        return _binary_search_helper(values, key, i_min, i_mid - 1)
    elif values[i_mid] < key:
        return _binary_search_helper(values, key, i_mid + 1, i_max)
    else:
        return i_mid
