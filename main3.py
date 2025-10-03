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


