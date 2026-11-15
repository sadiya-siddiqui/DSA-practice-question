##Q1
def product_except_self(nums):
    left=1
    right=1
    n=len(nums)
    new_list=[1]*len(nums)            ##same length ki list bani h 

    ##left passs
    for i in range (n):
        new_list[i]=left
        left=left*nums[i]
    ##right passs
    for i in range(n-1,-1,-1):
        new_list[i]*=right
        right=right* nums[i]
    return new_list
print(product_except_self([1, 2, 3, 4]))    # [24, 12, 8, 6]
print(product_except_self([-1, 1, 0, -3, 3]))  # [0, 0, 9, 0, 0]
print(product_except_self([2, 3]))          # [3, 2]
print(product_except_self([1]))             # [1]  (single element)

