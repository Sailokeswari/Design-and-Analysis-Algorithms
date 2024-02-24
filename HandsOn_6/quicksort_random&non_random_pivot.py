# Implementation of Quicksort using Random and Non-Random choice of Pivot

import random

# def for non random choice of pivot element

def non_random_pivot(arr, low, high):
    pivot_ele = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot_ele:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort_non_random_pivot(arr, low, high):
    if low < high:
        piv = non_random_pivot(arr, low, high)
        quicksort_non_random_pivot(arr, low, piv - 1)
        quicksort_non_random_pivot(arr, piv + 1, high)

# def for random choice of pivot element

def random_pivot(arr, low, high):
    rand_index = random.randint(low, high)
    arr[high], arr[rand_index] = arr[rand_index], arr[high]
    return non_random_pivot(arr, low, high)

def random_pivot_quicksort(arr, low, high):
    if low < high:
        pi = random_pivot(arr, low, high)
        random_pivot_quicksort(arr, low, pi - 1)
        random_pivot_quicksort(arr, pi + 1, high)

 # sample array to sort elements using non_random and random pivot elements
arr = [11,9,19,15,2,5]
n = len(arr)
quicksort_non_random_pivot(arr, 0, n - 1)
print("Sorted array using non random pivot:", arr)

arr = [11,9,19,15,2,5]
n = len(arr)
random_pivot_quicksort(arr, 0, n - 1)
print("Sorted array using random pivot:", arr)


#Output:
#Sorted array using non random pivot: [2, 5, 9, 11, 15, 19]
#Sorted array using random pivot: [2, 5, 9, 11, 15, 19]