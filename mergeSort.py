def merge(arr, lb, mid, rb):
	n1 = mid - lb + 1
	n2 = rb - mid
	# create temp arrays
	L = [0] * (n1)
	R = [0] * (n2)
	# Copy data to temp arrays L[] and R[]
	for i in range(0, n1):
		L[i] = arr[lb + i]
	for j in range(0, n2):
		R[j] = arr[mid + 1 + j]
	# Merge the temp arrays back into arr[l..r]
	i = 0	 # Initial index of first subarray
	j = 0	 # Initial index of second subarray
	k = lb	 # Initial index of merged subarray
	while i < n1 and j < n2:
		if L[i] <= R[j]:
			arr[k] = L[i]
			i += 1
		else:
			arr[k] = R[j]
			j += 1
		k += 1

	while i < n1:
		arr[k] = L[i]
		i += 1
		k += 1

	while j < n2:
		arr[k] = R[j]
		j += 1
		k += 1

def mergeSort(arr, lb, rb):
	if lb < rb:
		mid = lb+(rb-lb)//2
		mergeSort(arr, lb, mid)
		mergeSort(arr, mid+1, rb)
		merge(arr, lb, mid, rb)
