                         ##Strings

##Q1
# a="programming"
# count=0
# for i in a:
#     if i in "aeiouAEIOU":
#         count+=1
# print(count)        

##Q2
# a="hello"
# freq={}
# for i in a:
#     if i in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)

##Q3
# a="python"
# n=len(a)
# new_freq=""
# for i in range(n-1,-1,-1):
#     new_freq+=(a[i])

# print(new_freq)

##Q4
# a="madam"
# rev=""
# n=len(a)
# for i in range(n-1,-1,-1):
#     rev+=a[i]
# if a==rev:
#         print("palindrome")
# else:
#         print("not a palindrom")

##Q9
# s="python is easy"
# words=s.split()

# print(len(words))

##Q10
# s="python"
# result=""
# for i in s:
#     if i in "aeiouAEIOU":
#         result+="*"
#     else:
#         result+=i
# print(result)

##Q11
# s1="listen"
# s2="silent"
# if sorted(s1)==sorted(s2):
#     print("angram")
# else:
#     print("not angram")

##Q12
# s="programming"
# result=""
# for i in s:
#     if i not in result:
#         result+=i
#     else:
#         continue
# print(result)