### Pie chart.
import math
from random import randrange
from matplotlib import pyplot

data = []
for n in range(100):
    data += [randrange(100) * math.sin(n)]
pyplot.hist(data)

#! Display plotted window.
pyplot.show()
