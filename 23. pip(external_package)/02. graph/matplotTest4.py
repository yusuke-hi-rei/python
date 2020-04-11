### Bar graph.
from matplotlib import pyplot

x = range(10)
y = range(500, 1000, 50)

data = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# tick_label: X axis label.
pyplot.bar(x, y, tick_label=data)

#! Display plotted window.
pyplot.show()


