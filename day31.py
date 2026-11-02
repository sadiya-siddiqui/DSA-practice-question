##Q1                                        or 1 way of doing this question 
# def is_anagram(nums1,nums2):
#     if len(nums1)!=len(nums2):
#         return False
    
#     freq1={}
#     freq2={}
#     for ch in nums1:
#         if ch in freq1:
#             freq1[ch]+=1
#         else:
#             freq1[ch]=1
#     for ch in nums2:
#         if ch in freq2:
#            freq2[ch]+=1
#         else:
#             freq2[ch]=1
#     return freq1==freq2
# print(is_anagram("anagram", "nagaram")) 
# print(is_anagram("rat", "car"))    # False
# print(is_anagram("aab", "abb"))    # False
# print(is_anagram("", ""))          # True
# print(is_anagram("a", "b"))        # False
# print(is_anagram("ab", "abc"))     # False

##                     or 2 way of doing this question 
# def is_anagram(s,t):
#     freq={}
#     for ch in s:
#         if ch in freq:
#             freq[ch]+=1
#         else:
#             freq[ch]=1

#     for ch in t:
#         if ch in freq:
#             freq[ch]-=1
#         else:
#             freq[ch]=-1
#     for val in freq.values():
#         if val!=0:
#             return False
#     return True
# print(is_anagram("anagram", "nagaram"))   # True
# print(is_anagram("rat", "car"))           # False
# print(is_anagram("aab", "abb"))           # False
# print(is_anagram("", ""))                 # True
# print(is_anagram("a", "b"))               # False
# print(is_anagram("ab", "abc"))            # False
# ##                                      or 3 way of doing this question 


# def is_anagram(s,n):
#     if len(s)!=len(n):
#         return False
#     else:
#         return sorted(s)==sorted(n)
# print(is_anagram("anagram", "nagaram"))   # True
# print(is_anagram("rat", "car"))           # False
# print(is_anagram("aab", "abb"))           # False
# print(is_anagram("", ""))                 # True
# print(is_anagram("a", "b"))               # False
# print(is_anagram("ab", "abc"))            # False

##Q2

def two_sum_sorted(nums,target):
    i=0
    j=len(nums)-1

    while   i<j:
        current_sum=nums[i]+nums[j]
        if current_sum==target:
            return [i+1,j+1]
        elif current_sum<target:
            i+=1
        else:
            j-=1
    
print(two_sum_sorted([2, 7, 11, 15], 9))    # [1, 2]
print(two_sum_sorted([2, 3, 4], 6))         # [1, 3]
print(two_sum_sorted([-1, 0], -1))          # [1, 2]
print(two_sum_sorted([1, 2, 3, 4, 5], 9))   # [4, 5]
