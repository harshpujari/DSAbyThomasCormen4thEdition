# Function to do reverse insertion sort (sorts in descending order)
def insertionSort(arr):
	# Traverse through the array starting from the second element
	for i in range(1, len(arr)):

		key = arr[i]
		j = i-1

		# Shift elements that are smaller than key to the right
		while j >= 0 and key > arr[j]:
			arr[j+1] = arr[j]
			j -= 1

		# Place key at the correct descending order position
		arr[j+1] = key

if __name__ == "__main__":
	# Example usage for descending order sort
	arr = [64, 34, 25, 12, 22, 11, 90]
	insertionSort(arr)
	print("Sorted array in descending order:", arr)
