#Свеженцева,Сивцов 1 двойка
import matplotlib.pyplot as plt
plt.xlabel('x1')
plt.ylabel('x2')
plt.xlim(0,40)
plt.ylim(0,40)
plt.scatter(x=19,y=13,c='black')
plt.scatter(x=14,y=17,c='black')
plt.plot([0,20],[17,17])
plt.plot([19,19],[0,20])

plt.plot([0,35.25],[28.2,0])
plt.arrow(x=3,y=5,dx=2,dy=2)
plt.show()