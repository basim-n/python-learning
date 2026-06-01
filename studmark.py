# name=input("enter student name:")
# mark1=float(input("enter maths mark:"))
# mark2=float(input("enter physics mark:"))
# mark3=float(input("enter chemistry mark:"))
# total=mark1+mark2+mark3
# average=total/3
# print("\n---RESULT---")
# print("name:",name)
# print("Marks Total:",total)
# print("marks average",average)
# if average>=90:
#     print('GRADE A')
# elif average>=75:
#     print("GRADE B")
# elif average >=60:
#     print('GRADE C')
# else:
#     print('FAIL')


def print_names(students):
    for i in students:
        print(i["name"])

def find_highest_score(students):
    largest=students[0]['score']
    
    for stud in students:
         if stud["score"]>largest:
             largest=stud["score"]

    return largest

def find_top_students(students,highest):
    high_stud=[]
    for stud in students:
         if stud["score"]==highest:
             high_stud.append(stud["name"])
    return high_stud



students = [
    {"name": "Basim", "score": 85},
    {"name": "Arun", "score": 92},
    {"name": "Sneha", "score": 78},
    {"name": "Rahul", "score": 92}
]
print_names(students)




highest=find_highest_score(students)
print("largest score is",highest)


print("Students having highest mark is",find_top_students(students,highest))

