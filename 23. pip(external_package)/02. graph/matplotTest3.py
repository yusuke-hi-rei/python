### Scatter plot
import math
from random import randrange
from matplotlib import pyplot

x1 = []
y1 = []
for n in range(1000):
    x1 += [randrange(100) * math.sin(n)]
    y1 += [randrange(100) * math.cos(n)]
#! "+"".""x""o""*" etc. can be used.
pyplot.plot(x1, y1, "+")

#! Display plotted window.
pyplot.show()


