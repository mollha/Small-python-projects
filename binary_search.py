def binary_search(array: list, target, start=0, end=None):
    if not end:
        end = len(array) - 1

    if not (end - start):
        if array[start] == target:
            return array[start]
        else:
            return 'Error, the target could not be found in the array'

    array.sort()
    middle_index = start + (end - start) // 2
    center_val = array[middle_index]

    if center_val == target:
        return middle_index
    elif center_val < target:
        return binary_search(array, target, middle_index + 1, end)
    else:
        return binary_search(array, target, start, middle_index - 1)


print(binary_search([1, 2, 4, 6, 8, 2, 4, 6, 8, 9, 3, 5, 6, 2], 4))

# Worst-case time complexity is O(logn)
# Worst-case space complexity is O(1)