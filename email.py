marks = []

for i in range(1, 5):
    student = int(input("Enter marks of student " + str(i) + ": "))
    marks.append(student)
print("Total marks:", sum(marks))
student_names = []
for i in range(1, 8):
    name = input("Enter name of student " + str(i) + ": ")
    student_names.append(name)
print("Student names:", student_names)

merged_list = dict(zip(student_names, marks))
print("Merged list of student names and marks:", merged_list)  

list = []
# num = int(input())
# for i in range(1,5):
num = int(input())
list.append(num)
print(list)
print("Total :", sum(list))