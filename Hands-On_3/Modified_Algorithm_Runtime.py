# Runtime for Modified Algorithm

import time
import numpy as npy
import matplotlib.pyplot as pltlb

# Original consider as algo1
def algo_original(n):
    x = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            x = x + 1
    return x

# Modified consider as algo2
def algo_modified(n):
    x = 1
    y = 1
    for i in range(1,n+1):
        for j in range(1,n+1):
            x = x + 1
            y = i + j
    return x

n_val = npy.arange(1, 400)

# calculating runtime for original algorithm algo1
initial_time = time.time()
algo1_res = algo_original(200)
end_runtime_algo1 = time.time()
algo1_exetime = end_runtime_algo1 - initial_time

# calculating runtime for modified algorithm algo2
initial_time_modified = time.time()
algo2_res = algo_modified(200)
end_runtime_algo2 = time.time()
algo2_exetime = end_runtime_algo2 - initial_time_modified

# Calculate and print the difference in runtime
runtime_difference = algo2_exetime - algo1_exetime
# Finding the runtime difference between algo1 and algo2
print("Original_Runtime:", algo1_exetime, "sec")
print("Modified_Runtime:", algo2_exetime, "sec")
print("Runtime Difference:", runtime_difference, "sec")

pltlb.plot(n_val, algo1_exetime * npy.ones_like(n_val), 'red', label='Original Algorithm')
pltlb.plot(n_val, algo2_exetime * npy.ones_like(n_val), 'green', label='Modified Algorithm')
pltlb.plot(n_val, runtime_difference * npy.ones_like(n_val), 'm', label='Runtime Difference')
pltlb.xlabel('Values of n')
pltlb.ylabel('Time(s)')
pltlb.title('Runtime for Modified Algorithm')
pltlb.legend()
pltlb.show()