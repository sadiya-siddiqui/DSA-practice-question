##Q1

# def group_anagrams(string):
#     group={}
#     for i in string:
#         key="".join(sorted(i))
#         if key in group:
#             group[key].append(i)
#         else:
#             group[key]=[i]
#     return list(group.values())
# print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# # [["eat","tea","ate"], ["tan","nat"], ["bat"]]

# print(group_anagrams([""]))          # [[""]]
# print(group_anagrams(["a"]))         # [["a"]]

##Q2
def top_k_frequent(nums,k):
    freq={}
    result=[]
    for i in nums:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    sort_items=sorted(freq.items(),key=lambda x:x[1],reverse=True)
    for i in range(k):
        result.append(sort_items[i][0])
    return result
print(top_k_frequent([1,1,1,2,2,3], 2))    # [1, 2]
print(top_k_frequent([1], 1))               # [1]
print(top_k_frequent([1,2], 2))             # [1, 2]  (order alag ho sakta hai)
print(top_k_frequent([4,4,4,4,5,5], 1))     # [4]