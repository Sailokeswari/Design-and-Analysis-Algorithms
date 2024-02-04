# 2. Plot for Algorithm Runtime of Time vs n

import time
import numpy as npy
import matplotlib.pyplot as pltlb

# fun definition from given algorithm

def f(n):
    x = 1
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            x = x+1
    return x

n_val = npy.arange(1, 400)
exe_times = npy.zeros_like(n_val, dtype=float)

for index, n in enumerate(n_val):
    initial_time = time.time()
    f(n)
    exe_times[index] = time.time() - initial_time

# plotting a graph for Algorithm runtime of time vs n

pltlb.plot(n_val, exe_times, 'bo', label='Data')
fit_datapoints = npy.polyfit(n_val, exe_times, 2)
fitted_curve = npy.polyval(fit_datapoints, n_val)
pltlb.plot(n_val, fitted_curve, 'r-', linewidth=2, label='Fitted Curve')
pltlb.xlabel('Values of n')
pltlb.ylabel('Time(s)')
pltlb.title('Plot For Algoritm Runtime')
pltlb.grid(True)
pltlb.legend()
pltlb.show()