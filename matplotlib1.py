import matplotlib.pyplot as plt

x = [1 , 2 ,3 ,4, 5]
y = [1, 4, 9, 16, 25]

plt.plot(x,y,"g--") #r=red b=blue g=green --=dashed o=dots for each point (ro,go,bo,r--,g--,b--)
plt.plot([0,1,2,3],[0,1,4,9,],"r-",label = "Squares", linewidth = 2)
plt.plot([0,1,2,3,4,5],[0,1,8,27,64,125],"b-",label = "Cubes", linewidth = 3)
#plt.axis([0,10,0,50])
plt.ylabel("Y-Axis")
plt.xlabel("X-Axis")
plt.title("MyGraph")
#plt.legend()
plt.show()


x1 = ["A","B","C","D"]
y1 = [20, 30, 40, 50]

#plt.bar(x1,y1)
# plt.show()