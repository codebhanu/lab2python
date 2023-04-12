my_numbers=[1,2,3,4,5,6,7,8,9,10]
print("List of numbers")
print(my_numbers)
def larger_than_5(my_numbers):
    greater_than5=[]
    for i in my_numbers:
        if i>5:
            greater_than5.append(i)
    print("Elements greater than 5:")
    print(greater_than5)
       
       
       
larger_than_5(my_numbers)       