class person():
    def __init__(self,name):
        self.name=name
    def namelength(self):
        print("give the characters of the ",len(self.name))
a=person(input("enter the number"))
a.namelength()