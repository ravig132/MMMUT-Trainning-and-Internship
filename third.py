# cook your dish here
# Tuble
# unchangeable,orederd,allow duplicate
# name=("Prakhar","Rohit","ancna",True,12)
# print(len(name))
# print(type(name))
# print(name)
# print(name[-3])
# # range
# print(name[1:4])


# Tuples are immutable so you can't append any element to it but there is a way if u still want to add something in a tuple 
# convert to list 
# let say we have tuple 
# name=("Prakhar","Rohit","ancna",True,12)
# # now we can change it to list
# listname=list(name)
# listname.append("Mohit")
# name=tuple(listname)
# print(name)


# Sets
# unordered,items unchangeable,not allow duplicate
# this_items={"banana","apple","akjcna",23,True,1,False,0}
# print(this_items)

# # len of Set
# print(len(this_items))
# print(type(this_items))

# constructor 
# name=set(("ajkf","anfk","23","akjf"))
# # print(name)

# for item in name:
#     print(item)
# print("2" in name)

# name.add("orange")
# print(name)

# lastname={"ajkfn","akjf"}
# name.update(lastname)
# print(name)

# name.remove("23")
# name.discard("23")
# name.pop()
# name.clear()
# del name
# print(name)
# set1={"anja","akjf",23}
# set2={23,3,4,4,4}
# set3=set1.union(set2)
# print(set3)

# intersection(),difference(),symetric difference

# frozenset is an immutable

# fruits=frozenset({"apple","orange"})
# print(fruits)
# print(type(fruits))




# Dictionary
# its is in the form of key:value
# ordered,changeable,not allow duplicates
# my_Dict={"name":"Ram","age":23}
# print(my_Dict)
# print(len(my_Dict))
# print(my_Dict["name"])
# print(my_Dict.get("name"))

# Assignment
# num={23,23,42,546,46,5,6,56,75,7}















# functions

# def my_function():
#     print("we are learning python")
# my_function()
# my_function()
# my_function()

# def greeting():
#     return "Hello"


# parameters
# def sum1(num1,num2):
#     return num1+num2
# # arguments
# ans=sum1(12,3)

# Default parameters
# def fun(val="ajfkn"):
#     print(val)
# fun("name")




# Keyword Arguments
# def greet(var1,var2):
#     print("I am from",var1)
#     print("you are from",var2)
    
# greet(var2="akjkjnd",var1="akljf")

# write function to change f->C;

# C=(F-32)*5/9
    

# Recursion

# def fun(n):
#     # base condition
#     if(n==0):
#         return
#     print(n)
#     fun(n-1)
# fun(6)

# Assignment
# print factorial of n
# print faboncii series
# find the sum a list element have all intergers by using recursion 
# num=[32,23,45,5,66,6,6,7,65,44,3,3,22]

    
# Assignment
# write function to add two numbers
# write function to print the table to a numbers
#  Function banao jo number ka square return kare
# reverse a list without using built-in-function
# name=["klmac","aafo",12,32,4,4,2,43,35,"sdano",True]
# check weather 45 present in a name list 
# merge two list 
# find the frequency of 89 in a list
# num=[2,4,4,64,54,65,76,76,87,89,43,54,46,565,7,2,89,89,34,89]