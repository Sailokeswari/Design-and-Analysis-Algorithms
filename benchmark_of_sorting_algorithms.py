import timeit
import numpy as npy
import matplotlib.pyplot as pltlb

# Bubble sort Algorithm for Sorting

def bubble_sort_implementation(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

# Selection sort Algorithm for Sorting

def selection_sort_implementation(a):
    for i in range(len(a)):
        small = i
        for j in range(i + 1, len(a)):
            if a[j] < a[small]:
                small = j
        a[i], a[small] = a[small], a[i]

# Insertion sort Algorithm for Sorting

def insertion_sort_implementation(a):
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key


# Benchmarking for different algorithms and array sizes

input_sizes = [5, 10, 20,100,1000,2000]
algorithms = [insertion_sort_implementation, selection_sort_implementation, bubble_sort_implementation]
execution_times = []

# Using Random function to generate random array elements of different size

for algorithm in algorithms:
    times_for_algorithm = []
    for size in input_sizes:
        data = npy.random.randint(1, 100, size=size)
        a_copy = data.copy()
        time_taken = timeit.timeit(lambda: algorithm(a_copy), number=1)
        times_for_algorithm.append((size, time_taken))
    execution_times.append(times_for_algorithm)

# Plotting the graph of input size vs time

pltlb.figure(figsize=(10, 6))

for i, algorithm in enumerate(algorithms):
    times_for_algorithm = execution_times[i]
    sizes, times = zip(*times_for_algorithm)
    pltlb.plot(sizes, times, label=algorithm.__name__, marker='o')

pltlb.xlabel('Input Size of Array')
pltlb.ylabel('Time Taken for Execution(s)')
pltlb.title('Benchmark for Insertion,Selection and Bubble Sort Algorithms')
pltlb.legend()
pltlb.show()

