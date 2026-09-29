##Q1
# type error because in this one digit is int and second will be string

##Q2
# a = 10
# b = "20"

# print(a + int(b))

# ##Q3

# try:
#     a = int(input("Enter number: "))
#     print("valid  no.",a)
# except ValueError:
#    print("invalid no.")

##Q4
# try:
#     a = 10
#     b = 0
#     divide=a/b
#     print(divide)
# except ZeroDivisionError:
#     divide= "can't divide by zero"
#     print(divide)

##Q5
# try:
#     a = [10,20,30]
#     index=int(input("enter index:"))
#     print(a[index])
# except IndexError:
#     print("invalid index")
# except ValueError:
#     print("Please enter a number")

##Q6
# try:
#     student = {
#     "name": "Sadiya",
#     "marks": 90
# }
#     print(student["age"])
# except KeyError:
#     print("key not found")

##Q7
# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter another number: "))
#     print(a / b)
# except ValueError:
#     print("invalid value")
# except ZeroDivisionError:
#     print("can't divide by zero")

##Q8
# try:
#      a = int(input("Enter number: "))

# except ValueError:
#      print("invaild no.")
# else:
#      print("valid no.")
##Q9
# try:
#     a=str(input("enter no."))
#     b=4
#     print(a+b)
# except TypeError:
#     print("invalid value")
# finally :
#     print("finished")

##Q10
# def divide_no(a,b):
#     try:
#         result=a/b
        
#     except ZeroDivisionError:
#         return "cannot divide by zero"
    
#     return result
# result=divide_no(4,9)
# print(result)

##Q11
# def get_element(a, index):
#     try:
#         return a[index]
#     except IndexError:
#         return"invalid index"

# result=get_element([10,20,30], 1)
# print(result)

##Q12
# def get_marks(student, name):

#     try:
#         return student[name]

#     except KeyError:
#         return "Student not found"


# students = {
#     "Sadiya": 90,
#     "Ali": 75,
#     "Sara": 95
# }

# result = get_marks(students, "Sadiya")
# print(result)

#Q13
# def check_age(age):
#     if age<0:
#         raise ValueError("age can't be negative")
#     elif age<18:
#         return "minor"
#     elif age>=18:
#         return "adult"
# result=check_age(-1)
# print(result)
  
##Q14
# def calculate_average(a):
    
#    try:
#         total = 0
#         for i in a:
#             total += i

#         average = total / len(a)

#         return average
#    except ZeroDivisionError:
#        return "Cannot calculate average of empty list"

# result = calculate_average([])
# print(result)

##Q15

# def analyze_numbers(a):
#      total=0   
#      count=0
#      invalid=[]
#      for i in a:
#         if isinstance(i,(int,float)):
#             total+=i
#             count+=1
#         else:
#                 invalid.append(i)
#      try:
#             avg=total/count
#      except ZeroDivisionError:
#           avg=0
#      return     total,count,avg,invalid
# result=analyze_numbers([10, 20, "30", 40, 0, 50,"hello", "python"])
# print(result)
       

