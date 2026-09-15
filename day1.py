# #Q1
# name=input("enter name :")
# age=int(input("enter age :"))
# print(name,age)

# #  Q2
# a=int(input("enter no.1st :"))
# b=int(input("enter no. 2nd :"))
# print("sum:",a+b)

# #Q3
# a=int(input("enter no.1st :"))
# if a%2==0:
#     print(a,"is even")
# else:
#     print(a,"is odd")

# #Q4
# a=int(input("enter no. :"))
# if a >0:
#     print("positive")
# elif a<0:
#     print("negative")
# else:
#     print("zero")

# #Q5
# a=int(input("enter no.1st :"))
# b=int(input("enter no. 2nd :"))
# if a>b:
#     print(a,"a is largest")
# elif b>a:
#     print("b is largest")
# else:
#     print("both are equal")

##Q6  only largest 
# a=int(input("enter no.1st :"))
# b=int(input("enter no. 2nd :"))
# c=int(input("enter no.3rd :"))
# if a>=b and a>=c:
#     print("a is largest")
# elif b>=a and b>=c:
#     print("b is largest")
# else:
#     print("c is largest")

## Q7     if they want largest no.then do this 
# a=int(input("enter no.1st :"))
# b=int(input("enter no. 2nd :"))
# c=int(input("enter no.3rd :"))
# if a== b ==c:
#     print("all are equal")
# elif a==b and a>c:
#     print("a and b is largest")
# elif b == c and b > a:
#     print("b and c are largest")
# elif a == c and a > b:
#     print("a and c are largest")
# elif a>=b and a>=c:
#     print("a is largest")
# elif b>=a and b>=c:
#     print("b is largest")
# else:
#     print("c is largest")

##Q8
# marks=int(input("enter marks:"))
# if marks < 0 or marks > 100:
#     print("invalid no.")
# elif 90<=marks>=100:
#     print("a grade")
# elif 75<=marks>=90:
#     print("b grade")
# elif 60<=marks>=75:
#     print("c grade")
# elif 40<=marks>=60:
#     print("d grade")
# else:
#     print("fail")

##Q9            calculator
# a=int(input("enter no.1st :"))
# operator=str(input("enter operator :"))
# b=int(input("enter no.2nd :"))
# if operator=="+":
#     print(a+b)
# elif operator=="-":
#     print(a-b)
# elif operator=="*":
#     print(a*b)
# elif operator=="/":
#     print(a/b)
# elif operator=="//":
#     print(a//b)
# elif operator=="%":
#     print(a%b)
# elif operator=="**":
#     print(a**b)
# else:
#     print("none")

##Q10 login system
# name=input("enter username :")
# password=input("enter password :")
# if name=="sadiya" and password=="1234":
#     print("loginsuccesfully")
# elif name=="sadiya" and password!="1234":
#     print("name is correct but password wrong")
# elif name!="sadiya" and password=="1234":
#     print("name is wrong ")
# else:
#     print("invalid username and password")


##Q11
# a=int(input("enter the no. :"))
# if  a%3==0 and a%5==0:
#     print("divisible by both ")
# elif a%5==0:
#     print("divisible by 5")
# elif a%3==0:
#     print("divisible by 3 ")
# else:
#     print("neither of both ")
##Q12
# age=int(input("enter age:"))
# if age <0:
#     print("invalid age ")
# elif age<=12:
#     print("child")
# elif age<=19:
#     print("teenager")
# elif age<=59:
#     print("adult")
# else:
#     print("senoir")

##Q13
# a=int(input("enter no.:"))
# if a==0:
#     print("zero")
# elif a%2==0 and a>0:
#     print("positive even")
# elif a%2!=0 and a>0:
#     print("positive odd")
# elif a%2==0 and a<0:
#     print("negative even")
# elif a%2!=0 and a<0:
#     print("negative odd")

##Q14
# a=int(input("enter year:"))
# if a%400==0 or (a%4==0 and a%100!=0):
#     print("leap year")
# else:
#     print("not a leap year")
##Q15
# a = input("Enter password: ")

# if len(a) >= 8 and a == "python123":
#     print("Valid")
# else:
#     print("Invalid")