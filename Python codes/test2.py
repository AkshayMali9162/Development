class Akshay():  
    gender = "Male"
    def __init__(self,name,age,comp):
        self.name = name
        self.age = age
        self.comp = comp
  
    def actions(self):
        print(f"Hello My name is {self.name} and i am {self.age} years old My current comp is {self.comp}, my gender is {Akshay.gender}")

    def love(self,name):
        print(f"My fav game is {name}")
        
class Kartik(Akshay):

    def __init__(self, name, age, comp):
        Akshay.__init__(self, name, age, comp)


firstemp = Akshay(name="akshay",age = 24,comp = "tcs")
print(firstemp.age)
print(firstemp.comp)
print(firstemp.gender)
print(firstemp.name)
firstemp.actions()
firstemp.love(name="gta")

print("-"*100)
secondtemp = Kartik(name="Kartik",age = 23,comp = "eng")
print(secondtemp.age)
print(secondtemp.comp)
print(secondtemp.gender)
print(secondtemp.name)
secondtemp.actions()
secondtemp.love(name="gta")




