from timeit import default_timer as timer
import numpy as np # for np.log and np.linspace
from time import sleep # for faking a running time

ns = np.linspace(10, 100, 50)
ys = []
for n in ns:
    then = timer()

    # Fake algorithm
    print(n)
    sleep((0.03 * n * np.log(n + 2) + 10) / 10)

    now = timer()
    running_time = now - then

    # adding 1e-10 so we don't divide by zero
    ys.append(running_time / (n * np.log(n) + 1e-10))

import matplotlib.pyplot as plt # plotting functionality
plt.plot(ns, ys)
plt.xlabel("Input size")
plt.ylabel("T(n) / n log n")
plt.savefig("my-plot.pdf")
