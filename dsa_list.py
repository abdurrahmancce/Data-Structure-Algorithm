# Creating a list with mixed data types
my_list = [10, 20, 30, 40, 50]

# Accessing elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Updating elements
my_list[2] = 99
print("Updated list:", my_list)

# Adding new elements
my_list.append(60)
my_list.insert(1, 15)
print("List after adding elements:", my_list)

# Removing elements
my_list.remove(40)   # removes first occurrence of 40
popped_value = my_list.pop()  # removes last element
print("List after removals:", my_list)
print("Popped value:", popped_value)

# Iterating through the list
print("Iterating through list:")
for item in my_list:
    print(item)

# Conditional logic with lists
even_numbers = [num for num in my_list if num % 2 == 0]
print("Even numbers only:", even_numbers)

# Length of list
print("Length of list:", len(my_list))
