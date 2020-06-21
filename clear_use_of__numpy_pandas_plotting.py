import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

a=np.array([1,2,3])
b=np.array([[1.3,2.4],[.3,4.1]])
d=np.array(((1,2,3),(4,5,6)))
e=np.array([(1,2,3),[4,5,6],(7,8,9)])


#a, it's type and other methods
print(a,"\n",type(a),"\n",a.dtype,"\n",a.ndim,"\n",a.size,"\n",a.shape)

print("\n","\n")

#b, it's type and other methods
print(b,"\n",type(b),"\n",b.dtype,"\n",b.ndim,"\n",b.size,"\n",b.shape)

print("\n","\n")

#prints d
print(d)


print("\n","\n")

#prints e
print(e)



# Data for plotting
t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

fig.savefig("test.png")
plt.show()




df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
})
print(df1)
