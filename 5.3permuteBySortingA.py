import random


def shuffle(a):
    """
    Shuffles the list a in-place using the Fisher-Yates shuffle algorithm.

    Args:
        a: The list to shuffle.

    Returns:
        None. The list is shuffled in-place.
    """

    n = len(a)
    for i in range(n):
        # Generate a random index between i and n-1 (inclusive)
        r = random.randint(i, n - 1)

        # Swap the elements at indices i and r
        a[i], a[r] = a[r], a[i]

# Example usage
my_list = [1, 2, 3, 4, 5]
shuffle(my_list)
print(my_list)
