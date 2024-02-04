# 4.Indicating n_0 on plot 

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

pltlb.plot(n_val, exe_times, 'g', label='Data')
fit_datapoints = npy.polyfit(n_val, exe_times, 2)
fitted_curve = npy.polyval(fit_datapoints, n_val)
pltlb.plot(n_val, fitted_curve, 'bo', linewidth=2, label='Fitted Curve')

# Zooming in n_0 on plot

n_0 = 100

# Indicating the location of n_0 on plot using scatter plot

pltlb.scatter(n_0, npy.polyval(fit_datapoints, n_0), s=150, c='orange', marker='s',
          label=r'n_0')
pltlb.text(n_0, npy.polyval(fit_datapoints, n_0), r'n_0', ha='right', va='bottom')

pltlb.xlabel('Values of n')
pltlb.ylabel('Time(s)')
pltlb.title('Plot for indicating n_0')
pltlb.grid(True)
pltlb.legend()
pltlb.show()