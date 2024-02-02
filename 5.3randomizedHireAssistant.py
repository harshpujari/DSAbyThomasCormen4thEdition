import random

def find_maximum_value(candidate_list):
    # Shuffle the list of candidates
    random.shuffle(candidate_list)

    # Initialize the best variable with the first element of the shuffled list
    best = candidate_list[0]

    # Iterate through the shuffled list
    for i in candidate_list:
        # Compare the current element with the current best value
        if i > best:
            # Update the best value if the current element is greater
            best = i

    # Return the maximum value found
    return best

# Example list of candidates (you can replace this with your actual list)
candidates = [5, 8, 2, 10, 3]

# Call the function with the list of candidates
result = find_maximum_value(candidates)

# Print the result
print("Maximum Value:", result)
