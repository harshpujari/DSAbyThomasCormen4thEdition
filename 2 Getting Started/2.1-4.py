# LINEAR-SEARCH(A, n, x)
# 1 for i = 1 to n
# 2     if A[i] == x
# 3         return i
# 4 return NIL
#
# Loop Invariant:
# At the start of each iteration with index i, the subarray A[1..i-1]
# has been searched and x does not appear in that subarray.
# In other words, for all j in [1..i-1], A[j] != x.
#
# Initialization:
# Before the first iteration, i = 1 and the searched subarray A[1..i-1]
# is empty. The statement "x does not appear in A[1..0]" is vacuously true,
# so the invariant holds.
#
# Maintenance:
# Assume the invariant holds at the start of iteration i.
# The algorithm checks whether A[i] == x.
# - If yes, it returns i, which is correct because x appears at A[i].
# - If no, then x does not appear in A[i], and by the invariant x does not
#   appear in A[1..i-1]. Therefore x does not appear in A[1..i], and the
#   invariant holds for the next iteration (i+1).
#
# Termination:
# The loop terminates when i becomes n+1 after checking A[n], or earlier if x is found.
# If x is found at some index k, the algorithm returns k immediately, which satisfies the problem.
# If the loop completes without finding x, then by the invariant x does not appear in A[1..n].
# The algorithm returns NIL, which correctly indicates that x is not present.
#
# Therefore, by initialization, maintenance, and termination of the loop invariant,
# the LINEAR-SEARCH procedure is correct.


def linear_search(arr, x):
    """Return the 1-based index of x in arr, or None if x is not found."""
    for i in range(1, len(arr) + 1):
        if arr[i - 1] == x:
            return i
    return None


if __name__ == "__main__":
    A = [10, 5, 8, 3, 7]
    x = 3
    result = linear_search(A, x)
    print(f"Search for {x} returned index: {result}")
