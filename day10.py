##Q1
# def hello():
#     print("hello python")
# hello()

# ##Q2
# def greet(name):
#     print("hello",name)
# greet("sadiya")


##  Q3
# def total_sum(a,b):
#     return a+b
# total_sum(2,3)

# ##Q4
# def even_odd(a):
#     if a%2==0:
#         print("even")
#     else:
#         print("odd")
# even_odd(95)

##Q5

# def largest_number(a):
#     largest=a[0]
#     for i in a:
#         if i>largest:
#             largest=i
#     return largest
# result=largest_number([10,20,30,40,506])
# print(result)

##  Q6
# def smallest_number(a):
#     smallest=a[0]
#     for i in a:
#         if i<smallest:
#             smallest=i
#     return smallest
# result=smallest_number([10,20,30,40,506])
# print(result)

##Q7
# def count_vowels(s):
#     count=0
#     for i in s:
#         if i in "aeiouAEIOU":
#             count+=1
#     return count
# result=count_vowels("programming") 
# print(result)   

# ##Q8
# def reverse_string(s):
    
#     n=len(s)
#     rev=""
#     for i in range(n-1,-1,-1):
#         rev+=s[i]
#     return rev
# result=reverse_string("python")
# print(result)

##Q9
# def palindrom_number(s):
#     n=len(s)
#     rev=""
#     for i in range(n-1,-1,-1):
#             rev+=s[i]
   
#     if s==rev:
#           return "palindrome"
#     else:
#           return "not a aplindrome"
# result=palindrom_number("madam")
# print(result)

#  Q10

# def remove_duplicates(a):
#     seen = set()
#     result = []
#     for i in a:
#         if i not in seen:
#             seen.add(i)
#             result.append(i)
#     return result

# a = [10, 20, 10, 30, 20, 40]
# print(remove_duplicates(a))  # Output: [10, 20, 30, 40]

##Q11
# def freq_func(a):
#     freq={}
#     for i in (a):
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# a=[10,20,10,30,90,10]
# print(freq_func(a))

##Q12
def toat_number(a):
    largest=a[0]
    smallest=a[0]
    even=0
    odd=0
    for i in a:
        if i>largest:
            largest=i
        elif i<smallest:
            smallest=i
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1
    return largest,smallest,even,odd
result=toat_number([10,15,20,5,30])
print(result)