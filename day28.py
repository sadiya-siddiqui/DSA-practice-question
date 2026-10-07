# ##Q1                                   binary search
# def binary_search(nums,target):
#     i=0
#     j=len(nums)-1
#     while i<=j:
#         mid=(i+j)//2
#         if nums[mid]==target:
#             return ("that is in index=", mid)
#         elif nums[mid]<target:
#             i=mid+1
#         elif nums[mid]>target:
#             j=mid-1
#     return -1
# result=binary_search([1, 3, 5, 7, 9, 11], 7)
# print(result)

#Q2        missing number
# def missing_numbers(nums):
#     n=len(nums)
#     total_sum=n*(n+1)//2
#     actual_sum=sum(nums)
#     missing_num=total_sum-actual_sum
#     return missing_num
# print(missing_numbers([3, 0, 1]))              # 2
# print(missing_numbers([0, 1]))                 # 2
# print(missing_numbers([9,6,4,2,3,5,7,0,1]))    # 8
# print(missing_numbers([0]))                    # 1
# print(missing_numbers([1])) 


