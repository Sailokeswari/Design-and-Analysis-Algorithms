# Implementation of quicksort for the ith order statistic

def partition_quicksortarray(arr, lowest_ele, highest_ele):

    # Choosing the rightmost element as the pivot
    pivot_ele = arr[highest_ele]
    i = lowest_ele - 1
    for j in range(lowest_ele, highest_ele):
        if arr[j] <= pivot_ele:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[highest_ele] = arr[highest_ele], arr[i + 1]
    return i + 1

def quicksort(arr, low, high):
     # Recursive function to perform quicksort
    if low < high:
        pi = partition_quicksortarray(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)

def implement_ith_order_statistic_ele(arr, i):
    # Function for finding the ith order statistic in the array
    n = len(arr)
    if i < 0 or i >= n:
        return None
    quicksort(arr, 0, n - 1)
    return arr[i]

# Example:
arr = [21, 4, 9, 1, 3, 91, 55]
# finding the 3rd order statistic which is the 4th smallest element
i = 3  
print(f"The {i}th order statistic is: {implement_ith_order_statistic_ele(arr, i)}")

# Output:
# The 3th order statistic is: 9