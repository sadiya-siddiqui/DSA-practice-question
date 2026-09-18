# ##Q1
# a=[10,20,10,30,20,40,10]
# count=[]
# for i in a:
#       if a.count(i)>1 and i not in count:
#         count.append(i)
# print(count)

# ##Q2
#


##Q7
# a=[10,20,5,30,15]
# total=0
# for i in a:
#     total+=i
# print(total)
   
##Q8
# a=[10,20,5,30,15]
# count=[]
# for i in a:
#     if i%2!=0:
#         count.append(i)
# print(count)

#Q9
# a=[10,20,30,4,60]
# b=int(input("enter:"))
# for i in a:
#     if b in a:
#         print("present",b)
#     else:
#         print("not found")

##q10
# a=[10,20,30,40,50]
# n=len(a)
# new_list=[]
# for i in range (n-1,-1,-1):
#     new_list.append(a[i])

# print(new_list)

##Q11
# a=[10,20,30,40,50]
# b=[20,50,30,60,70]
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)


##Q12
# a=[10,30,40,20,50,60,1]
# largest=a[0]
# smallest=a[0]
# for i in a:
#     if i>largest:
#         largest=i
#     elif i<smallest:
#         smallest=i
# print("it's largest",largest)
# print("it's smallest",smallest)
