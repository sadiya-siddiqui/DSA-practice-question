##Q1
# def non_repeting(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]==1:
#             return i
#     return None
# result=non_repeting( "aabbcdeff")
# print(result)

##Q2
# def last_non_repeting(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
        
#     for i in a[::-1]:
#         if freq[i]==1:
#             return i
# result=last_non_repeting("aabbcdeff")
# print(result)
        
##Q3
# def first_repeting(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]>1:
#             return i
# result=first_repeting("abcdabef")
# print(result)

##Q4
# def most_frequent(a):
#     freq={}
#     max_freq=0
#     max_digit=0
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]>max_freq:
#             max_freq=freq[i]
#             max_digit=i
#     return max_digit
# result=most_frequent("aabbbccccdd")
# print(result)

##Q5
# def least_frequent(a):
#     freq={}
#     min_freq=float("inf")
#     min_digit=0
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]<min_freq:
#             min_freq=freq[i]
#             min_digit=i
#     return min_digit
# result=least_frequent("aabbbccccd")
# print(result)

##Q6
# def remove_duplicate(a):
   
#     seen=set()
#     new_string=""
#     for i in a:
#         if i not in seen:
#             new_string+=i
#             seen.add(i)
#     return new_string
# result=remove_duplicate("programming")
# print(result)

#Q7
# def count_word(a):
#     word=a.split()
#     return len(word)
# result=count_word("Python is easy to learn")
# print(result)

##Q8
# def longest_word(a):
#     longest=""
#     word=a.split()
   
#     for i in word:
#         if len(i)>len(longest):
#             longest=i
#     return longest
# result=longest_word( "Python programming is interesting")
# print(result)

##Q9
# def shortest_word(a):
#     word=a.split()
#     shortest=word[0]  
#     for i in word:
#         if len(i)<len(shortest):
#             shortest=i
#     return shortest
# result=shortest_word("Python is very easy")
# print(result)

##Q10
# def reverse_word(a):
#     word=a.split()
#     new_list=[]
#     for words in word:
#             new_list.append(words[::-1])
#     return " ".join(new_list)

# result=reverse_word("python is easy")
# print(result)

##Q11
# def reverse_word(a):
#     word=a.split()   
#      return " ".join(word[::-1])
# result=reverse_word("python is easy")
# print(result)

##Q12
# def count_case(a):
#     upper=0
#     lower=0
#     digit=0
#     for i in a:
#         if i.isupper():
#             upper+=1
#         elif i.islower():
#             lower+=1
#         elif i.isdigit():
#             digit+=1
#     return upper,lower,digit
# result=count_case("PyThOn123")
# print(result)

##Q13
# def anagram(a,b):
#     a_low=a.lower().replace(" ","")
#     b_low=b.lower().replace(" ","")
#     if sorted(a_low)==sorted(b_low):
#         return True
#     return False
# result=anagram("listen","silent")
# print(result)

##Q14
# def common_char(a,b):
#     new_list=[]
#     for i in a:
#         if i in b:
#             if i not in new_list:
#                 new_list.append(i)
#     return new_list
# result=common_char("programming", "gaming")
# print(result)

##Q15
def second_feq(a):
    sec_freq=0
    freq={}
    first_freq=0
    first_char=None
    sec_char=None
    
    for i in a:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    for char,count in freq.items():
        if count>first_freq:
            sec_feq=first_freq
            sec_char=first_char
            first_freq=count
            first_char=char
        elif count > sec_freq and count < first_freq:
            sec_freq = count
            sec_char = char
    return sec_char,sec_feq
result=second_feq("aaabbccccdd")
print(result)


    