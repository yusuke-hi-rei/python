### Trigonometric graph
import math
import numpy
from matplotlib import pyplot

#! A 360 * 5 sequence that varies smoothly from zero to 5 * PI.
x1 = numpy.linspace(0, 5 * math.pi, 360 * 5)
#! The result of the sin function for all values in the sequence.
y1 = numpy.sin(x1)
pyplot.plot(x1, y1, label="sin")

x2 = numpy.linspace(0,5 * math.pi, 360 * 5)
y2 = numpy.cos(x2)
pyplot.plot(x2, y2, label="cos")

#! Title
pyplot.title("Trigonometric")

#! X-axis and Y-axis labels.
pyplot.xlabel("x-axis")
pyplot.ylabel("y-axis")

#! Usage guide.(label="sin", label="cos")
pyplot.legend()

#! Display plotted window.
pyplot.show()


