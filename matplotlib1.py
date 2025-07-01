import matplotlib.pyplot as plt

#x = [1 , 2 ,3 ,4, 5]
#y = [1, 4, 9, 16, 25]

#plt.plot(x,y,"g--") #r=red b=blue g=green --=dashed o=dots for each point (ro,go,bo,r--,g--,b--)
#plt.plot([0,1,2,3],[0,1,4,9,],"r-",label = "Squares", linewidth = 2)
#plt.plot([0,1,2,3,4,5],[0,1,8,27,64,125],"b-",label = "Cubes", linewidth = 3)
#plt.axis([0,10,0,50])
#plt.ylabel("Y-Axis")
#plt.xlabel("X-Axis")
#plt.title("MyGraph")
# plt.legend()
#plt.show()


#x1 = ["A","B","C","D"]
#y1 = [20, 30, 40, 50]

#plt.bar(x1,y1)
# plt.show()

ages = [22,55,36,45,21,67,45,23,89,11,33,67,88,67,89,12,6,9,48,68,18]
bins = [0,10,20,30,40,50,60,70,80,90,100]

#Using data above to make histogram below:

#plt.hist(ages,bins, histtype = 'bar', rwidth = 0.8)
#plt.xlabel("Age Interval")
#plt.ylabel("Frequency")
#plt.title("Histogram")
#plt.show()

#Scatterplots
#x = [1,2,3,4,5,6,7,8,9]
#y = [0,1,0,1,0,1,0,1,0]

#plt.scatter(x,y,label = "Scatter Plot", color = "red", marker = 'o', s = 50)

#plt.xlabel("X-Axis")
#plt.ylabel("Y-Axis")
#plt.title("Scatter plot")
#plt.legend()
#plt.show()

#Pi Charts:

#slices = [6,1,12,1,3]
#activities = ["sleeping","eating","working","netflix","workout & friends"]

#cols = ['c','m','r','b','g']

#plt.pie(slices, labels = activities, colors =cols, startangle = 90, shadow = True)
#plt.title("Day Chart")
#plt.show()

#Stack Plots:

days = [1,2,3,4,5]

eating = [2,3,4,3,2]
sleeping = [7,8,6,11,7]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

plt.plot([], [], color = 'm', label = 'Eating', linewidth = 5)
plt.plot([], [], color = 'c', label = 'Sleeping', linewidth = 5)
plt.plot([], [], color = 'r', label = 'Working', linewidth = 5)
plt.plot([], [], color = 'k', label = 'Playing', linewidth = 5)

plt.stackplot(days, eating, sleeping, working, playing, colors = ['m','c','r','k'])

plt.xlabel("x")
plt.ylabel("y")
plt.title("Stackplot")
plt.legend()
plt.show()