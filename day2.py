##Q13
# a=input("enter string")
# count=0
# for i in a:
#     if i in"aeiouAEIOU":
#         count+=1
# print(count)

##Q14    jb character ko individual batana ho 
# string=str(input("enter string:"))
# char=str(input("enter charcater:"))
# for i in string:
#     if i in char:
#      print(string.find(char))

##Q14
# string=str(input("enter string:"))
# char=str(input("enter charcater:"))
# if char in string:
#     print("found")
# else:
#     print("not found")

##Q15
# string=str(input("enter string:"))
# char=str(input("enter char:"))
# if char in string:
#     print(string.count(char)," times it comes")
# else:
#     print("not comes")
    

##Q16
# a=input("enter string:")
# vowel=0
# consonant=0
# for i in a:
#     if i in "aeiouAEIOU":
#         vowel+=1
#     elif i.isalpha():
#         consonant+=1
# print("vowel",vowel)
# print("consonants",consonant) 

##Q22
# a=input("enter string:")
# if a.find(" "):
#     print(a.replace(" ",""))

##Q23
# a = input("enter string:")

# for i in a:
#     if a.count(i) == 1:
#         break
#     else:
#         print("no unique charcter")

# print(i)

##Q24
# a=input("enter:")
# seen=""
# for i in a:
#     if i not in  seen:
#         seen+=i
# print(seen)
  

##Q25
# a=input("enter:")
# b=input("enter:")
# a_sorted=sorted(a)
# b_sorted=sorted(b)
# if a_sorted==b_sorted:
#     print("anagram")
# else:
#     print("not anagram")
