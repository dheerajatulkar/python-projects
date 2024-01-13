#list and dictionary practice program

num = int(input("Enter a number of student: "))
student_data = []
for i in range(num):
  data = {}
  marks=[]
  name = input("Enter name of student: ")
  roll = int(input("Enter roll number: "))
  for j in range(5):
    mark = int(input(f"Enter the marks of {j+1}: "))
    marks.append(mark)
  data["name"] = name
  data['roll']=roll
  data["marks"]=marks  
  student_data.append(data)

for stu in student_data:
  print(f"the name is {stu['name']} and the roll number is {stu['roll']}")
  print(f"the total marks are {sum(stu['marks'])}")
  