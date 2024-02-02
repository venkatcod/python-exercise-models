amount=int(input("enter the number"))
if amount<=100:
    try:
        raise TypeError
    except:
        print("insufienct")
    else:
        print("hjkl")