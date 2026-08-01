# import math

# class circle:
#     def __init__(self,radius):
#         self.radius = radius
    
#     def area(self):
#         return (math.pi)*self.radius**2
#     def perimeter(self):
#         return 2*(math.pi)*self.radius**2
        

# Circle = circle(5)
# Area = Circle.area()
# Perimeter = Circle.perimeter()

# print("Area is :",Area," Perimeter is :",Perimeter)


# class Rectangle:
#     def __init__(self,height,width):
#         self.height = height
#         self.width = width
#     def area(self):
#         return self.height*self.width
#     def perimeter(self):
#         return 2*(self.height+self.width)
    
    
# rectangle = Rectangle(4,8)
# Area = rectangle.area()
# Perimeter = rectangle.perimeter()

# print("Area is :",Area," Perimeter is :",Perimeter)


# f = open("fourthDayAndAssignment.txt","r")
# data = f.read()
# print(data)
# # f.close()


with open("fourthDayAndAssignment.txt") as f:
    print(f.read())