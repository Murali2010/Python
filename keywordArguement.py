def main():
    interest(rate=2, time=5, principal=20000)
    interest(15000, rate=3, time=2)
    #interest(principal=2000, rate=5, 4)
def interest(principal, rate, time):
    si = principal*rate*time/100
    print("Simple Interest is $%.2f," % si)
main()
    
