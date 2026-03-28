students =[]
name = input("Enter the name of the student: ")
age = int(input("Enter the age of the student: "))
data = [name, age ]
students.append(data)
print("*****All data of students: ****")
for i in students:
    print("name is", i[0])
    print("age is", i [1])

