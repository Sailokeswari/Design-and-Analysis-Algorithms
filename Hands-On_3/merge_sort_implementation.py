# Merge Sort Implementation

def merge_Sort_Algorithm(ar):
    if len(ar) <= 1:
        return ar

# partitioning the array into two halves

    mid = len(ar) // 2

    left_half_array = ar[:mid]
    right_half_array = ar[mid:]

# storing left sorted array
    sorted_left_array = merge_Sort_Algorithm(left_half_array)

# storing right sorted array
    sorted_right_array = merge_Sort_Algorithm(right_half_array)

    return mergeArrays(sorted_left_array, sorted_right_array)

def mergeArrays(left_array, right_array):

# storing the final sorted array as a result
    final_result = []
    i = j = 0

    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            final_result.append(left_array[i])
            i = i+1
        else:
            final_result.append(right_array[j])
            j = j+1

    final_result.extend(left_array[i:])
    final_result.extend(right_array[j:])

    return final_result

unsorted_arr = [5,2,4,7,1,3,2,6]
print("Array before Merge Sort:" , unsorted_arr)
sorted_arr = merge_Sort_Algorithm(unsorted_arr)
print("Array after Merge Sort:", sorted_arr)


# Output:

Array before Merge Sort:[5, 2, 4, 7, 1, 3, 2, 6]
Array after Merge Sort: [1, 2, 2, 3, 4, 5, 6, 7]
