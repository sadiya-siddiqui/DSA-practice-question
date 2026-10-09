##Q1
# def third_largest(a):
#     first=a[0]
#     second=a[0]
#     third=a[0]
#     for i in a:
#         if i>first:
#             third=second
#             second=first
#             first=i
#         elif i>second:
#             third=second
#             second=i
#         elif i>third:
#             third=i
#     return third
# result=third_largest([12, 45, 7, 89, 34, 56, 23])
# print(result)

##Q2
# def third_smallest(a):
#     first=a[0]
#     second=a[0]
#     third=a[0]
#     for i in a:
#         if i<first:
#             third=second
#             second=first
#             first=i
#         elif i<second:
#             third=second
#             second=i
#         elif i<third:
#             third=i
#     return third
# result=third_smallest([34, 12, 56, 7, 89, 23, 45])
# print(result)

# ##Q3
# def greater_avg(a):
#     avg=0
#     total=0
#     new_list=[]
#     for i in a:
#         total+=i
#     avg=total/len(a)
#     for i in a:
#         if i>avg:
#             new_list.append(i)
#     return new_list,avg
# result=greater_avg([10, 20, 30, 40, 50])
# print(result)

##Q4
# def smaller_element(a):
#     avg=0
#     total=0
#     new_list=[]
#     for i in a:
#         total+=i
#     avg=total/len(a)
#     for i in a:
#         if i<avg:
#             new_list.append(i)
#     return new_list,avg
# result=smaller_element( [10, 20, 30, 40, 50])
# print(result)

##Q5
# def first_twice(a):
#     twice=0
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#             if freq[i]==2:   
#                  return i
# result=first_twice([5, 3, 8, 5, 2, 3])
# print(result)

##Q6
# def last_twice(a):
#     freq={}
#     for i in  a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a[::-1]:
#             if freq[i]==2:   
#                  return i
# result=last_twice([5, 3, 8, 5, 2, 3])
# print(result)

# ##Q7
# def most_freq(a):
#     freq={}
#     max_freq=0
#     max_element=None
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#         if freq[i]>max_freq:
#             max_freq=freq[i]
#             max_element=i
#     return max_element
# result=most_freq( [2, 3, 2, 5, 3, 2, 4])
# print(result)

##Q8
# def least_element(a):
#     freq={}
#     min_freq=float("inf")
#     min_element=None
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#         if freq[i]<min_freq:
#             min_freq=freq[i]
#             min_element=i
#     return min_element
# result=least_element([2, 3, 2, 5, 3, 2, 4])
# print(result)

# ##Q9
# def atleast_once(a):
#     new_list=[]
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#             if freq[i]==1:   
#                  new_list.append(i)
#     return new_list
# result=atleast_once([2, 3, 2, 5, 3, 2, 4])
# print(result)

##Q10
# def exactly_twice(a):
#     new_list = []
#     freq = {}

#     for i in a:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

#     for i in freq:
#         if freq[i] == 2:
#             new_list.append(i)

#     return new_list
# result = exactly_twice([2, 3, 2, 5, 3, 2, 4])
# print(result)

##Q11
# def common_element(a,b):
#     new_list=[]
#     for i in a:
#         if i in b:
#              new_list.append(i)
#     return new_list
# result=common_element([1, 2, 2, 3, 4],[2, 3, 3, 5, 6])
# print(result)

##Q12
# def only_first_list(a,b):
#     new_list=[]
#     for i in a:
#         if i not in b:
#              new_list.append(i)
#     return new_list
# result=only_first_list( [1, 2, 3, 4],[3, 4, 5, 6])
# print(result)

##Q13
# def only_second_list(a,b):
#     new_list=[]
#     for i in b:
#         if i not in a:
#              new_list.append(i)
#     return new_list
# result=only_second_list( [1, 2, 3, 4],[3, 4, 5, 6])
# print(result)


##Q14
# def merge_list(a,b):
#     new_list=[]
#     for i in a:
#         if i not in new_list:
#              new_list.append(i)
#     for i in b:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list
# result=merge_list( [1, 2, 3, 4],[3, 4, 5, 6])
# print(result)

##Q15

def rotate(a):
    n=len(a)
    new_list=[]
    for i in range (n-2,n):
        new_list.append(a[i])
    for i in range (0,n-2):
        new_list.append(a[i])

    return new_list
result=rotate([1, 2, 3, 4, 5])
print(result)