### Pie chart.
import math
from random import randrange
from matplotlib import pyplot

data = [12300, 9800, 7600, 4500, 2100]
label = ["Tokyo", "Osaka", "Nagoya", "Sapporo", "Kobe",]

pyplot.pie(data, labels=label)

pyplot.legend(loc="upper left");

#! Display plotted window.
pyplot.show()


