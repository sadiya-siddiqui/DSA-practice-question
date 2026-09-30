##Q1
# def print_char_all(a):
#     for i in a:
#         print(i)
# result=print_char_all("python")
# print(result)

##Q2
# def count_char(a):
#     count=0
#     for i in a :
#         count+=1
#     return count
# result=count_char("python")
# print(result)

##Q3
# def count_vowel (a):
#     count=0
#     for i in a:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# result=count_vowel("programming")
# print(result)

##Q4
# def count_consonant (a):
#     count=0
#     for i in a:
#         if i.isalpha() and i not in "aeiouAEIOU":
#             count+=1
#     return count
# result=count_consonant("programming")
# print(result)

##Q5
# def rev_char(a):
#     n=len(a)
#     rev=""
#     for i in a:
#         rev=i+rev
#     return rev
# result=rev_char("python")
# print(result)

##Q6
# def palindrome_num(a):
#     rev=""
#     for i in a:
#         rev=i+rev
#     if rev==a:
#             return True
#     else:
#             return False
# result=palindrome_num("madam")
# print(result)

##                           or short version
# def palindrome_num(a):
#     rev=""
#     for i in a:
#         rev=i+rev
#     return rev==a
# result=palindrome_num("madam")
# print(result)

##Q7
# def count_character(s, target):
#     count=0
#     for i in s:
#         if i==target:
#             count+=1
#     return count
# result=count_character("programming", "r")
# print(result)

##Q8
# def count_frequency(s):
#     freq={}
#     for i in s:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# result=count_frequency("hello")
# print(result)

##Q9
# def count_letters_digits(s):
#     count_letter=0
#     count_digit=0
#     for i in s:
#         if i.isalpha():
#             count_letter+=1
#         elif i.isdigit():
#             count_digit+=1
#     return count_digit,count_letter
# result=count_letters_digits("python1234abc")
# print(result)

##Q10
# def remove_spaces(s):
#     spac=""
#     for i in s:
#         if i.strip():
#             spac+=i
#     return spac
# result=remove_spaces("python1234asd")
# print(result)


                              ##or
# def remove_spaces(s):
#     result = ""

#     for i in s:
#         if not i.isspace():
#             result += i

#     return result


##Q11
# def non_repeting(s):
#     repe={}
#     for i in s:
#         if i in repe:
#             repe[i]+=1
#         else:
#             repe[i]=1
#     for i in s:
#         if repe[i]==1:
#             return i
#     return repe
# result=non_repeting("aabbbsbba")
# print(result)

##Q12
# def repeting(s):
#     seen=set()
#     duplicate=[]
#     for i in s:
#         if i in seen:
#             if i not in duplicate:
#                 duplicate.append(i)
#         else:
#             seen.add(i)
        
#     return duplicate
# result=non_repeting("programming")
# print(result)

##Q13
# def duplicate_remove(s):
#     seen=set()
#     duplicate=""
#     for i in s:
#         if i not in seen:
#             seen.add(i)
#             duplicate+=i   

#     return duplicate
# result=duplicate_remove("programming")
# print(result)

##Q14
# def most_frequent(s):
#     freq={}
#     for i in s:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     most_char=""
#     highest_count=0
#     for i in freq:
#         if freq[i]>highest_count:
#             highest_count=freq[i]
#             most_char=i
#     return most_char
# result=most_frequent("programming")
# print(result)

##  Q15
def analyze_string(s):
    count_letter=0
    count_digit=0
    space=0
    vowel=0
    constant=0
    freq={}
    for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
        if i.isdigit():
            count_digit+=1
        elif i.isalpha():
            count_letter+=1
            if i in "aeiouAEIOU":
                vowel+=1
            else:
                constant+=1
        elif i.isspace():
            space+=1
    n=len(s)
    
    return count_letter,count_digit,constant,vowel,space,n
result=analyze_string("Hello World 2026!")
print(result)


