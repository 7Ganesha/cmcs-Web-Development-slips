import matplotlib as mpl
import matplotlib.pyplot as plt


#create simple graph
#using plot() method

import numpy as np
#generate random number using linspace
x=np.linspace(0,50,100)
y=x*np.linspace(100,150,100)

#set title
plt.title('simple plot')

#add x label
plt.xlabel('x side')
plt.ylabel('y side')

#set limit on x and y
plt.xlim([0,5])
(0.0, 5.0)
plt.ylim([0,5])
(0.0, 5.0)
plt.plot(x,y)
plt.show()
plt.legend(loc='upper right')