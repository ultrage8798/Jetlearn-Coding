import numpy as np

list = [1, 2, 3, 4, 5]
arr = np.array(list)

arr2 = np.array([[1,2,3][4,5,6]])

#print((arr*10))

#datatype of array
#print(arr2.dtype)

#shape of array
#print(arr2.shape)

#dimensions of array
#print(arr2.ndim)

#print(arr2)

#zeros = np.zeros(5)
#ones = np.ones(5)
#print(zeros)
#print(ones)

#arr3 = np.array([1,2,3,4,5],dtype='int')
#print(arr3)

#arr4 = np.arrange(1,10)
#arr5 = arr4.reshape(3,3)
#print(arr5.shape)
#print(arr5)

arr6 = np.array(4, 2, 1, 5, 3)
#arr7 = np.sort(arr6)
#print(arr7)

#Accessing
print(arr6[1])
print(arr2[0,2])