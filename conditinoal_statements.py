
print("1.inches\n 2.yards\n 3.miles\n 4.millimeter\n 5.centimeters\n 6.meters\n 7.kilometers ")
option=int(input("enter the option"))
feet=int(input("enter the feet"))
if(option==1):
    inches=feet*12
    print("given linches",inches)
elif(option==2):
    yards=feet/3
    print("given  yards %.4f "%yards)
elif (option ==3):
    miles=feet/5280
    print("given  miles   ",miles )
elif(option==4):
    millimeters=feet*305
    print("given milllimeter",millimeters)
elif (option ==5):
    centimeters=feet*30.48

    print("given  centimeters    ", centimeters)
else:
    meters=feet/3.281
    print("given meters",meters)