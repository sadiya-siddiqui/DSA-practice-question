##Q1
# def deault_argu(name="guest"):
#         return name + "hello"
# result=deault_argu("sadiya")
# print(result)

##Q2
# def calculate_price(price, discount=0):
#     discount_amount=price*discount/100
#     total=price-discount_amount
#     return total
    
# result=calculate_price(1000,20)
# print(result)

##Q3
# def max_min(a):
#     max=a[0]
#     min=a[0]
#     for i in a:
#         if i>max:
#             max=i
#         elif i<min:
#             min=i
#     return max,min
# result=max_min([10, 50, 20, 5, 40])
# print(result)

##Q4
# def analyze_numbers(a):
#     total=0
#     avg=0
#     largest=a[0]
#     smallest=a[0]
#     for i in a:
#         if i>largest:
#             largest=i
#         elif i<smallest:
#             smallest=i
#         total=total+i
#     avg=total/len(a)
#     return largest,smallest,total,avg
# result=analyze_numbers([10, 20, 30, 40])
# print(result)

##  Q5
# def sum_all(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# result=sum_all(10,20,30)
# print(result)

##Q6
# def find_largest(*args):
#     largest=args[0]
#     for i in args:
#         if i>largest:
#             largest=i
#     return largest
# result=find_largest(10, 50, 20, 90, 30)
# print(result)

##Q7
# def count_even(*args):
#     even=0
#     for i in args:
#         if i%2==0:
#             even+=1
#     return even
# result=count_even(10,15,20,25,30)
# print(result)

##Q8
# def calculate_average(*args):
#     avg=0
#     total=0
#     for i in args:
#         total=total+i
#     avg=total/len(args)
#     return avg
# result=calculate_average(10, 20, 30, 40)
# print(result)

##Q9
# def find_smallest(*args):
#     smallest=args[0]
#     for i in args:
#         if i<smallest:
#             smallest=i
#     return smallest
# result=find_smallest(10, 50, 5, 20,-2)
# print(result)

##Q10
# def analyze_args(*args):
#     total=0
#     largest=args[0]
#     smallest=args[0]
#     even_count=0
#     odd_count=0
#     for i in args:
#         if i>largest:
#             largest=i
#         elif i<smallest:
#             smallest=i
#         if i%2==0:
#             even_count+=1
#         else:
#             odd_count+=1
#         total+=i
#     return total,largest,smallest,even_count,odd_count
# result=analyze_args(10,15,20,25,30)
# print(result)

##Q11
# def show_info(**kwargs):
#     for key,value in kwargs.items():
#         print (key,":",value)
   
# result=show_info(
#     name="Sadiya",
#     age=20,
#     course="Python"
# )
# print(result)

##Q12
# def get_name(**kwargs):
    
#         return kwargs["name"]
# result=get_name(
#     name="Sadiya",
#     age=20,
#     city="Lucknow"
# )
# print(result)

##Q13
# def count_info(**kwargs):
#     return len(kwargs)
# result=count_info(
#     name="Sadiya",
#     age=20,
#     course="Python",
#     city="Lucknow"
# )
# print(result)

##Q14
# def employee_info(**kwargs):
#     return kwargs
# result=employee_info(
#     name="Sadiya",
#     salary=75000,
#     department="IT"
# )
# print(result)

##Q15
def analyze_employee(**kwargs):
    
        if kwargs["salary"]>=60000:
            is_high_salary=True
        else:
            is_high_salary=False
        if kwargs["age"]>=18:
            is_adult=True
        else:
            is_adult=False

        total_info=len(kwargs)
        return {
    "name": kwargs["name"],
    "salary": kwargs["salary"],
    "is_high_salary": is_high_salary,
    "is_adult": is_adult,
    "total_info": total_info
}
result=analyze_employee(
    name="Sadiya",
    salary=75000,
    age=22,
    department="IT",
    experience=2
)
print(result)

