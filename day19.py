##Q1
# def analyze_numbers(numbers):
#     total=0
#     even_count=0
#     largest=numbers[0]
#     for i in numbers:
#         if i%2==0:
#             even_count+=1
#         if i>largest:
#             largest=i
#         total+=i
#     return total, even_count, largest
# result=analyze_numbers([12,5,8,21,10])
# print(result)


##Q2
# def analyze_students(students):
#     highest_marks=students[0]["marks"]
#     highest_name=students[0]["name"]
#     avg_marks=0
#     total=0
#     for i in students:
#         if i["marks"]>highest_marks:
#             highest_marks=i["marks"]
#             highest_name=i["name"]
#         total+=i["marks"]
#     avg_marks=total/len(students)
#     return highest_marks,highest_name,avg_marks
# result=analyze_students([
#     {"name": "Ali", "marks": 85},
#     {"name": "Sara", "marks": 92},
#     {"name": "John", "marks": 78}
# ])
# print(result)
                                          ##  day 19 part 1
# ##Q1
# def sum_list(a):
#     sum=0
#     for i in a:
#         sum+=i
#     return sum

# result=sum_list([10, 20, 30, 40])
# print(result)

##Q2
# def count_elements(a):
#     count=0
#     for i in a:
#         count+=1
#     return count
# result=count_elements([10,20,30,40,50])
# print(result)

##Q3
# def largest_num(a):
#     largest=a[0]
#     for i in a:
#         if i>=largest:
#             largest=i
#     return largest
# result=largest_num([10,50,20,90,40])
# print(result)

##Q4
# def find_smallest(a):
#     smallest=a[0]
#     for i in a:
#         if i<smallest:
#             smallest=i
#     return smallest
# result=find_smallest([10,50,5,20,-2])
# print(result)


##Q5
# def calculate_average(a):
#     avg=0
#     total=0
#     for i in a:
#         total+=i
#     avg=total/len(a)
#     return avg
# result=calculate_average([10,20,30,40])
# print(result)

##Q6
# def count_even(a):
#     even=0
#     for i in a:
#         if i%2==0:
#             even+=1
#     return even
# result=count_even([10, 15, 20, 25, 30, 35])
# print(result)

##Q7
# def count_odd(a):
#     odd=0
#     for i in a:
#         if i%2!=0:
#             odd+=1
#     return odd
# result=count_odd([10, 15, 20, 25, 30, 35])
# print(result)

##Q8
# def positive_numbers(a):
#     pos=[]
#     for i in a:
#         if i>=0:
#             pos.append(i)
#     return pos
# result=positive_numbers([10, -5, 20, -8, 30, 0])
# print(result)

##Q9
# def first_negative(a):
#     for i in a:
#         if i<0:
#             return i
#     return None
# result=first_negative([10, 20, 5, -8, -3, 15])
# print(result)

##Q10
# def analyze_list(a):
#     total=0
#     largest=a[0]
#     smallest=a[0]
#     avg=0
#     even_count=0
#     odd_count=0
#     for i in a:
#         total+=i
#         if i>=largest:
#             largest=i
#         elif i<smallest:
#             smallest=i

#         if i%2==0:
#             even_count+=1
#         else:
#             odd_count+=1
#     avg=total/len(a)
#     return total,largest,smallest,avg,even_count,odd_count
# result=analyze_list([10, 15, 20, 25, 30])
# print(result)

##                       part 2
##Q1
# def number_exists(a, target):
#     for i in a:
#         if i==target:
#             return True
#     return False
# result=number_exists([10, 20, 30, 40],target = 90)
# print(result)

##Q2
# def find_index(a, target):
    
#     for i in range (len(a)):
#         if a[i]==target:
#             return i
#     return None

# result=find_index([10, 20, 30, 40],
# target = 30)
# print(result)
            
##Q3
# def find_even(a):
#     even=[]
#     for i in a:
#         if i%2==0:
#             even.append(i)
#     return even
# result=find_even([10, 15, 20, 25, 30, 35])
# print(result)        

##Q4
# def greater_number(a,target):
#     greater_list=[]
#     for i in a:
#         if i>target:
#             greater_list.append(i)
#     return greater_list
# result=greater_number([10, 25, 5, 40, 30],target = 20)
# print(result)

#Q5
# def negative_number(a):
#     negative_list=[]
#     for i in a:
#         if i<0:
#             negative_list.append(i)
#     return negative_list
# result=negative_number([10, -5, 20, -8, 30, -2])
# print(result)

##Q6
# def first_even(a):
#     for i in a:
#         if i%2==0:
#             return i
#     return None
# result=first_even([11, 15, 7, 9, 20, 24])
# print(result)

##Q7
# def last_even(a):
#     last=None
#     for i in a:
#         if i%2==0:
#             even=i
#     return even
   
# result=last_even([10, 15, 20, 25, 30, 35])
# print(result)

##Q8
# def count_greater(a, target):
#     count=0
#     for i in a:
#         if i>target:
#             count+=1
#     return count
# result=count_greater([10, 25, 5, 40, 30],target = 20)
# print(result)

##Q9
# def find_duplicates(a):
#     seen=set()
#     duplicate=[]
#     for i in a:
#         if i in seen:
#             if i not in duplicate:
#                 duplicate.append(i)
#         else:
#             seen.add(i)
#     return duplicate
# result=find_duplicates([10, 20, 30, 20, 40, 10, 50])
# print(result)

##Q10
def analyze_list(a):
    total=0
    largest=a[0]
    smallest=a[0]
    pos_list=[]
    neg_list=[]
    avg=0
    even_count=0
    odd_count=0
    first_negative = None
    last_even=None
    for i in a:
        total+=i
        if i>=largest:
            largest=i
        elif i<smallest:
            smallest=i
        if i>=0:
            pos_list.append(i)
        if i<0:
            neg_list.append(i)
            if first_negative is None:
            
                 first_negative=i

        if i%2==0:
            last_even=i
            even_count+=1
        else:
            odd_count+=1
    avg=total/len(a)
    return  {
        "total": total,
        "average": avg,
        "largest": largest,
        "smallest": smallest,
        "positive_list": pos_list,
        "negative_list": neg_list,
        "even_count": even_count,
        "odd_count": odd_count,
        "first_negative": first_negative,
        "last_even": last_even
    }
result=analyze_list([10, -5, 20, 30, -8, 40, 15])
print(result)