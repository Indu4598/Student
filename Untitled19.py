
# coding: utf-8

# In[ ]:




# In[ ]:

def insert(students_detail):
    name = input('Enter the name of student:')
    rollno =int(input('Enter the roll number:'))
    age=int(input('Enter the age: '))
    year=int(input('Enter the year: '))
    sem=int(input('Enter the sem: '))
    marks=float(input('Enter marks till date: '))
    
    students_detail.append({
                            'Name': name,
                            'Rollno': rollno,
                            'age':age,
                            'year': year,
                            'sem':sem,
                            'Marks till date':marks
                            })
def delete(stuents_detail):
    roll_del=int(input())
    students_details = [{k: v for k, v in d.items() if k != 'roll_del'} for d in students_detail ]
    
def display(students_detail):
    for student in students_detail:
    print('\n')
    for key, value in student.items():
        print('{0}: {1}'.format(key, value))

students_detail=[]
while i!=4:
    print("Enter the operation to be performed")
    print("1.Insert 2.Delete 3.Display 4.Exit ")
    i=int(input())
    if i==1:
        insert(students_detail)
    if i==2:
        delete(students_detail)
    if i==3:
        display(students_detail)

