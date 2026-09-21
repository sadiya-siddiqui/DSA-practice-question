##                  DICTIONARY
##Q1
# dict={
#     "rahul":85,
#     "aman":90,
#     "priya":95
# }
# print(dict)

##Q2
# dict={
#     "rahul":85,
#     "aman":90,
#     "priya":95
# }
# print(dict.keys())
# ##Q3
# dict={
#     "rahul":85,
#     "aman":90,
#     "priya":95
# }
# print(dict.values())

##Q4
# student={
#     "rahul":85,
#     "aman":90,
#     "priya":95
# }
# max_marks=0
# best_student=""
# for name,marks in student.items():
#     if marks>max_marks:
#         max_marks=marks
#         best_student=(name)
# print(max_marks,best_student)

##Q5
# s="banana"
# freq={}
# for i in s:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
##Q6
# dict_final={}
# dict1={"a":1,"b":2}
# dict2={"c":3,"d":4}
# dict_final=dict1|dict2 
# print(dict_final)

##Q7
# d={
#     'a':1,
#     'b':2,
#     'c':3
# }
# inverted={}
# for key,value in d.items():
#     inverted[value]=key
# print(inverted)

##Q8
# d={'a':1,'b':2,'c':3}
# del d['b']
# print(d)

##Q9
# student={
#     "rahul":85,
#     'aman':90,
#     'priya':95
#     }
# print(90 in student.values())

##Q10
scores = {"Rahul": 85, "Aman": 90, "Priya": 78}

sorted_score=sorted(scores.items(),key=lambda x:x[1])
print(sorted_score)