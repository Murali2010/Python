import factModule

n=int(input("Enter a number: "))
print("Factorial using non-recursive function")
print(factModule.fact(n))
print("Factorial using recursive function")
print("The factorial of ", n," is ",factModule.rec_fact(n))
