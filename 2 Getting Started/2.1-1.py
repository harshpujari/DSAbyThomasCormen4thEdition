import importlib.util
import os


def load_insertion_sort():
    """Load insertion_sort from the local 2.1insertionSort.py file."""
    module_path = os.path.join(os.path.dirname(__file__), "2.1insertionSort.py")
    spec = importlib.util.spec_from_file_location("insertion_sort_module", module_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.insertion_sort


def illustrate_insertion_sort(arr):
    """Print the array state after each insertion step."""
    arr = arr.copy()
    print("Initial array:", arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        print(f"After inserting element at index {i} ({key}): {arr}")
    return arr


if __name__ == "__main__":
    data = [31, 41, 59, 26, 41, 58]
    insertion_sort = load_insertion_sort()

    print("Using imported insertion sort from 2.1insertionSort.py")
    sorted_data = data.copy()
    insertion_sort(sorted_data)
    print("Final sorted array:", sorted_data)

    print("\nIllustration of insertion sort operation:")
    illustrate_insertion_sort(data)
