def find_maximum_subarray(A, low, high):
    if high == low:
        return low, high, A[low]  # Base case: single element

    mid = (low + high) // 2  # Calculate midpoint
    left_low, left_high, left_sum = find_maximum_subarray(A, low, mid)  # Left half
    right_low, right_high, right_sum = find_maximum_subarray(A, mid + 1, high)  # Right half
    cross_low, cross_high, cross_sum = find_max_crossing_subarray(A, low, mid, high)  # Crossing subarray

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low, left_high, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low, right_high, right_sum
    else:
        return cross_low, cross_high, cross_sum

def find_max_crossing_subarray(A, low, mid, high):
    left_sum = float('-inf')
    sum_ = 0
    max_left = 0

    for i in range(mid, low - 1, -1):
        sum_ += A[i]
        if sum_ > left_sum:
            left_sum = sum_
            max_left = i

    right_sum = float('-inf')
    sum_ = 0
    max_right = 0

    for j in range(mid + 1, high + 1):
        sum_ += A[j]
        if sum_ > right_sum:
            right_sum = sum_
            max_right = j

    return max_left, max_right, left_sum + right_sum

# Example usage
A = [3, -4, 6, -2, 5, -1, 2, -7]
low, high, max_sum = find_maximum_subarray(A, 0, len(A) - 1)
print(f"The maximum subarray has sum {max_sum}, and it spans from index {low} to {high}.")
