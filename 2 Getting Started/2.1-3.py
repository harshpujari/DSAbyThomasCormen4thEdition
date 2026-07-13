def insertion_sort_descending(arr):
    """Sort arr into monotonically decreasing order using insertion sort."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        # Shift elements that are smaller than key to the right.
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    data = [31, 41, 59, 26, 41, 58]
    insertion_sort_descending(data)
    print("Sorted array in decreasing order:", data)
