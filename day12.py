# ##Q1
# def calculate_total(a,b,c):
#     return a+b+c
# result=calculate_total(10,20,30)
# print(result)

# ##Q2
# def maximum(a,b):
#     if a>b:
#            return a
#     else:
#           return b
# result=maximum(7,3)
# print(result)

##Q3
# def minmum(a,b,c):
#     if a<b and a<c:
#            return a
#     elif b<a and b<c:
#           return b
#     else:
#           return c   
# result=minmum(10,3,20)
# print(result)

# ##Q4
# def check_even_odd(n):
#     if n%2==0:
#         return "even"
#     elif n%2!=0:
#         return "odd"

#     return n
# result=check_even_odd(24)
# print(result)

##Q5
# def greet(n="sadiya"):
#     print("hello",n)

#     return n
# greet()

##Q6
# def count_greater(a,target):
#     count=0
#     for i in a:
#         if i>target:
#             count+=1
#     return count
# result=count_greater([10,25,5,40,15,50],20)
# print(result)

# ##Q7
# def count_greater(a,target):
#     new_list=[]
#     for i in a:
#         if i>target:
#             new_list.append(i)
#     return new_list
# result=count_greater([10,25,5,40,15,50],20)
# print(result)

##Q8
# def count_character(a,target):
#     count=0
#     for i in a:
#         if i == target:
#             count+=1
#     return count
# result=count_character("programming","g")
# print(result)

##Q9
# def count_frequency(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# result=count_frequency("hello")
# print(result)

##Q10

# def count_frequency(a):
#     freq = {}

#     for i in a:
#         if i in freq:
#             freq[i] += 1
#         else:
#             freq[i] = 1

#     return freq


# def most_frequent(a):
#     freq = count_frequency(a)

#     most_char = ""
#     highest_count = 0

#     for i in freq:
#         if freq[i] > highest_count:
#             highest_count = freq[i]
#             most_char = i

#     return most_char


# result = most_frequent("programming")
# print(result)
##Q11
# def unique_values(a):
#     seen=set()
#     new_list=[]
#     for i in a:
#         if i not in seen:
#             seen.add(i)
#             new_list.append(i)
#     return new_list
# result=unique_values([10,20,10,30,20,40])
# print(result)

##Q12
# def common_element(a,b):
#     common=[]
#     for i in a:
#        if i in b:
#           common.append(i)
#     return common
# result=common_element([10,20,30,40,50],[30,40,50,60,70])
# print(result)

##Q13
# def analyze(a):
#     largest=a[0]
#     smallest=a[0]
#     calculate_total=0
#     for i in a:
#         if i>largest:
#             largest=i
#         elif i<smallest:
#             smallest=i

#         calculate_total=calculate_total+i
#     return largest,smallest,calculate_total
# result=analyze([30,20,10])
# print(result)

# ##Q14
# def analyze(marks):

#     highest=marks[0]
#     lowest=marks[0]
#     avg=0
#     total=0
#     passed_count=0
#     for i in marks:
#         total=total+i
#         if i>highest:
#             highest=i
#         elif i<lowest:
#             lowest=i

#         if i>=40:
#             passed_count+=1
#         avg=total/len(marks)
#     return "total=",total,"highest=",highest,"lowest=",lowest,"average=",avg,"passed_count=",passed_count
# result=analyze([75,82,65,90,55])
# print(result)

##Q15
def analyze(a):
    largest=a[0]
    smallest=a[0]
    total=0
    pos_count=0
    neg_count=0
    even_ccount=0
    odd_count=0
    duplicates=[]
    freq={}
    seen=set()
    avg=0
    for i in a:
        total=total+i
##largest&smallest
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
##even&odd
        if i%2==0:
            even_ccount+=1
        elif i%2!=0:
            odd_count+=1
##pos&neg
        if i>=0:
            pos_count+=1
        elif i<0:
            neg_count+=1
#duplicate
        if i in seen:
            if i not in duplicates:
                duplicates.append(i)
        else:
                seen.add(i)
##frequency
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    avg=total/len(a)
    return ("largest=",largest,
            "smallest=",smallest,
            "even_count",even_ccount,
            "odd_count",odd_count,
            "pos_count=",pos_count,
            "neg_count=",neg_count,
            "freq=",freq,
            "duplicate=",duplicates,
            "total=",total,
            "avg=",avg)
result=analyze([10,20,10,30,40,20,50,10,-5,-10])
print(result)
       

        