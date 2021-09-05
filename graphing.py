'''
Graphs percentage increase in performance (raw and relative to previous performance) after addition of
player ability scores
'''
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('dark_background')

raw = [1.75,3.22,4.51,1.15,1.39]
relative = [2.15,3.77,5.13,1.28,1.45]
names = ['SVM', 'MNB', 'DT','KNN','Neural']



fig, ax = plt.subplots()
bar_width = 0.4
x = np.arange(len(names))
b1 = ax.bar(x, raw, width=bar_width, label="raw")
b2 = ax.bar(x + bar_width, relative, width=bar_width, label="relative")
ax.set_xticks(x+bar_width/2)
ax.set_xticklabels(names)
ax.set_ylabel("Percentage Increase in Accuracy")
ax.set_xlabel("Algorithm")
ax.legend()
ax.grid(axis='y')
fig.show()