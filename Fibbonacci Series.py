TITLE="Fibonacci Series"

def Fibonacci(number):
    fib=[0,1]
    for i in range(2,number):
        fib.append(fib[i-1]+fib[i-2])
    return fib
print (Fibonacci(10))

def factorial(number):
    if number==0:
        return 1
    else:
        return number*factorial(number-1)
print(factorial(10))

def summing(number):
    if number==0 or number==1:
        return number
    else:
        return number+summing(number-1)
print(summing(10))