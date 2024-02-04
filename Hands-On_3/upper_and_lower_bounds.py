# 3. Plot for Upper and Lower Bounds of algorithm

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

# Specifying upper and lower bounds

upper_bound = 1.0 * npy.polyval(fit_datapoints, n_val)
lower_bound = 0.5 * npy.polyval(fit_datapoints, n_val)

# printing  big-O and big-Omega

print("Upper Bound (Big-O):", upper_bound)
print("Lower Bound (Big-Omega):", lower_bound)

# Plot for upper and lower bounds of curve

pltlb.plot(n_val, upper_bound, 'm', linewidth=1.5, label='Upper_Bound')
pltlb.plot(n_val, lower_bound, 'o', linewidth=1.5, label='Lower_Bound')
pltlb.xlabel('Values of n')
pltlb.ylabel('Time(s)')
pltlb.title('Plot For Algoritm Runtime Upper and Lower Bounds')
pltlb.grid(True)
pltlb.legend()
pltlb.show()


# Output:
The Big-O, Big-Omega and Big-theta of given algorithm arange
Upper Bound Big-O : O(n^2)
3.53206539e-04  3.63520753e-04  3.73958144e-04  3.84518710e-04

Lower Bound Big-Omega: Ω(n^2)
5.37556923e-03  5.40141994e-03  5.42733223e-03  5.45330611e-03

Big-theta: Θ(n^2)
 