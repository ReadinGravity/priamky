import matplotlib.pyplot as plt
import numpy as np
x1=int(input("daj x1: ")); x2=int(input("daj x2: "))
y1=int(input("daj y1: ")); y2=int(input("daj y2: "))

x_values = [x1,x2]
y_values = [y1,y2]

frame1.axes.get_xaxis().set_visible(False)
frame1.axes.get_yaxis().set_visible(False)
plt.plot(x_values,y_values)
plt.savefig('foo.png')
plt.savefig('foo.pdf')
