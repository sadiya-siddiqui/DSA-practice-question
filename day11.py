                                               ##function+list

# ##Q1
# def list_sum(a):
#     sum=0
#     for i in a:
#         sum=sum+i
#     return sum
# result=list_sum([10,20,30,40])
# print(result)

# ##Q2
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

##Q3
# def even_number(a):
#     even_list=[]
#     for i in a:
#         if i%2==0:
#             even_list.append(i)
#     return even_list
# result=even_number([10,15,20,25,30,35])
# print(result)

# ##Q4
# def odd_number(a):
#     odd_list=[]
#     for i in a:
#         if i%2!=0:
#             odd_list.append(i) 
#     return odd_list
# result=odd_number([10,15,20,25,30,35])
# print(result)


##                                            function+string
##Q5
# def count_vowels(s):
#     count=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# result=count_vowels("programming")
# print(result)

##Q6
# def count_consonants(s):
#     count=0
#     for i in s:
#         if i not in "aeiouAEIOU":
#             count+=1
#     return count
# result=count_consonants("python")
# print(result)

##Q7
# def reverse_string(s):
#     rev=""
#     n=len(s)

#     for i in range (n-1,-1,-1):
#         rev+=s[i]
#     return rev
# result=reverse_string("python")
# print(result)

##Q8
# def palindrome(s):
#     rev=""
#     n=len(s)
#     for i in range(n-1,-1,-1):
#            rev+=s[i]
#     if s==rev:
#         return True
#     else:
#          return False
# result=palindrome("madam")
# print(result)

                                                    ##function+dictionary
##Q9
# def frequency_s(a):
#     dict_fre={}
    
#     for i in a:
#         if i in dict_fre:
#             dict_fre[i]+=1
#         else:
#             dict_fre[i]=1
#     return dict_fre
# result=frequency_s([10,20,10,30,20,10])
# print(result)

# ##Q10
# def frequency_s(a):
#     dict_fre={}
    
#     for i in a:
#         if i in dict_fre:
#             dict_fre[i]+=1
#         else:
#             dict_fre[i]=1
#     return dict_fre
# result=frequency_s("programming")
# print(result)

                                   ##Function+SET
##Q11
# def remove_duplicates(a):
#     seen=set()
#     new_list=[]

#     for i in a:
#         if i not in seen:
#            seen.add(i)
#            new_list.append(i)
#     return new_list
# result=remove_duplicates([10,20,30,10,20,40,30])
# print(result)

##Q12
# def find_duplicates(a):
#     seen=set()
#     duplicate=[]
#     for i in a:
#         if i  in seen:
#            duplicate.append(i)
#         else:
#            seen.add(i)
#     return duplicate
# result=find_duplicates([10,20,30,10,20,40,30])
# print(result)


                                          ##FUNCTION+MULTIPLE LOGIC

##Q13
# def analyze_list(a):
#     largest=a[0]
#     smallest=a[0]
#     even_count=0
#     odd_count=0
#     total=0
#     for i in a:
#         if i>largest:
#             largest=i
#         elif i<smallest:
#             smallest=i
#         if i%2==0:
#             even_count+=1
#         elif i%2!=0:
#             odd_count+=1

#         total=total+i
#     return largest,smallest,even_count,odd_count,total
# result=analyze_list([10,15,20,5,30,40])
# print(result)

##Q14
# def second_largest_number(a):
#     largest=a[0]
#     second_larg=a[0]
#     for i in a:
#         if i>largest:
#             second_larg=largest
#             largest=i
#         elif i>second_larg:
#             second_larg=i
#     return second_larg
# result=second_largest_number([10,50,30,80,40,60])
# print(result)

##Q15
def analyze_list(a):
    largest=a[0]
    smallest=a[0]

    even_count=0
    odd_count=0

    positive_count=0
    negative_count=0

    dict_fre={}
    seen=set()
    duplicate=[]

    total=0
    ##largest&smallest
    for i in a:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
##even&odd count
        if i%2==0:
            even_count+=1
        elif i%2!=0:
            odd_count+=1
##pos&neg count
        if i>=0:
            positive_count+=1
        elif i<0:
            negative_count+=1
##duplicate
        if i in seen:
            if i not in duplicate:
                 duplicate.append(i) 
        else:
           seen.add(i)
## frequeny
        if i in dict_fre:
            dict_fre[i] += 1
        else:
            dict_fre[i] = 1

        total=total+i
    return largest,smallest,even_count,odd_count,positive_count,negative_count,dict_fre,duplicate,total
result=analyze_list([10,20,10,30,40,20,50,10,-5,-10])
print(result)