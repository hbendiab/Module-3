# Module 3: String Manipulation and Loops Practice working with string methods and loops in Python.
#EX 1 : STRING METHODS 
# TODO: Create a string variable with a sentence
sentence = "    j'apprends à coder sur Python.   "
print(sentence)

sentence_1 = "J'ai dit \"Bonjour\""
print(sentence)

upper_sentence = sentence.upper()
print(upper_sentence)

# TODO: Convert the string to lowercase
lower_sentence = sentence.lower()
print(lower_sentence)

# TODO: Capitalize the first letter of each word
majuscule_mots = sentence.title()
print(majuscule_mots)
# TODO: Replace a word in the string
replace = sentence.replace("Python","Java")
print(replace)
# TODO: Split the string into a list of words
separation = sentence.split()
print(separation)

# TODO: Join the list of words back into a string using a different separator
join_sentence = "-".join(separation)
print(join_sentence)

# TODO: Find the position of a specific word in the string

position = sentence.find("coder")
print(position)

# TODO: Check if the string starts with a specific word : .stratswith("mot") renvoie TRUE ou FALSE 

print(sentence.startswith("Python"))

# TODO: Remove leading and trailing whitespace from a string : enlever espace au début et à la fin d'une chaîne .strip()

clean_sentence = sentence.strip()
print("Avant :", repr(sentence))
print("Après :", repr(clean_sentence))

## Exercise 3: For Loops

# TODO: Create a list of numbers 
# ajouter ou supprimer des nombres dans cette liste (append, remove, pop)
numbers = [1,2,3,4,5,6,7,8,9]
print(numbers)

numbers = list(range(1,6))
print(numbers)

# TODO: Use a for loop to print each number in the list : boucle for sert à afficher chaque élément de ta liste numbers, un par un

for num in numbers:
    print(num)

# TODO: Use a for loop with enumerate() to print both index and value : enumerate permet de connaitre la position et la valeur des numeros 
for index, value in enumerate(numbers, start=0):
    print(f"Index{index} : {value}")

for index, value in enumerate(numbers, start=1):
    print(f"Index{index} : {value}")

# TODO: Create a dictionary and use a for loop to print all keys and values
vegetables = {
"tomate" : "rouge", "artichaut" : "vert", "courgette" : "vert foncé", "salade" : "vert clair" 
}
for key, value in vegetables.items():
    print(f"{key} : {value}")

# TODO: Use a for loop with range() to print numbers from 1 to 10

numbers = range(1, 34)
print(numbers)

#numbers = list(range(1, 34))print(numbers) print (numbers)#

city = ["paris","marseille","lyon","toulon"]
for i in city: 
    print(i) 


# exemple : 

    
# TODO: Use list comprehension to create a new list of squares of numbers



# TODO: Use a nested for loop to create a multiplication table (up to 5x5)


#exercice 4 - While loops 
# TODO: Use a while loop to print numbers from 1 to 10

# TODO: Create a guessing game using a while loop
# (generate a random number and let the user guess until correct)

# TODO: Use a while loop to calculate the factorial of a number

# TODO: Implement a simple calculator using a while loop
# (continue calculating until the user chooses to exit)

#exercice 5 - Combining Strings and Loops 
# TODO: Create a function that counts the occurrence of each vowel in a string

# TODO: Implement a simple Caesar cipher (shift each letter by a fixed amount)

# TODO: Create a function that generates the NATO phonetic alphabet representation of a word

# TODO: Implement a function that checks if a string is a palindrome

# Test each function with sample inputs and print the results