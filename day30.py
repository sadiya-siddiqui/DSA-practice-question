##Q1
# def buy_stock_sell(prices):
#     profit=0
#     for i in range (1,len(prices)):
#         if prices[i]>prices[i-1]:
#             profit+=prices[i]-prices[i-1]
#     return profit
# result=buy_stock_sell([7, 1, 5, 3, 6, 4])
# print(result)

# ##Q2
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
# print(valid_parenthesis("()[]{}"))     # True
# print(valid_parenthesis("(]"))         # False
# print(valid_parenthesis("([)]"))       # False
# print(valid_parenthesis("{[]}"))       # True
# print(valid_parenthesis(""))           # True
# print(valid_parenthesis("("))          # False
# print(valid_parenthesis(")"))          # False
##Q3
# def contains_duplicate(nums):
#     seen=set()
#     for i in nums:
#         if i in seen:
#             return True
           
#         else:
#             seen.add(i)
#     return False 
# print(contains_duplicate([1,2,3,1]))              # True
# print(contains_duplicate([1,2,3,4]))              # False
# print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))  # True
# print(contains_duplicate([]))                     # False
# print(contains_duplicate([1]))                    # False