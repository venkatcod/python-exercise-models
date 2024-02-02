try:
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    print(a+b)
except ValueError:
    print("it has some value errors")
except TypeError:
    print("it is a type error")