##Q1
# def frequency(a):
#     freq={}
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     return freq
# result=frequency("programming")
# print(result)

##Q2
# def duplicate_element(a):
#     duplicate=[]
#     seen=set()
#     for i in a:
#         if i in seen:
#             duplicate.append(i)
#         else:
#             seen.add(i)
#     return duplicate
# result=duplicate_element("programming")
# print(result)

##Q3
# def repeted_char(a):
#     freq={}
#     new_string=""
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#          if freq[i]==1:
#              new_string+=i
             
#     return new_string
# result=repeted_char("programming")
# print(result)

##Q4
# def max_frequency(a):
#     max_freq=0
#     freq={}
#     maxx_digit=None
#     for i in a:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in a:
#         if freq[i]>max_freq:
#             max_freq=freq[i]
#             maxx_digit=i
#     return maxx_digit
# result=max_frequency("programming")
# print(result)
# ##Q5
# def min_frequency(a):
#     min_freq=float("inf")
#     freq={}
#     min_digit=None
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
# result=min_frequency("programming")
# print(result)
                                                 ##DSA

##Q1
# def two_sum(nums,target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i]+nums[j]==target:
#                 return [i,j]
# result=two_sum([2, 7, 11, 15], 9)
# print(result)

##Q2
# def buy_sell(prices):
#     profit=0
#     cheapest_price=prices[0]
#     max_profit=0
#     for i in prices:
#         if i< cheapest_price:
#             cheapest_price=i
#         else:
#                 profit=i-cheapest_price
#                 if profit>max_profit:
#                      max_profit=profit   
#     return max_profit
# result=buy_sell([7,1,5,3,6,4])
# print(result)

##Q3
def move_zeroes(nums):
    non_zero=0
  
    for i in range(len(nums)) :
        if nums[i] !=0:
            nums[non_zero],nums[i]=nums[i],nums[non_zero]
            non_zero+=1
    return nums
result=move_zeroes([0,1,0,3,12])
print(result)

##Q4          do by reverse but it solve by two pointerapproach
# def palindrome(nums):
#     rev=""
#     n=len(nums)
#     for i in range(n-1,-1,-1):
#         rev+=nums[i]
#     if nums==rev:
#             return True
#     else:
#             return False
# result=palindrome("A man, a plan, a canal: Panama")
# print(result)

                     ##or
def palindrome_two_pointer(nums):
    left=0
    right=len(nums)-1
    while left <right:
        if not nums[left].isalnum():
          
            left+=1
        elif not nums[right].isalnum():
            right-=1
        elif nums[left].lower()!=nums[right].lower():
            return False
        else:
            left+=1
            right-=1
    return True
# result=palindrome_two_pointer("A man, a plan, a canal: Panama")
# print(result)        
result=palindrome_two_pointer("race a car")
print(result)