##Q1
# def frequency_num_digit(a):
#     freq={}
#     while a>0:
#         digit=a%10
#         if digit in freq:
#                 freq[digit]+=1
#         else:
#                 freq[digit]=1
#         a=a//10
#     return freq
# result=frequency_num_digit(112233445566)
# print(result)

##Q2
# def frequency_num_digit(a):
#     freq={}
#     max_freq=0
#     max_digit=0
#     while a>0:
#         digit=a%10
#         if digit in freq:
#                 freq[digit]+=1
#         else:
#                 freq[digit]=1
#         a=a//10
#         for i in freq:
#           if freq[i]>max_freq:
#             max_freq=freq[i]
#             max_digit=i
#     return max_digit,max_freq
# result=frequency_num_digit(583525583)
# print(result)

##Q3
# def second_frequent_num(a):
#     first_freq=0
#     second_freq=0
#     freq={}
#     first_digit=0
#     second_digit=0
#     while a>0:
#         digit=a%10
#         if digit in freq:
#             freq[digit]+=1
#         else:
#             freq[digit]=1
#         a=a//10
#     for i in freq:
#             if freq[i]>first_freq:
#                 second_freq=first_freq
#                 second_digit=first_digit
#                 first_freq=freq[i]
#                 first_digit=i
#             elif freq[i]>second_freq:
#                 second_freq=freq[i]
#                 second_digit=i
#     return "freq=",second_freq ,"digit is=",second_digit     
# result=second_frequent_num(1122333444555)
# print(result)
        

##Q4
# def sum_unique(a):
#     sum=0
#     seen=set()
#     count=0
#     while a>0:
#         digit=a%10
#         if digit in seen:
#                 count+=1
#         else:
#             sum+=digit
#             seen.add(digit)
#         a=a//10
#     return count ,sum
# result=sum_unique(1122334455667)
# print(result)


# ##Q5                                it give output with list
# def first_duplicate(a):
#     seen=set()
#     duplicat=[]
#     while a>0:
#         digit=a%10
#         if digit in seen:
#                 if digit not in duplicat:
#                      duplicat.append(digit)       
#         else:
#             seen.add(digit)
#         a=a//10
#     return duplicat
# result=first_duplicate(583525741)
# print(result)

                                          ##Q5 or  it give output without list
# def first_duplicate(a):
#     seen=set()

#     while a>0:
#         digit=a%10

#         if digit in seen:
#             return digit
#         else:
#             seen.add(digit)

#         a=a//10

#     return None
# result=first_duplicate(583525741)
# print(result)



##Q6                                    give output in descending order
# def remove_repete(a):
#     seen=set()
#     duplicat=[]
#     while a>0:
#         digit=a%10
#         if digit in seen:
#                 if digit not in duplicat:
#                      duplicat.append(digit)       
#         else:
#             seen.add(digit)
#         a=a//10
#     return duplicat
# result=remove_repete(112233445566)
# print(result)
 

                                          ##Q6 or give answer in ascending order

# def remove_repeated(a):
#     seen=set()
#     unique=[]

#     while a>0:
#         digit=a%10

#         if digit not in seen:
#             seen.add(digit)
#             unique.append(digit)

#         a=a//10

#     return unique[::-1]
# result=remove_repeated(112233445566)
# print(result)

##Q7
# def duplicate_digit(a):
#     duplicate=[]
#     seen=set()
#     count=0
#     second_duplicate=[]
#     while a>0:
#         digit=a%10
#         if digit in seen:
#             duplicate.append(digit)
#         else:
#             seen.add(digit)
#         a=a//10
#     for i in duplicate:
#         count+=1
#         if count==2:
#             second_duplicate.append(i)
       
#     return i
# result=duplicate_digit(583525741)
# print(result)

##Q8
# def repet_digit(a):
#     digit_repete=0
#     max_freq=0
#     freq={}
#     while a>0:
#         digit=a%10
#         if digit in freq:
#             freq[digit]+=1
#         else:
#             freq[digit]=1
#         a=a//10
#     for i in freq:
#         if freq[i]>max_freq:
#             max_freq=freq[i]
#             digit_repete=i
#     return "repete digit=",digit_repete,"max_digit",max_freq
# result=repet_digit(1122334455667788)
# print(result)

##Q9
# def count_freq(a):
#     count=0
#     freq={}
#     while a>0:
#         digit=a%10
#         if digit in freq:
#             freq[digit]+=1
#         else:
#             freq[digit]=1
#         a=a//10
#     for i in freq:
#         if freq[i]==2:
#             count+=1
#     return count
# result=count_freq(112233445566778899)
# print(result)

##Q10
# def min_freq(a):
#     freq={}
#     min_freqency=float('inf')
#     min_digit=None
#     while a>0:
#         digit=a%10
#         if digit in freq:
#             freq[digit]+=1
#         else:
#             freq[digit]=1
#         a=a//10
#     for i in freq:
#         if freq[i]<min_freqency:
#             min_freqency=freq[i]
#             min_digit=i
#     return min_digit
# result=min_freq(1112233445556)
# print(result)

##Q11
# def distinct_unique(a):
#     seen=set()
#     while a>0:
#         digit=a%10
#         seen.add(digit)
#         a=a//10
#     return len(seen)
# result=distinct_unique(583525741)
# print(result)

# ##Q13
# def digit_not_repete(a):
#     duplicate=[]
#     seen=set()
#     while a>0:
#         digit=a%10
#         if digit in seen:
#             if digit not in duplicate:
#                 duplicate.append(digit)
#         else:
#             seen.add(digit)
#         a=a//10
#     return sorted(duplicate)
# result=digit_not_repete(583525741223)
# print(result)

##Q14
# def difference(a):
#     highest_freq=-1
#     lowest_freq=float('inf')
#     freq={}
#     while a>0:
#         digit=a%10
#         if digit in freq:
#             freq[digit]+=1
#         else:
#             freq[digit]=1
#         a=a//10
#     for i in freq:
#         if freq[i]>highest_freq:
#             highest_freq=freq[i]
#         if freq[i]<lowest_freq:
#             lowest_freq=freq[i]
#     differ=highest_freq-lowest_freq
#     return differ
# result=difference(583525741)
# print(result)    

# ##Q15
# def min_freq(a):
#     freq={}
#     digits=[]
#     while a>0:
#         digits.append(a%10)
#         a=a//10
#     digits.reverse()
#     for digit in digits:
#          if digit in freq:
#                     freq[digit]+=1
#          else:
#                     freq[digit]=1

#          if freq[digit]==2:
#             return digit
# result=min_freq(583525741)
# print(result)