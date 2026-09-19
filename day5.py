                ##LISTS

#       #Q1

# a=[10,2,30,40,30,20]
# new_list=[]
# for i in a:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

##Q2
# a=[10,20,3,40,50]
# second_smallest=a[0]
# smallest=a[0]
# for i in a:
#     if i<smallest:
#         second_smallest=smallest
#         smallest=i
#     elif i<second_smallest:
#         second_smallest=i
# print(second_smallest)

##Q4
# a=[10,20,30,-5,-2,4,-5]
# pos_list=0
# neg_list=0
# for i in a:
#     if i>0:
#         pos_list+=1
#     elif i<0:
#         neg_list+=1
# print(pos_list,neg_list)

##Q5
# a=[10,3,20,50,15,70]
# even_count=0
# odd_count=0
# for i in a:
#     if i%2==0:
#         even_count+=1
#     elif i%2!=0:
#         odd_count+=1
# print(even_count,odd_count)

##Q6
# a=[10,20,30,10,40,10]
# target=10
# count=0
# for i in a:
#     if i==target:
#         count+=1
        
# print(count)

##Q7
# a=[10,25,5,40,15]
# largest=a[0]
# smallest=a[0]

# for i in a:
#     if i>largest:
#       largest=i
#     elif i<smallest:
#        smallest=i
# diff=largest-smallest
# print(diff)

##8
# a=[10,-5,20,-8,30,-2,40]
# pos_list=[]
# for i in a:
#     if i<0:
#         continue
#     elif i>=0:
#         pos_list.append(i)

# print(pos_list)

##Q9
# a=[10,20,30,10,40,20,50]
# count=[]
# for i in a:
#     if a.count(i)>1 and i not in count:
#         count.append(i)
# print(count)

##Q10
# a=[0,2,5,4,20,0,3,0,70]
# new_list=[]
# zero_count=0
# for i in a:
#     if i==0:
#         zero_count+=1
#     else:
#          new_list.append(i)

# for i in range(zero_count):
#     new_list.append(0)
# print(new_list)


##Q11
# a=[1,2,3,5,6]
# expected=1
# for i in a:
#     if i==expected:
#         expected+=1
#     else:
#         missing=expected
        #break

# print(missing)
##Q12
# a=[10,20,30,20,40,50]
# n=len(a)
# is_sorted=True
# for i in range(1,n-1):
#     if a[i]<a[i-1]:
#         is_sorted=False
#         break
# if is_sorted:
#     print("sorted")
# else:
#     print("not sorets")

##Q13
# a=[10,20,30,20,40,50,20,90]
# seen=set()
# for i in a:
#     if i in seen:
#         print(i)
#         break
#     seen.add(i)
    