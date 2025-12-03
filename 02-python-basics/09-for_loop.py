my_list = [1,2,3,4,5,6,7,8,9,10]
add = 0

for number in my_list:
    print(number)
    add += number
    
print(add)

for index, number in enumerate(list(range(10, 110))):
    print(index, number)