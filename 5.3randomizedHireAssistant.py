import random

# Example list of candidates (you can replace this with your actual list)
lst = [5, 8, 2, 10, 3]

# Shuffle the list
random.shuffle(lst)

# Initialize the best variable with the first element of the shuffled list
best = lst[0]

# Iterate through the shuffled list
for i in lst:
    # Compare the current element with the current best value
    if i > best:
        # Update the best value if the current element is greater
        best = i

# Return the maximum value found
print("Maximum Value:", best)
