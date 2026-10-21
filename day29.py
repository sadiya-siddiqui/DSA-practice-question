# ##Q1                                 merge sorted array
# def merge_sorted(nums1,nums2):
#     i=0
#     j=0
#     merge_array_new=[]
#     while i<len(nums1) and j<len(nums2):
#         if nums1[i]<nums2[j]:
#             merge_array_new.append(nums1[i])
#             i+=1
#         else:
#             merge_array_new.append(nums2[j])
#             j+=1
#     while i<len(nums1):
#         merge_array_new.append(nums1[i])
#         i+=1
#     while j<len(nums2):
#             merge_array_new.append(nums2[j])
#             j+=1
#     return merge_array_new
# result=merge_sorted([1, 3, 5], [2, 4, 6])
# print(result)

##Q2
# def majority_element(nums):
#     freq={}    
#     for i in nums:
#         if i in freq:
#             freq[i]+=1
#         else:
#             freq[i]=1
#     for i in freq:
#        if freq[i]>len(nums)//2:
#          return i
#     return None
# result = majority_element([2, 2, 1, 1, 1, 2, 2])
# print(result)

##Q3     compeleted
# def valid_parenthesis(nums):
#     stack=[]
#     match = {')': '(', ']': '[', '}': '{'}
#     for ch in nums:
#         if ch in "{[(":
#             stack.append(ch)
#         else:
#             if not  stack:
#                 return False
#             if stack.pop()!=match[ch]:
#                 return False
#     return len(stack)==0
# print(valid_parenthesis("()"))         # True
# print(valid_parenthesis("()[]{}"))  

    
##Q4
# def max_subarray(nums):
#     current_sum=nums[0]
#     max_sum=nums[0]
#     for i in range (1,len(nums)):
#         current_sum=max(nums[i],current_sum+nums[i])
#         max_sum=max(max_sum,current_sum)
#     return current_sum,max_sum
# result=max_subarray( [-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(result)
