                  ##                  tuple
##Q1
# a=(10,20,30,40,50)
# print(a[2])

##Q2
# a=(1,2,3)
# print(a.remove(a[0]))

##Q3
# t=("apple","banana","cherry")
# a,b,c=t
# print(t)
# print(b)
# print(c)

##Q4
# a=(1,2,3,2,4,2,5)
# print(a.count(2))
# print(a.index(2))

##Q5
# a=[10,20,30,20,40,30,40,50,90]
# b=set(a)
# print(b)

##Q6
# a={10,20,30,40,50}
# target=30
# if target in a:
#     print("present")
# else:
#     print("not present")
##Q7
# s="programing"
# a=set(s)
# print(a)
##Q8
a = [10,20,30,40,50,60]
b = [30,40,50,70,80]
c = [40,50,90,100]
d=set(a)
e=set(b)
f=set(c)
g=d.intersection(e)
h=g.intersection(f)
print(h)


##                                        sets
##Q1
# a={1,2,3,5,6}
# a.add(4)
# print(a)

# print(type(a))

##Q2
# a=[1,2,3,2,4,2,4,3,5]
# b=set(a)
# print(type(b))
# print(b)
# c=list(b)
# print(c)
# print(type(c))

##Q3
# set1={1,2,3}
# set2={3,4,5}
# set_total=set1.union(set2)
# print(set_total)

##Q4
# set1={1,2,3}
# set2={3,4,5}
# set_total=set1.intersection(set2)
# print(set_total)

##Q5
# set1={1,2,3}
# set2={3,4,5}
# set_total=set1-set2
# print(set_total)

##Q6
# a={1,2,3}
# b={1,2,3,4,5,6}
# print(a.issubset(b))