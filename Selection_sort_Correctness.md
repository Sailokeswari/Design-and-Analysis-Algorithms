2. Argue selection sort correctness.

Selection Sort: Selection sort is one kind of simple and popular sorting algorithm that works mainly by selecting the smallest element in an unsorted array and bringing it at the beginning of the array repeatedly until the whole array is sorted.

Let's discuss below about the Correctness of Selective Sort.

Correctness:

As we know that,Selection Sort mainly works in that way by choosing the minimum element from the array and compares then swapping will be done repeatedly through eavh iteration by moving the least element to the beginning of the array.The array is partitioned into two disjoint regions.The first one is sorted region which contains the elemets already sorted and arranged in a specific order.The another one is unsorted region will have the elements that need to be sorted.The search action for each region will be done for the minimal element on the unsorted region of the array. 

# Example:
a = [6,7,1,8,5]
selection_sort(array)
print("Array for Sorting using Selection Sort:", arr)  

# Output: 
a = [1,5,6,7,8]

We can consider the loop varaint from below three aspects to argue the correctness of Selection sort.

Initialization:
At the start of each iteration, the portion of the array before the current position is already sorted. Initially, this is true since the array as a whole is the unsorted portion.

Maintenance: 
At the conclusion of each pass, the minimum element from the unsorted portion will be chosen and will be placed in its correct position in the sorted portion of the array. The order of remaining elements will not be changed in the sorted region. Therefore, this results after the each iteration one elemented is added on to the sorted port of the array dataset, and from the unsorted region one element is removed.

Termination:
The algorithm comes to an end when the entire array has been sorted. This will occurs when the unsorted region of array becomes empty. At this point of time, the complete array is sorted, and the correctness is preserved.

def selection_sort_implementation(a):
    for i in range(len(a)):
        small = i
        for j in range(i + 1, len(a)):
            if a[j] < a[small]:
                small = j
        a[i], a[small] = a[small], a[i] # swapping of smallest element at beginning position


 Above snippet represents the algorithm for selection sort where searching and sorting of minimum element will be done.

 The time complexity for the Selection sort is O(N^2), where n represents the number of elements that array consists of.As this algorithm works by selecting and swapping the smallest element over and over again it is very difficult and inefficient to apply on the large data sets compared to other advanced algorithms due to its quadratic time complexity.But due to its ease and simplicity of implementation it works well for smaller datasets.


3.System Information:

Processor - 11th Gen Intel(R) Core(TM) i5-1155G7 @ 2.50GHz   2.50 GHz
Installed RAM	8.00 GB (7.79 GB usable)
System type	64-bit operating system, x64-based processor




 