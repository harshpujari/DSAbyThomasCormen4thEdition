def bubbleSort(arr):
	n = len(arr)
	swapped = False
	for i in range(n-1):
		# range(n) also work but outer loop will repeat one time more than needed.
		# Last i elements are already in place
		for j in range(0, n-i-1):
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			return
