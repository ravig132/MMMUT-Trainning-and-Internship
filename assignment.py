marks = [29,26,78,42,54,64,74,32,65,98,39]

# larget number
print("Largest value of the list is :",max(marks))

# smallest number
print("Smallest value of the list is :",min(marks))

totalMarks = 0
marks.sort(reverse=True)
print(marks[0:5])
for i in range(0,5):
    totalMarks+=marks[i]

print("The average of the top 5 student is : ",totalMarks/5)

# marks of three student of from list copy of list
newList = marks[0:3]
print(newList)


# marks greater than 50 
for i in range(len(marks)):
    if marks[i] > 50 :
        print(marks[i],end=" ")





