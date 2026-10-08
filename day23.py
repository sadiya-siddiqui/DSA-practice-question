##Q1
# def sum_digit(a):
#     position=1
#     total=0
#     while a>0:
#         digit=a%10
#         if position==2 or position==3 or position==5 or position==7:
#             total+=digit
#         position+=1
#         a=a//10
#     return total
# result=sum_digit(58374621)
# print(result)    

##Q2

# def sum_odd(a):
#     postion=1
#     total_product=1
#     while a>0:
#         digit=a%10
#         if postion%2!=0:
#             total_product*=digit
#         postion+=1
#         a=a//10
#     return total_product
# result=sum_odd(58374621)
# print(result)

##Q3
# def largest_even(a):
#     max_even=-1
#     while a>0:
#         digit=a%10
       
#         if digit%2==0:
#             if digit >max_even:
#                 max_even=digit
#         a=a//10
#     return max_even 
# result=largest_even(58374621)
# print(result)

##Q4
# def smallest_odd(a):
#     min_odd=float('inf')
#     while a>0:
#         digit=a%10
#         if digit%2!=0:
#             if digit< min_odd:
#                 min_odd=digit
#         a=a//10
#     return min_odd
# result=smallest_odd(58374621)
# print(result)

##Q5
# def greater_digit(a):
#     count=0
#     while a>0:
#         digit=a%10
#         if digit>5:
#                count+=1
#         a=a//10
#     return count
# result=greater_digit(58374621)
# print(result)

##Q6
# def count_divisible(a):
#     count=0
#     while a>0:
#         digit=a%10
#         if digit%3==0:
#             count+=1
#         a=a//10
#     return count
# result=count_divisible(58374621)
# print(result)

##Q7
# def sum_digits(a):
   
#     total=0
#     while a>0:
#         digit=a%10
#         if digit in(2,3,5,7):
#             total+=digit
       
#         a=a//10
#     return total
# result=sum_digits(58374621)
# print(result)

##Q8
# def sum_digits(a):
#     total=1
#     while a>0:
#         digit=a%10
#         if digit not  in(2,3,5,7):
#             total*=digit
       
#         a=a//10
#     return total
# result=sum_digits(58374621)
# print(result)

##Q9
# def all_even(a):
#     while a>0:
#         digit=a%10
#         if digit%2==0:
#             return False
#         a=a//10
#     return True
# result=all_even(58374621)
# print(result)

##Q10
# def all_odd(a):
#     while a>0:
#         digit=a%10
#         if digit%2!=0:
#             return True
#         a=a//10
#     return False
# result=all_odd(246)
# print(result)

