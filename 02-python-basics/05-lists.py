list_numbers = [1,2,3,4,5]
list_letters = ['a', 'e', 'i', 'o', 'u']
list_mix = [1, 'a', 2, True, [1,2,3], 5.5]
shopping_cart = ['Laptop', 'Silla gamer', 'Café']

print(type(list_mix))

# Métodos

# append
print(list_numbers)
list_numbers.append(100)
print(list_numbers)

# remove
list_numbers.remove(4)
print(list_numbers)

# count

print(list_numbers.count(2))

# copy

copy_list_numbers = list_numbers.copy()
print(copy_list_numbers)