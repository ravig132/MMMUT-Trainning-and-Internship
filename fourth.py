# class student:
#     name = "Ravi"

# S1 = student()
# print(S1.name)
# del S1


# class person:
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name

# p1 = person(18,"Ravi")
# print(p1.name)
# print(p1.age)



# class dog:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
#     def bark(self):
#         print(self.name,"Woof!")


# d1 = dog("Buddy",3)
# d1.bark()


# class person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age = age 
#     def greet(self):
#         print("Hello my name is :",self.name)


# p1 = person("John",36)
# p1.greet()

# class car:
#     def __init__(self,brand,price):
#         self.brand = brand
#         self.price = price
#     def printBrandName(self):
#         print("Car brand is :",self.brand)
#     def printCarPrice(self):
#         print("The price is :",self.price)
        

# c1 = car("Thar",700000)
# c1.printBrandName()
# c1.printCarPrice()

# class student:
#     def __init__(self,name,grade):
#         self.name = name 
#         self.grade = grade 
    


# s1 = student("Ram","A")
# print(s1.grade)

# s1.grade = "B"

# print(s1.grade)


# class rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#     def area(self):
#         return self.height*self.width

# r1 = rectangle(5,3)
# print("Area of the rectangle is :",r1.area())



class animal:
    def __init__(self,name):
        self.name = name 
    def speak(self):
        print(self.name)

class dog(animal):
    pass

d1 = dog("Rex")

d1.speak()

