##Q1
# def nested_list(a):
#     for i in a:
#         for j in a:
#             print(j)
    
# result=nested_list([ [10,20,30],
#     [40,50,60],
#     [70,80,90]])
# print(result)

##Q2
# def nested_sum(a):
#     total=0
#     for i in a :
#         for j in i:
#             total=total+j
#     return total
# result=nested_sum([[10,20],[30,40],[50,60]])
# print(result)

##Q3
# def largest_nested(a):
#     largest=a[0][0]
#     for i in a:
#         for j in i:
#             if j>largest:
#                 largest=j
#     return largest
# result=largest_nested([[10,50,20],
#     [30,90,40],
#     [60,70,80]])
# print(result)

##Q4
# def even_count_nested(a):
#     count=0
#     for i in a:
#         for j in i:
#             if j%2==0:
#              count+=1

#     return count
# result=even_count_nested([[10,50,20],
#     [30,90,40],
#     [60,70,80]])
# print(result)

##Q5
# def flatten_list(a):
#     new_list=[]
#     for i in a:
#         for j in i:
#             new_list.append(j)
#     return new_list
# result=flatten_list([ [10,20],
#     [30,40],
#     [50,60]])
# print(result)

# ##Q6
# def row_sum(a):
#     new_list=[]
#     for i in a:
#         row_total=0
#         for j in i:
#             row_total+=j
#         new_list.append(row_total)    
#     return new_list
# result=row_sum([ [10,20,30],
#     [40,50,60],
#     [70,80,90]])    
# print(result)
            
##Q7
# def highest_student(student):
#     highest_marks=student[0]["marks"]
#     best_student=student[0]["name"]
#     for i in student:
#          if i["marks"]>highest_marks:
#                  highest_marks=i["marks"]
#                  best_student=i["name"]
#     return best_student,highest_marks
# result=highest_student([   {"name":"Sadiya", "marks":95},
#     {"name":"Ali", "marks":70},
#     {"name":"Sara", "marks":90}])
# print(result)

##Q8
# def average_marks(student):
#     total=0
#     for i in student:
#         total+=i["marks"]
#     avg=total/len(student)
#     return avg
# result=average_marks([{"name":"Sadiya", "marks":80},
#     {"name":"Ali", "marks":70},
#     {"name":"Sara", "marks":90}])
# # print(result)

# ##Q9

# def highest_student(student):
#     passed=[]
    
#     for i in student:
#          if i["marks"]>=40:
#                 passed.append(i["name"])
#     return passed
# result=highest_student([   {"name":"Sadiya", "marks":95},
#     {"name":"Ali", "marks":23},
#     {"name":"Sara", "marks":50},
#     {"name":"simba","marks":45}
#     ])
# print(result)

###Q10

# def highest_salary(emp):
#     hightes=emp[0]["salary"]
#     name=emp[0]["name"]
#     for i in emp:
#         if i["salary"]>hightes:
#             hightes=i["salary"]
#             name=i["name"]
#     return hightes,name
# result=highest_salary([{"name":"A", "salary":50000},
#     {"name":"B", "salary":75000},
#     {"name":"C", "salary":60000},
#     {"name":"D", "salary":90000}])
# print(result)

##Q11
# def freq_list(n):
#     sfreq={}
#     for i in n:
#         if i in sfreq:
#             sfreq[i]+=1
#         else:
#             sfreq[i]=1
#     return sfreq
# result=freq_list( [10,20,10,30,20,10,40,30])
# print(result)

# ##Q12
# def group_dipartment(n):
#     groups={}
#     for i in n:
#         department=i["department"]
#         if department in groups:
#             groups[department].append(i["name"])
#         else:
#             groups[department]=[i["name"]]
           
#     return groups
# result=group_dipartment( [ {"name":"A", "department":"IT"},
#     {"name":"B", "department":"HR"},
#     {"name":"C", "department":"IT"},
#     {"name":"D", "department":"Sales"},
#     {"name":"E", "department":"HR"}])
# print(result)

##13
# def analyze(a):
#     largest=a[0]["salary"]
#     smallest=a[0]["salary"]
#     total_salary=0
#     highest_employee=a[0]["name"]
#     no_employee=0
#     for i in a:
#         salary=i["salary"]
#         total_salary+=salary
# ##largest&smallest
#         if salary>largest:
#             largest=salary
#             highest_employee=i["name"]
#         elif salary<smallest:
#             smallest=salary
#         if salary>60000:
#             no_employee+=1
#     avg=total_salary/len(a)
#     return ("largest=",largest,
#             "smallest=",smallest,
            
#             "avg=",avg,"highest_employee",highest_employee,
#             "no._of emp=",no_employee)
# result=analyze([{"name":"A","salary":50000,"age":25},
#     {"name":"B","salary":75000,"age":30},
#     {"name":"C","salary":60000,"age":28},
#     {"name":"D","salary":90000,"age":35}])
# print(result)
       
##Q14

# def analyze(student):
#     highest_avg=0
#     best_student=""
#     for i in student:   
#         total=0                        ##list
#         for mark in i["marks"] :  
#             total+=mark                 ##dictionary
#         avg=total/len(i["marks"])
#         if avg>highest_avg:
#             highest_avg=avg
#             best_student=i["name"]
#     return best_student
# result=analyze([{
#         "name": "Sadiya",
#         "marks": [80, 90, 75]
#     },
#     {
#         "name": "Ali",
#         "marks": [60, 70, 65]
#     },
#     {
#         "name": "Sara",
#         "marks": [90, 95, 92]
#     }])
# print(result)

##Q15
# def analyze_data(employee):
#     ##salary
#     highest_salary=employee[0]["salary"]
#     lowest_salary=employee[0]["salary"]
#     avg=0
#     total=0
#     count=0
#     highest_employee=employee[0]["name"]
#     skill_freq={}
#     python_employees=[]

#     for i in employee:
#         salary=i["salary"]
#         total+=salary
#         if salary>highest_salary:
#                 highest_salary=salary
#                 highest_employee=i["name"]
#         elif salary<lowest_salary:
#                 lowest_salary=salary
    
#         if salary>60000:
#               count+=1
#         for skill in i["skills"]:
#               if skill in skill_freq:
#                     skill_freq[skill]+=1
#               else:
#                     skill_freq[skill]=1

#         if "python" in i["skills"]:
#             python_employees.append(i["name"])

#     avg=total/len(employee)
#     return highest_salary,lowest_salary,avg ,count,highest_employee,skill_freq,"python_employee",python_employees
# result=analyze_data([{
#         "name": "A",
#         "department": "IT",
#         "salary": 50000,
#         "skills": ["Python", "SQL"]
#     },
#     {                                                  
#         "name": "B",
#         "department": "HR",
#         "salary": 75000,
#         "skills": ["Excel", "Communication"]
#     },
#     {
#         "name": "C",
#         "department": "IT",
#         "salary": 90000,
#         "skills": ["Python", "SQL", "Django"]
#     },
#     {
#         "name": "D",
#         "department": "Sales",
#         "salary": 60000,
#         "skills": ["Excel", "Communication"]
#     }])   
# print(result)


