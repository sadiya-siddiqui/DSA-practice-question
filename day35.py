##Q1                     leet code 704
# def binary_search(nums,target):
#     left=0
#     right=len(nums)-1
#     while left<=right:
#         mid=(left+right)//2
#         if nums[mid]==target:
#             return mid                                   
#         elif nums[mid]<=target:
#             left=mid+1
#         else:
#             right=mid-1
#     return -1
# print(binary_search([-1,0,3,5,9,12], 9))    # 4
# print(binary_search([-1,0,3,5,9,12], 2))    # -1
# print(binary_search([5], 5))                # 0
# print(binary_search([5], 3))                # -1
  
## why binary search
# 1. Binary Search O(log n):
#    Har step pe search space AADHA ho jaata hai. n → n/2 → n/4 → ... → 1.
#    Steps = log₂(n).

# 2. while left <= right:
#    Kyunki jab left == right ho, tab EK element bacha hota hai.
#    Agar left < right likhein, to woh element MISS ho jayega.

# 3. Array sorted:
#    Binary Search MID pe jaata hai aur decide karta hai target LEFT mein hai ya RIGHT mein.
#    Ye decision sirf tab sahi hai jab array SORTED ho.

##Q2 Search Insert Position (LeetCode 35)
# def search_insert(nums,target):
#     left=0
#     right=len(nums)-1
#     while left<=right:
#         mid=(left+right)//2
#         if nums[mid] ==target:
#               return mid 
#         elif nums[mid] <target:
#             left=mid+1
#         else:
#             right=mid-1
#     return left
# print(search_insert([1,3,5,6], 5))    # 2
# print(search_insert([1,3,5,6], 2))    # 1
# print(search_insert([1,3,5,6], 7))    # 4
# print(search_insert([1,3,5,6], 0))    # 0
