# Python program for implementation of Quicksort Sort

# This function takes last element as pivot, places
# the pivot element at its correct position in sorted
# array, and places all smaller (smaller than pivot)
# to left of pivot and all greater elements to right
# of pivot

def partition(data: list, start:int, end: int) -> int:
    i = start - 1
    pivot = data[end]

    for j in range(start, end):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]

    data[i + 1], data[end] = data[end], data[i + 1]
    return i + 1


def quickSort(data: list, start: int, end: int):
    if start < end:
        pivot = partition(data, start, end)

        quickSort(data, start, pivot - 1)
        quickSort(data, pivot + 1, end)


arr = [10, 7, 8, 9, 1, 5]
quickSort(arr, 0, len(arr) - 1)
print(arr)