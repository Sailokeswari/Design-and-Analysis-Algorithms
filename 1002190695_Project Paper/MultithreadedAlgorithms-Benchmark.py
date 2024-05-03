# Implementation of Multithreaded Algorithm Runtime Analysis and Benchmarks

import numpy as np
import timeit
import matplotlib.pyplot as plt
import threading

class SortingAlgorithmsMultithreaded:
    def __init__(self, arr):
        self.arr = arr

    # Brute-force Insertion Sort
    def insertion_sort(self):
        for i in range(1, len(self.arr)):
            key = self.arr[i]
            j = i - 1
            while j >= 0 and self.arr[j] > key:
                self.arr[j + 1] = self.arr[j]
                j -= 1
            self.arr[j + 1] = key

    # Brute-force Selection Sort
    def selection_sort(self):
        for i in range(len(self.arr)):
            min_idx = i
            for j in range(i + 1, len(self.arr)):
                if self.arr[j] < self.arr[min_idx]:
                    min_idx = j
            self.arr[i], self.arr[min_idx] = self.arr[min_idx], self.arr[i]

    # Brute-force Bubble Sort
    def bubble_sort(self):
        n = len(self.arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]

    # Merge Sort
    def merge_sort(self):
        def merge(arr, l, m, r):
            n1 = m - l + 1
            n2 = r - m

            L = [0] * n1
            R = [0] * n2

            for i in range(n1):
                L[i] = arr[l + i]

            for j in range(n2):
                R[j] = arr[m + 1 + j]

            i = 0
            j = 0
            k = l

            while i < n1 and j < n2:
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < n1:
                arr[k] = L[i]
                i += 1
                k += 1

            while j < n2:
                arr[k] = R[j]
                j += 1
                k += 1

        def merge_sort_helper(arr, l, r):
            if l < r:
                m = (l + r) // 2

                merge_sort_helper(arr, l, m)
                merge_sort_helper(arr, m + 1, r)

                merge(arr, l, m, r)

        merge_sort_helper(self.arr, 0, len(self.arr) - 1)

    # Brute-force Quick Sort (not practical, included for completeness)
    def quick_sort(self):
        def partition(low, high):
            pivot = self.arr[high]
            i = low - 1
            for j in range(low, high):
                if self.arr[j] < pivot:
                    i += 1
                    self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
            self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
            return i + 1

        def quick_sort_helper(low, high):
            if low < high:
                pi = partition(low, high)
                quick_sort_helper(low, pi - 1)
                quick_sort_helper(pi + 1, high)

        quick_sort_helper(0, len(self.arr) - 1)

if __name__ == "__main__":
    input_sizes = [5, 10, 20, 30, 40, 50]
    algorithms = ['insertion_sort', 'selection_sort', 'bubble_sort', 'merge_sort', 'quick_sort']
    execution_times = {algo: [] for algo in algorithms}

    threads = []
    for algorithm_name in algorithms:
        thread = threading.Thread(target=lambda name: execution_times.update({name: []}),
                                  args=(algorithm_name,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    for algorithm_name in algorithms:
        for size in input_sizes:
            data = np.random.randint(1, 100, size=size)
            algo = SortingAlgorithmsMultithreaded(data)
            time_taken = timeit.timeit(lambda: getattr(algo, algorithm_name)(), number=1)
            execution_times[algorithm_name].append((size, time_taken))

    # Plotting the graph of input size vs time
    plt.figure(figsize=(14, 8))

    for algo, times_for_algorithm in execution_times.items():
        sizes, times = zip(*times_for_algorithm)
        plt.plot(sizes, times, label=algo)

    plt.xlabel('Input Size of Array')
    plt.ylabel('Time Taken for Execution(s)')
    plt.title('Benchmark for Sorting Algorithms')
    plt.legend()
    plt.grid(True)
    plt.show()
