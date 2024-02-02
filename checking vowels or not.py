alpha=(input("enter the string"))
if(alpha>='A' or alpha<='Z') or (alpha>='a' or alpha<='a'):
    if(alpha=='a' or alpha=='A' or alpha=='E' or alpha=='e' or alpha=='I' or alpha=='i' or alpha=='o' or alpha=='O' or alpha=='U' or alpha=='u'):
        print("vowel")
    else:
        print("it is a alphabet not a vowel")
else:
    print("it is a constant")