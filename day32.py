# ##Q1
# def max_sum_subarray(nums,k):
#     first_sum=0
#     max_sum=0
#     first_sum=sum(nums[:k])
#     max_sum=first_sum
#     for i in range(k,len(nums)):
#         first_sum+=nums[i]
#         first_sum-=nums[i-k]
#         max_sum=max(max_sum,first_sum)
#     return max_sum
# print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))   # 9
# print(max_sum_subarray([1, 2, 3, 4, 5], 2))      # 9
# print(max_sum_subarray([5, 5, 5], 1))            # 5
# print(max_sum_subarray([2, 1, 5, 1, 3, 2], 3))   # 9
# print(max_sum_subarray([1, 2, 3, 4, 5], 2))      # 9
# print(max_sum_subarray([5, 5, 5], 1))            # 5
# print(max_sum_subarray([10, 20, 30, 40], 2))     # 70

##Q2
# def container_most_water(height):
#     left=0
#     right=len(height)-1
#     max_area=0
#     while left<right:
#         width=right-left
#         current_height=min(height[left],height[right])
#         current_area=width*current_height
#         if current_area>max_area:
#             max_area=current_area
#         if height[left]<height[right]:
#             left+=1
#         else:
#             right-=1
#     return max_area
# print(container_most_water([1,8,6,2,5,4,8,3,7]))   # 49
# print(container_most_water([1,1]))                  # 1
# print(container_most_water([4,3,2,1,4]))            # 16
# print(container_most_water([1,2,1]))                # 2

##Q3
# def three_sum(nums):
#     nums.sort()
#     result=[]
#     for i in range(len(nums)-2):
#         if i>0 and nums[i]==nums[i-1]:           # skip duplicate element of i
#             continue
#         left=i+1
#         right=len(nums)-1
#         while left<right:
#             sum=nums[i]+nums[left]+nums[right]
#             if sum==0:
#                 result.append([nums[i],nums[left],nums[right]])
#                 while left<right and nums[left]==nums[left+1]:
#                     left+=1
#                 while left <right and nums[right]==nums[right-1]:
#                         right -=1
#                 left+=1
#                 right-=1
#             elif sum<0:
#                 left+=1
#             else:
#                 right-=1
#     return result
# print(three_sum([-1,0,1,2,-1,-4]))   # [[-1,-1,2],[-1,0,1]]
# print(three_sum([0,1,1]))             # []
# print(three_sum([0,0,0]))             # [[0,0,0]]
# print(three_sum([-2,0,1,1,2]))        # [[-2,0,2],[-2,1,1]]

##Q4
def length_of_longest_substring(nums):
    left=0
    max_substring_length=0
    seen=set()
    for right in range (len(nums)):
       while nums[right] in seen:
           seen.remove(nums[left])
           left+=1
       seen.add(nums[right])
       max_substring_length=max(max_substring_length,right-left+1)
    return max_substring_length
print(length_of_longest_substring("abcabcbb"))   # 3
print(length_of_longest_substring("bbbbb"))      # 1
print(length_of_longest_substring("pwwkew"))     # 3
print(length_of_longest_substring(""))           # 0
print(length_of_longest_substring(" "))          # 1
       
