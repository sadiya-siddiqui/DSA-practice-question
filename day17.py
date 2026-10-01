##Q1
# def first_even(s):
#     for i in s:
#         if i%2==0:
#             return i
#     return None
# result=first_even([11, 15, 7, 9, 20, 24])
# print(result)

##Q2
# def first_negative(a):
#     for i in a:
#         if i<0:
#             return i
#     return None
# result=first_negative([10, 20, 5, -8, -3, 15])
# print(result)

##Q3
# def first_vowel(s):
#     for i in s:
#         if  i in "aeiouAEIOU":
#             return i
#     return None
# result=first_vowel("python programming")
# print(result)

##Q4
# def first_greater(a, target):
#     for i in a:
#         if i >target:
#             return i
#     return None
# result=first_greater([10, 15, 30, 25, 40], 20)
# print(result)

##Q5
# def number_exists(a, target):
#     for i in a:
#         if i ==target:
#             return True
        
#     return False
# result=number_exists([10, 20, 30, 40], 60)
# print(result)

##Q6
# def find_index(a, target):
#     for i in range (len(a)):
#         if a[i] ==target:
#             return i
#     return None
# result=find_index([10, 20, 30, 40], 30)
# print(result)

##Q7
# def last_even(s):
#     last=None
#     for i in s:
#         if i%2==0:
#             last=i
#             continue

#     return last
# result=last_even([10, 15, 20, 25, 30, 35])
# print(result)

# ##Q8
# def neg_count(a):
#     count=0
#     for i in a:
#         if i <0:
#             break
#         count+=1
#     return count
# result=neg_count([10, 20, 30, -5, 40, 50])
# print(result)

##Q9
# def sum_neg(a):
#     total=0
#     for i in a:
#         if i<0:
#             break
#         total=total+i
#     return total
# result=sum_neg([10, 20, 30, -5, 40])
# print(result)

##Q10
# def pos_even(a):
#     for i in a:
#         if i>0 and i%2==0:
#             return i
# result=pos_even([-5, -2, 0, 7, 9, 12, 20])
# print(result)

##Q11
# def repe_element(a):
#     seen=set()
#     for i in a:
#         if i in seen:
#             return i
#         else:
#             seen.add(i)
# result=repe_element([10, 20, 30, 40, 20, 50])
# print(result)

##Q12
# def unique_element(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#              freq[i]=1
#     for i in a:
#          if freq[i]==1:           
#              return i
#     return None
        
# result=unique_element([10, 20, 30, 20, 10, 40])
# print(result)
            
##Q13
# def longest_word(a):
#     word=a.split()
#     longest=""
#     for i in word:
#         if len(i)>len(longest):
#             longest=i

#     return longest
# result=longest_word("Python is very powerful programming language")
# print(result)

##Q14
# def smallest_word(a):
#     word=a.split()
#     smallest=word[0]
#     for i in word:
#         if len(i)<len(smallest):
#             smallest=i

#     return smallest
# result=smallest_word("Python is very powerful programming language")
# print(result)

##Q15
def analyze (a):
    freq={}
    word=a.split()
    longest=""
    shortest_word=word[0]
    first_vowel=None
    first_digit=None
    word_count=len(word)
    for i in word:
        if len(i)>len(longest):
            longest=i
    for i in word:
        if len(i)<len(shortest_word):
              shortest_word=i
    for i in a:
        if first_vowel is None and i  in "aeiouAEIOU":
            first_vowel=i
        if first_digit is None and i.isdigit():
            first_digit=i
    for i in a:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1
    
    return {"word_count": word_count,
        "longest_word": longest,
        "shortest_word": shortest_word,
        "first_vowel": first_vowel,
        "first_digit": first_digit,
        "frequency": freq
}
result=analyze("Python 2026 is powerful")
print(result)
