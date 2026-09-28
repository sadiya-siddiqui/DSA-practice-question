##Q1 list comprehension
# a = [10,20,30,40,50]
# new_list=[i*2 for i in a]
# print(new_list)

# ##Q2
# a = [10,-5,20,-8,30,-2]
# new_list=[i for i in a if i>=0]
# print(new_list)

# ##Q3
# a = [10,15,20,25,30,35]
# new_list=[i for i in a if i%2==0]
# print(new_list)

##Q4
# a = [1,2,3,4,5]
# square=[i*i for i in a]
# print(square)

##Q5
# a = [1,2,3,4,5]
# dict_number={i:i*i for i in a}
# print(dict_number)

##Q6
# a = [10,20,30,40]
# use_dic=list(map(lambda i:i+5,a))
# print(use_dic)

##Q7
# a = [10,15,20,25,30,35]
# use_filter=list(filter(lambda i:i%2==0,a))
# print(use_filter)

##Q8

# multiply=lambda a,b:a*b
# print(multiply(4,5))

##Q9
# a=[50,20,80,10,40]
# new_list=sorted(a,key=lambda x:x)
# print(new_list)

##Q10
# employees = [
#     {"name":"A", "salary":50000},
#     {"name":"B", "salary":90000},
#     {"name":"C", "salary":60000}
# ]
# new_emp=sorted(employees,key=lambda x:x["salary"])
# print(new_emp)

##Q11
# employees = [
#     {"name":"A", "salary":50000},
#     {"name":"B", "salary":90000},
#     {"name":"C", "salary":60000}
# ]
# highest_salary=sorted(employees,key=lambda x:x["salary"] ,reverse=True)
# print(highest_salary[0])

##Q12
# students = [
#     {"name":"Sadiya", "marks":85},
#     {"name":"Ali", "marks":70},
#     {"name":"Sara", "marks":95}
# ]
# student_name=[i["name"] for i in students]
# print(student_name)

# ##Q13
# students = [
#     {"name":"Sadiya", "marks":85},
#     {"name":"Ali", "marks":70},
#     {"name":"Sara", "marks":95}
# ]
## with map& filter
# marks=list(map (lambda i:i["name"],filter(lambda i:i["marks"]>=80 ,students)))
# print(marks)

##without map& filter
# marks=[i["name"] for i in students  if i["marks"]>=80]
# print(marks)

##Q14
# a=[10,-2,4,-2,4,5,7]
# ##without  map and filter
# # pos_number=[i for i in a if i>=0]
# # print(pos_number)


# ##with map&filter
# pos_number=list(map(lambda i:i,filter(lambda i:i>=0,a)))
# print(pos_number)

##Q15
employees = [
    {"name":"A", "salary":50000, "age":25},
    {"name":"B", "salary":75000, "age":30},
    {"name":"C", "salary":90000, "age":28},
    {"name":"D", "salary":60000, "age":35}
]
part1=sorted(employees,key=lambda i:i["salary"])
part2=sorted(employees,key=lambda i:i["salary"],reverse=True)
part3=[i["name"] for i in employees if i["salary"]>60000]
part4=[i["name"] for i in employees]
part5=[i["salary"] for i in employees]
analyze_emp={"ascending": part1,
    "descending": part2,
    "above_60000": part3,
    "names": part4,
    "salaries": part5}
print(analyze_emp)
