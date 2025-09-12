#Linear Regression

x=[1,2,3,4,5]
y=[1,3,2,3,5]

def find_mean(a):
    return sum(a)/len(a)

mean_x = find_mean(x)
mean_y = find_mean(y)

print(mean_x)
print(mean_y)

#m formula: #m = sum((xi-mean(x)) * (yi-mean(y))) / sum((xi – mean(x))^2)

num = 0
den = 0

for i in range(len(x)):
    num = num+((x[i]-mean_x)*(y[i]-mean_y))
    den = den + pow((x[i]-mean_x),2)

m=num/den

#c formula: #c = mean(y) – m * mean(x)

c = round(mean_y-m*mean_x,1)

print("Manually finding m and c")
print("m = ",m)
print("c = ",c)

import numpy as np
from sklearn.linear_model import LinearRegression

x = np.array([[1],[2],[3],[4],[5]])
y = np.array([[1],[3],[2],[3],[5]])

reg = LinearRegression()
reg = reg.fit(x,y)
print("M & C Value thru machine learning")

print("m = ",reg.coef_)
print("c = ",reg.intercept_)