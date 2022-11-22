# Write a lambda function to sort a list of tuples in ascending order according to the number in the second position of each tuple.<br><br>
unsorted= [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 
#Sorted list of tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]
sorted_lst =sorted (unsorted, key=lambda a:a[1])
print(sorted_lst)
# Write a lambda function to cube every element of a list.<br>
org_list=[3,6,9,2] 
# List after lambda function: [27,216,729,8]<br><br>
cubed = list(map(lambda x: x**3, org_list))
print(cubed)

# Write a lambda function to determine whether a number is even or odd (the function should return True or False), and then use the function and a list comprehension to create a new list of booleans, where even numbers are True and odd numbers are False.<br><br>
# Input list: [3,6,9,2] List after lambda function and list comprehension: [False, True, False, True]<br><br>

is_even = lambda a: True if a %2 ==0 else False
boolean_even_odd = [is_even(b) for b in [3,6,9,2]]
print(boolean_even_odd)