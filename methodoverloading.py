def fib():
    f1=0
    f2=1

    n=int(input("enter the number"))
    print(f1)
    print(f2)
    for i in range(2,n+1):
        f=f1+f2
        print(f)
        f1=f2
        f2=f
fib()