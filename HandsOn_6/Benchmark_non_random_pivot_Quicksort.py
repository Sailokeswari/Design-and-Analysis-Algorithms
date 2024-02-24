# Implementation of Benchmnark for best case, worst case and average case using non_random pivot of Quicksort

import random
import time
import matplotlib.pyplot as plt

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

# benchmarking best case scenario 

def best_case_benchmark(n):
    return list(range(1, n+1))

# benchmarking worst case scenario

def worst_case_benchmark(n):
    return list(range(n, 0, -1))

# benchmarking average case scenario

def average_case_benchmark(n):
    return random.sample(range(1, n+1), n)

def benchmark_non_random_pivot(sort_fun, input_fun, sizes, iterations):
    times = []
    for n in sizes:
        total_time = 0
        for _ in range(iterations):
            arr = input_fun(n)
            start_time = time.time()
            sort_fun(arr, 0, n - 1)
            end_time = time.time()
            total_time += end_time - start_time
        avg_time = total_time / iterations
        times.append(avg_time)
    return times

sizes = [100, 200, 300, 400, 500]
iterations = 10

best_case_times = benchmark(quicksort_non_random_pivot, best_case_benchmark, sizes, iterations)
worst_case_times = benchmark(quicksort_non_random_pivot, worst_case_benchmark, sizes, iterations)
average_case_times = benchmark(quicksort_non_random_pivot, average_case_benchmark, sizes, iterations)

#plotting the graph of time vs array size n

plt.plot(sizes, best_case_times, label="Best Case Time",color='r')
plt.plot(sizes, worst_case_times, label="Worst Case Time",color='m')
plt.plot(sizes, average_case_times, label="Average Case Time",color='orange')
plt.xlabel("Input Size of array(n)")
plt.ylabel("Time (s)")
plt.title("Benchmark for Non-Random Pivot of Quicksort")
plt.legend()
plt.show()