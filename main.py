#Свеженцева,Сивцов, Михайловский 1 двойка
import matplotlib.pyplot as plt
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(0,40)
plt.ylim(0,40)
plt.scatter(x=13,y=19,c='black')
plt.scatter(x=17,y=14,c='black')
plt.plot([17,17],[0,40])
plt.plot([0,40],[19,19])

plt.plot([28.2,0],[0,35.25])
plt.arrow(x=0,y=0,dx=3,dy=4, width=.08)
plt.show()