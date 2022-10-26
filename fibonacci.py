import fibModule
n=int(input("Enter n"))
print("Fibonacci Series using function")
fibModule.fib(n)
print ("Fibonacci Series using recursive function")
for num in range(0, n):
    print(fibModule.fibRec(num))
