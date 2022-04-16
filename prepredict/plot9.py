import matplotlib.pyplot as plt
from pylab import *
import numpy as np
mpl.rcParams['font.sans-serif'] = ['SimHei']
res=[[1, 4, 9, 4, 10, 10, 6, 0], [0, 0, 0, 6, 15, 14, 6, 6], [6, 3, 9, 3, 5, 17, 9, 5], [7, 5, 10, 12, 11, 11, 10, 3],
     [5, 3, 8, 7, 10, 12, 1, 5], [5, 4, 12, 7, 6, 10, 7, 5], [4, 7, 8, 6, 8, 13, 5, 6], [6, 2, 7, 9, 10, 14, 8, 2],
     [7, 2, 15, 11, 10, 13, 5, 1]]
id = [1,2,3,4,5,6,7,8,9]
date = ['17','18','19','20','21','22','23','24','25']
tit=['0-3时','3-6时','6-9时','9-12时','12-15时','15-18时','18-21时','21-24时']
change=[]
y=range(0,15,3)
for i in range(0,8):
     lit=[]
     for j in range(0,9):
          print(j)
          lit.append(res[j][i])
     change.append(lit)
print(change)
fig=plt.figure(1)
for i in range(0,8):
     ax1=plt.subplot(4,2,i+1)
     plt.plot(id,change[i],color='b')
     plt.xlabel('日')
     plt.ylabel('船流量/艘')
     plt.yticks(y)
     plt.xticks(id, date)
     plt.title(tit[i])
plt.show()
# b=[1,0,6,7,5,5,4,6,7]
# b=np.array(b)
# from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
# plot_acf(b)
# plt.show()
# plot_pacf(b)
# plt.show()