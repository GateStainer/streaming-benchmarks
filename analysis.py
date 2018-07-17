import numpy as np
import matplotlib.pyplot as plt

with open("data/flink.txt") as f:
    data = f.readlines()

latency = []
for x in data:
	latency.append(int(x))
plt.hist(latency, 1000)
plt.title("Latency Histogram")
plt.xlabel("Latency(ms)")
plt.ylabel("Number")

plt.show()
