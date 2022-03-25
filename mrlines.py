import matplotlib.pyplot as plt
x1=[10,20,30]
y1=[10,20,30]
plt.plot(x1,y1,label="line 1")
x2=[30,40,50]
y2=[30,40,50]
plt.plot(x2,y2,label="label 2")
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('two line plot')
plt.legend()
plt.show()
