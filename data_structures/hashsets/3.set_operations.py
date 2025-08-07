"""This module shows cool python set implementation"""


def array_intersection(list1, list2):
    """
    Function to find the intersection between 2 lists while ensuring no duplicates
    """
    # Remove duplicates in the 2 lists
    set1 = set(list1)
    set2 = set(list2)

    # Find the intersection using the & operator
    intersection = set1 & set2

    # Return the sorted version of the intersection
    return sorted(list(intersection))


### Finding unique elements in a list that has duplicates


def non_repeating_items(nums):
    """
    Non repeating elements in a set
    """
    seen, repeated = set(), set()
    for num in nums:
        if num in seen:
            repeated.add(num)
        else:
            seen.add(num)

    return list(seen - repeated)


def unique_elements(list1, list2):
    """
    Find unique elements to 2 lists (union - intersection)
    """
    set1 = set(list1)
    set2 = set(list2)
    unique_to_1 = sorted(list(set1 - set2))
    unique_to_2 = sorted(list(set2 - set1))
    return (unique_to_1, unique_to_2)
