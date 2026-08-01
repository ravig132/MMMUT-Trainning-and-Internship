# # # # # marks = 45
# # # # # if marks>=50:
# # # # #     print ("isOk")
# # # # # else:
# # # # #     print ("isNotOk")

# # # # age = 18 
# # # # if age >= 18:
# # # #     print("Eligible for driving License")
# # # # elif age <=0:
# # # #     print("Invalid Age")
# # # # else:
# # # #     print("Not Eligible for driving License")

# # # marks = int(input("Enter your marks : "))
# # # if marks >= 90:
# # #     print("Grade A")
# # # elif marks >= 80:
# # #     print("Grade B")
# # # elif marks >= 70:
# # #     print("Grade C")
# # # elif marks >= 60:
# # #     print("Grade D")
# # # elif marks >= 50:
# # #     print("Grade E")
# # # else:
# # #     print("Grade F")


# # for i in range (1,100,2):
# #     print(i)



# x = 1
# while x<=100:
#     if x%2!=0:
#         x+=1
#         continue
#     print(x)
#     x+=1


# marks.append(66)
# marks.append("Ravi")
# # print(marks)
# name = list(("Ravi","Kavi","Bavi"))
# # print(marks[0])
# # print(marks[-1])


# #range

# if "Ravi" in marks :
#     print("Hai ye ")

# marks.insert(2,543)

# marks2 = [43,67]

# marks.extend(marks2)
# print(marks)



# marks.remove(90)

# print(marks)

# del marks[1]

# print(marks)

# marks.clear()
# print(marks)


# for i in marks:
#     print(i)


# for i in range(len(marks)):
#     print(marks[i])



# x = 0 
# while x<len(marks):
#     print(marks[x])
#     x+=1

# n = 6
# for i in range(n):
#     for j in range(0,i):
#         print("* ",end="")
#     print()
    
# rows = 6
# for i in range(1, rows):
#     print(" " * (rows - i) + " *" * i)
    

marks = [2,2,3,42,54,64,74,321,1,212,3]
print(max(marks))