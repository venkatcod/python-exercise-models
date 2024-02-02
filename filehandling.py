v=open("demo.txt",mode='w+')
v.write("hi hello")
v.seek(0)
print(v.read())

v.close()