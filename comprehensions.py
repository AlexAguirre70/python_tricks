# Use a list comprehension to create a list of the numbers from 1 to 100 (including 100). <br><br>
one_hundred = [x for x in range(1,101)]
print(one_hundred)
# Use a dictionary comprehension to count the length of each word in a sentence.<br>
sentence= "The quick brown fox jumped over the fence." 
list_dict={word:len(word) for word in sentence.split()}
print(list_dict)
# output: {'The': 3, 'quick': 5, 'brown': 5, 'fox': 3, 'jumped': 6, 'over': 4, 'the': 3, 'fence.': 6}