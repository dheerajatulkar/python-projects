num =  int(input("Enter a number of student: "))
data = []
subjects = ["hindi","english","maths","science","sst"]
for i in range(num):
  stu_data={}
  sub = {}
  name = input("Enter name of student: ")
  roll = int(input("Enter roll number: "))
  for j in subjects:
    mark = int(input(f"Enter the marks of {j}: "))
    sub[j]=mark
  stu_data["name"]=name
  stu_data["roll"]=roll
  stu_data['marks']=sub
  data.append(stu_data)

while True:
  roll_no = int(input("Enter the roll no check-"))
  r=0
  for item in data:
    if item['roll'] == roll_no:
      r+=1
      print(f"name = {item['name']}")
      for i,j in item['marks'].items():
        print(f"{i} = {j}")
      total = sum(item["marks"].values())
      print(f"total marks = {total} and percentage is {total*100/500}")
      break
  if(r==0):
    print("not found")