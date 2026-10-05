                               ##part1
##Q1
# def find_index(a,target):

#     for i in range (len(a)):
#         if a[i]==target:
#             return i
#     return -1
# result=find_index([10,20,30,40,50],30)
# print(result)

##Q1
# def prime_number(a):
#     for i in range(2,a):
#         if a%i==0:
#           return "not prime"
#         else:
#            i+=1
#     return "prime"
# result=prime_number(12)
# print(result)

##Q2
# def count_factor(a):
#     factor_count=0
#     for i in range(1,a+1):
#         if a%i==0:
#             factor_count+=1
#     return factor_count
# result=count_factor(12)
# print(result)

##Q3
# def sum_digit(a):
#    digit=0
#    sum=0
#    while a>0:
#         digit=a%10
#         sum+=digit
#         a=a//10

#    return sum
# result=sum_digit(12345)
# print(result)

##Q4
# def reverse_number(a):
#     last_digit=0
#     remaining_num=0
#     rev=0
#     while a>0:
#         last_digit=a%10
#         rev=rev*10+last_digit
#         a=a//10
#     return rev
# result=reverse_number(123)
# print(result)

##Q5
# def palindrome(a):
#     last_digit=0
#     org=a
#     rev=0
#     while a>0:
        
#         last_digit=a%10
#         rev=rev*10+last_digit
#         a=a//10
#         if org==rev:
#             return True
#         else:
#              return False


# result=palindrome(315)
# print(result)

##Q6
# def armstrong_num(a):
#     sum=0
#     org=a
#     temp=a
#     count_digit=0
#     while temp>0:
#           count_digit+=1
#           temp=temp//10
#           ##ARMSTRONG SUM

#     while a>0:
#         digit=a%10
#         sum+=digit**count_digit
#         a=a//10
#     if org==sum:
#             return "armstrong"
#     else:
#             return "not armstrong"
        
# result=armstrong_num(153)
# print(result)

##Q7
# def fact(a):
#     fact=1
    
#     for i in range(1,a+1):
#         fact=fact*i
#     return fact
# result=fact(5)
# print(result)

##Q8
# def fabonaci(a):
#     first=0
#     second=1
#     next=0
#     new_series=[]
#     for i in range(1,a+1):
#         new_series.append(first)
#         next=first+second
#         first=second
#         second=next
        
#     return new_series
# result=fabonaci(7)
# print(result)

##Q9
# def largest_digit(a):
#     largest=0
#     last_digit=0
#     while a>0:
#         last_digit=a%10
#         if last_digit>largest:
#             largest=last_digit
#         a=a//10
#     return largest
# result=largest_digit(58321)
# print(result)

##Q10
# def smallest_digit(a):
#     smallest=0
#     last_digit=0
#     smallest=a%10
#     while a>0:
#         last_digit=a%10
#         if last_digit<smallest:
#             smallest=last_digit
#         a=a//10
#     return smallest
# result=smallest_digit(58321)
# print(result)

##                           test part1
##Q1
# def sun_even_digit(a):
#     digit=0
#     sum=0
#     while a>0:
#         digit=a%10
#         if digit%2==0:
#             sum+=digit
#         a=a//10  
#     return sum
# result=sun_even_digit(58324)
# print(result)

##Q2
# def odd_digit_sum(a):
#     sum=0
#     digit=0
#     while a>0:
#         digit=a%10
#         if digit%2!=0:
#             sum+=digit
#         a=a//10
#     return sum
# result=odd_digit_sum(58324)
# print(result)

##Q3
# def largest_digit(a):
#     largest=0
#     digit=0
#     while a>0:
#         digit=a%10
#         if digit>largest:
#             largest=digit
#         a=a//10
#     return largest
# result=largest_digit(58324)
# print(result)

                                            ## part2

##Q1
# def second_largest(n):
#     largest=0
#     second_lar=0
#     digit=0
#     while n>0:
#         digit=n%10
#         if digit>largest:
#             second_lar=largest
#             largest=digit
#         elif digit>second_lar:
#                 second_lar=digit
#         n=n//10
#     return second_lar
# result=second_largest(58321)
# print(result)

##Q2
# def count_target_freq(a,target):
#     digit=0
#     count=0
#     while a>0:
#         digit=a%10
#         if digit== target:
#            count+=1
       
#         a=a//10
#     return count
# result=count_target_freq(583525,5)
# print(result)

##Q3

# def sum_even_pos(a):
#     position=0
#     digit=0
#     sum=0
#     while a>0:
#         position+=1
#         digit=a%10
        
#         if position%2==0:
#             sum+=digit

#         a=a//10
#     return sum
# result=sum_even_pos(58324)
# print(result)

##Q4
# def odd_sum_pos(a):
#     sum=0
#     position=0
#     digit=0
#     while a>0:
#         position+=1
#         digit=a%10
#         if position%2!=0:
#             sum+=digit
#         a=a//10
#     return sum
# result=odd_sum_pos(58324)
# print(result)

##Q5
# def multiple_digit(a):
#     multi=1
#     digit=0
#     while a>0:
#         digit=a%10
#         multi*=digit
#         a=a//10
#     return multi
# result=multiple_digit(58324)
# print(result)

##Q6
# def even_count(a):
#     even=0
#     digit=0

#     while a>0:
#         digit=a%10
#         if digit%2==0:
#             even+=1
#         a=a//10
#     return even
# result=even_count(5832468)
# print(result)

##Q7
# def odd_count(a):
#     odd=0
#     digit=0
#     while a>0:
#         digit=a%10
#         if digit%2!=0:
#             odd+=1
#         a=a//10
#     return odd
# result=odd_count(58324681)
# print(result)

##Q8
# def greater_count(a):
#     digit=0
#     greater=0
#     while a>0:
#         digit=a%10
#         if digit>5:
#             greater+=1
#         a=a//10
#     return greater
# result=greater_count(58374621)
# print(result)


##Q9
# def less_count(a):
#     digit=0
#     less=0
#     while a>0:
#         digit=a%10
#         if digit<5:
#             less+=1
#         a=a//10
#     return less
# result=less_count(58374621)
# print(result)

##Q10
# def greater_count(a):
#     digit=0
#     greater_sum=0
#     while a>0:
#         digit=a%10
#         if digit>5:
#             greater_sum+=digit
#         a=a//10
#     return greater_sum
# result=greater_count(58374621)
# print(result)

##Q11
# def less_count(a):
#     digit=0
#     less=0
#     while a>0:
#         digit=a%10
#         if digit<5:
#             less+=1
#         a=a//10
#     return less
# result=less_count(58374621)
# print(result)

##Q12
# def first_even_digit(a):
#     even_digit=[]
#     while a>0:
#         digit=a%10
#         even_digit.append(digit)
#         a=a//10
#     even_digit=even_digit[::-1]
#     for i in even_digit:
#             if i%2==0:
#               return i
       
#     return None
# result=first_even_digit(58371429)
# print(result)

##Q13
# def last_even_digit(a):
#     digit=0
#     while a>0:
#         digit=a%10
#         if digit%2==0:
#               return digit
#         a=a//10
#     return None
# result=last_even_digit(58371429)
# print(result)

##Q14
# def first_digit_greater(a):
#     digits=[]
#     while a>0:
#         digit=a%10
#         digits.append(digit)
#         a=a//10
#     digits=digits[::-1]
#     for i in digits:
#         if i>5:
#               return i
#         a=a//10
#     return None
# result=first_digit_greater(37492681)
# print(result)

##Q15

# def consicutive_num(a):
#     count=0
#     previous=0
#     while a>0:
#         digit=a%10
#         if digit==previous:
#             count+=1
#         previous=digit
#         a=a//10
#     return count
# result=consicutive_num(1122334455)
# print(result)

##Q16
# def consiutive_repet(a):
#     previous=None
#     current_count=0
#     max_count=0
#     max_digit=None
#     while a>0:
#         digit=a%10
#         if digit==previous:
#             current_count+=1
#         else:
#             current_count=1
#         if current_count>max_count:
#             max_count=current_count
#             max_digit=digit
#         previous=digit    
#         a=a//10
#     return max_count,max_digit
# result=consiutive_repet(122233444455)
# print(result)

        