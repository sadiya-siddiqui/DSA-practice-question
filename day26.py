# ##Q1
# def count_freq(a):
#     word=a.split()
#     freq={}
#     for i in word:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# result=count_freq( "python is easy and python is powerful")
# print(result)
    
##Q2
# def first_repete(a):
#     word=a.split()
#     seen=set()
#     for i in word:
#         if i in seen:
#             return i
#         else:
#             seen.add(i)
#     return None
# result=first_repete("python is easy and python is powerful")
# print(result)

##  Q3
# def non_repete(a):
#     word=a.split()
#     freq={}
#     for i in word:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in word:
#         if freq[i]==1:
#             return i
#     return None
# result=non_repete("python is easy and python is powerful")
# print(result)

##Q4
# def most_freq(a):
#     word=a.split()
#     freq={}
#     max_freq=0
#     max_digit=None
#     for i in word:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#         if freq[i]>max_freq:
#             max_freq=freq[i]
#             max_digit=i
#     return max_digit,max_freq
# result=most_freq("python is easy and python is powerful and python")
# print(result)

##Q5
# def remove_duplicate(a):
#     word=a.split()
#     seen=set()
#     new_list=[]
#     for i in word:
#         if i not  in seen:
#             new_list.append(i)
#             seen.add(i)
#     return " ".join(new_list)
# result=remove_duplicate("python is easy and python is powerful and python")
# print(result)

##Q6
# def longest_repet(a):
#     word=a.split()
#     freq={}
#     longest=""
#     for i in word:
#         if i in freq:
#             freq[i]+=1
            
#         else:
#             freq[i]=1
#     for i in freq:baki kyr 
#         if freq[i]>1:
#             if len(i)>len(longest):
#                 longest=i

#     return longest if longest else None
# result=longest_repet("python is programming and python programming is easy")
# print(result)

##Q7                 group words by first character
# def group_word_first(a):
#     word=a.split()
#     new_dict={}
   
#     for i in word:
#         first_char=i[0]
#         if first_char not in new_dict:
#             new_dict[first_char]=[]
#         new_dict[first_char].append(i)
#     return new_dict
# result=group_word_first("apple ant ball bat cat apple")
# print(result)

##Q8
# def anagrams(a,b):
#     a_low=a.lower().replace(" ","")
#     b_low=b.lower().replace(" ","")
#     if sorted(a_low)==sorted(b_low):
#         return True
#     else:
#         return False
# result=anagrams( "the eyes","they see")
# print(result)

##Q9
# def common_sentences(a,b):
#     word_a=a.split()
#     word_b=b.split()
#     seen=set()
#     new_list=[]
#     for i in word_a:
#         if i in word_b and i not in seen:
#             new_list.append(i)
#             seen.add(i)
#     return new_list
# result=common_sentences("python is easy and powerful", "python is popular and useful")
# print(result)

##Q10
# def second_highest_freq(a):
#     word=a.split()
#     freq={}
#     max_freq=0
#     max_sec_freq=0
#     max_diigi=None
#     max_sec_digit=None
#     for i in word:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#         if freq[i]>max_freq:
#             max_sec_freq=max_freq
#             max_sec_digit=max_diigi
#             max_freq=freq[i]
#             max_diigi=i
#         elif freq[i]>max_sec_freq and freq[i]<max_freq:
#             max_sec_freq=freq[i]
#             max_sec_digit=i
           
#     return max_sec_freq,max_sec_digit
# result=second_highest_freq("python is easy and python is powerful and is")
# print(result)

# ##Q11
# def replace_repeted(a):
#     freq={}
#     new_string=""
#     seen=set()
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1

#     for i in a:
#         if freq[i]>1:
#             if i in seen:
#                new_string +="*"
#             else:
#                 new_string+=i
#                 seen.add(i)
#         else:
#             new_string+=i
#     return new_string
# result=replace_repeted("programming")
# print(result)
    
##Q12
# def first_char_freq(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]>1:
#             return i
#         return None
# result=first_char_freq("abcdefa")
# print(result)

##Q13
# def length_char(a):
#     word=a.split()
#     new_list=[]
#     total=0
   
    
#     for i in word:
#          total+=len(i)
#     avg=total/len(word)
#     for i in word:

#         if len(i)>avg:
#             new_list.append(i)
#     return new_list
# result=length_char("python is easy programming")
# print(result)

##Q14
# def count_vowels(a):
#     word=a.split()
#     new_dict={}
#     count=0
#     for i in word:
#         for char in i:
#            if char in "aeiouAEIOU":
#                 count+=1
#         new_dict[i]=count
#     return new_dict
# result=count_vowels("python is easy")
# print(result)

##Q15
def word_freq(a):
    word=a.split()
    freq={}
    total_word=0
    unique_word=0
    most_freq=None
    most_freq_count=0
    total_word+=len(word)
    for i in word:
       
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    unique_word=len(freq)
    for i in freq:
        if freq[i]>most_freq_count:
            most_freq_count=freq[i]
            most_freq=i
        report = {
        "total_words": total_word,
        "unique_words": unique_word,
        "most_frequent_word": most_freq,
        "most_frequent_count": most_freq_count
    }

    return report
result = word_freq("python is easy and python is powerful")
print(result)



