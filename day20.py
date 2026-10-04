                                         ##part1
##Q1
# def reverse_list(a):
#     n=len(a)
#     new_list=[]
#     for i in range (n-1,-1,-1):
#         new_list.append(a[i])
#     return new_list
# result=reverse_list([10,20,30,40])
# print(result)

##Q2
# def second_largest(a):
#     largest=a[0]
#     second_largestes=a[0]
#     for i in a:
#         if i>largest:
#             second_largestes=largest
#             largest=i
        
#     return second_largestes
# result=second_largest([10,50,20,90,40])
# print(result)

# ##Q3
# def remove_digit(a):
#     seen=set()
#     duplicate=[]
#     for i in a:
#         if i not in seen:
#             duplicate.append(i)  
#             seen.add(i)
#     return duplicate
# result=remove_digit([10,20,10,30,20,40])
# print(result)

##Q4
# def pos_neg(a):
#     pos_count=0
#     neg_count=0
#     for i in a:
#         if i>=0:
#             pos_count+=1
#         elif i<0:
#             neg_count+=1
#     return pos_count,neg_count
# result=pos_neg([10,-5,20,-8,30,-2])
# print(result)

##Q5
# def first_duplicate(a):
#     seen=set()
#     duplicate=[]
#     for i in a:
#         if i in seen:
#             duplicate.append(i)
#             return duplicate
#         else:
#              seen.add(i)
#     return None
# result=first_duplicate([10,20,30,20,40,10])
# print(result)
        
##Q6
# def most_freq(a):
#     freq={}
#     highest_count=0
#     most_element=None
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
    
#     for i in freq:
#         if freq[i]>highest_count:
#             highest_count+=i
#         else:
#             most_element
#     return "highest frequency=",highest_count

# result=most_freq([10,20,10,30,20,10])
# print(result)

##Q7
# def evven_odd_list(a):
#     even_list=[]
#     odd_list=[]
#     for i in a:
#         if i%2==0:
#             even_list.append(i)
#         elif i%2!=0:
#             odd_list.append(i)
#     return even_list,odd_list
# result=evven_odd_list([10, 15, 20, 25, 30])
# print(result)

##Q8
# def find_missing(a):
#     for i in range (1,max(a)+1):
#         if i not in a:
#          return i
# result=find_missing([1,2,3,5])
# print(result)
        
##Q9
# def pali(a):
#     rev=""
#     n=len(a)
#     for i in range(n-1,-1,-1):
#         rev+=a[i]
#     if a==rev:
#             return True
#     else:
#             return False
        
# result=pali("madam")
# # print(result)

                                        #or
# def palindrome(a):
#     rev=""
#     n=len(a)
#     for i in range(n-1,-1,-1):
#         rev+=a[i]
#     if a==rev:
#         return True
#     else:
#         return False
# result=palindrome("python")
# print(result)
##Q10
# def analyze(a):
#     total=0
#     avg=0
#     largest=a[0]
#     smallest=a[0]
#     even_count=0
#     odd_count=0
#     pos_list=[]
#     neg_list=[]
#     for i in a:
#         total+=i
#         if i>=largest:
#             largest=i
#         elif i<smallest:
#             smallest=i
#         if i>=0:
#             pos_list.append(i)
#         elif i<0:
#             neg_list.append(i)
#         if i%2==0:
#             even_count+=1
#         elif i%2!=0:
#             odd_count+=1
#     avg=total/len(a)
#     return ("total=",total,
#             "average=",avg,
#             "largest_no.=",largest
#             ,"smallest_no.=",smallest,
#             "even_count",even_count,"odd_count=",odd_count,
#             "positive_list=",pos_list,"negative_list=",neg_list)
# result=analyze([10, -5, 20, 30, -8, 15])
# print(result)


##                            part 2
##Q1
# def indx(a,target):
#     for i in range(len(a)):
#         if a[i]==target:
#           return i
    
# result=indx([10,20,30,40],30)
# print(result)

##Q2
# def indx(a,target):
#     index=None

#     for i in range(len(a)):
#         if a[i]==target:
#             index=i
#     return index
# result=indx([10, 20, 30, 20, 40], 20)
# print(result)


##Q3
# def second_small(a):
#     second_smallest=a[0]
#     smallest=a[0]
#     for i in a:
#         if i<smallest:
#             second_smallest=smallest
#             smallest=i
#         if i<second_smallest and i>smallest:
#             second_smallest=i
#     return second_smallest
# result=second_small([10,50,5,20,-2])
# print(result)

##Q4
# def apper_target(a,target):
#     count_target=0
#     for i in a:
#         if i==target:
#             count_target+=1
#     return count_target
# result=apper_target([10,20,10,30,10,20],10)
# print(result)

##Q5
# def duplicate_ele(a):
#     duplicate=[]
#     seen=set()
#     for i in a:
#         if i in seen:
#             if i not in duplicate:
#               duplicate.append(i)
#         else:
#             seen.add(i)
#     return duplicate
# result=duplicate_ele([10, 20, 30, 20, 40, 10, 20])
# print(result)

##Q6
# def unique_ele(a):
#     new_list=[]
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#         if freq[i]==1:
#             new_list.append(i)

#     return new_list
# result=unique_ele([10, 20, 30, 20, 10, 40])
# print(result)

##Q7
# def common_element(a,b):
#       new_list=[]
#       for i in a:
#             if i in b:
#                   new_list.append(i)
            
#       return new_list
# result=common_element([10, 20, 30, 40],[30, 40, 50, 60])
# print(result)


##Q8
# def merge_lists(a,b):
#     new_list=[]
#     for i in a:
#             if i not  in new_list:
#                   new_list.append(i)
#     for i in b:
#           if i not in new_list:
#                 new_list.append(i)      
#     return new_list
# result=merge_lists([10, 20, 30],[20, 30, 40, 50])
# print(result)

##Q9
# def rotate(a):
#     first_ele=a[0]
#     new_list=[]
#     n=len(a)
#     for i in range (1,n):
#         new_list.append(a[i])
#     new_list.append(first_ele)
#     return new_list
# result=rotate([10, 20, 30, 40])
# print(result)


##Q10
def analyze(a):
    total=0
    avg=0
    largest=a[0]
    smallest=a[0]
    second_largest=a[0]
    second_smallest=a[0]
    even_count=0
    odd_count=0
    pos_count=0
    neg_count=0
    duplicate=[]
    seen=set()
    unique=[]
    freq={}
    for i in a:
        total+=i
        if i>largest:
            second_largest=largest
            largest=i
            
        elif i>second_largest and i<largest:
                second_largest=i
        if i<smallest:
            second_smallest=smallest
            smallest=i
        elif i > smallest and i < second_smallest:
                second_smallest=i
            
        if i>0:
            pos_count+=1
        elif i<0:
            neg_count+=1
        if i%2==0:
            even_count+=1
        elif i%2!=0:
            odd_count+=1
          ##duplicate elements  
        if i in seen:
            if i not in duplicate:
               duplicate.append(i)
        else:
            seen.add(i)
            ##unique elements
      
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for i in freq:
        if freq[i]==1:
            unique.append(i)


    avg=total/len(a)
    return {"total=":total,
            "average=":avg,
            "largest_no.=":largest
            ,"smallest_no.=":smallest,
            "even_count":even_count,
            "odd_count=":odd_count,
            "positive_count=":pos_count,
            "negative_count=":neg_count,
            "second_largest=":second_largest,
            "second_smallest=":second_smallest,
            "duplicate=":duplicate,
            "unique=":unique}
result=analyze([10, 20, 10, -5, 30, 20, -5, 40])
print(result)