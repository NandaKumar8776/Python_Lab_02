### Python Lab 2



## REQUIREMENT 1

from operator import indexOf
nmpoer
# Empty lists to store the length of the n_grams and the associated word.   
n_gram_length = []
n_gram_words = []

# Loop that stores the word and its n gram length in two lists but in the same index locations.
for line in indexes:
    # Splitting the lines by '|' to seperate.
    words,_ = line.split('|')
    n_gram_splitted_words = words.split('_')
    n_gram_length.append(len(n_gram_splitted_words))
    n_gram_words.append(words)

# Getting highest n_gram word by its associated index location where the n gram length is located.
max_n_gram = max(n_gram_length)

max_n_gram_word = n_gram_words[n_gram_length.index(max_n_gram)]

# Printing the n_gram sixe and the first associated word.
print(str(max_n_gram) + " " + max_n_gram_word)
print()



## REQUIREMENT 2 (Modifying same code further)

# Creating empty lists for the ID's as an addition, from the previous requirement code.
n_gram_length = []
n_gram_words = []
IDs_list = []
IDs_length = []

# Additionally, splitting the ID's by ',' and using rstrip to remove hanging '\n'.
for line in indexes:
    
    words,IDs = line.split('|')
    this_ID = IDs.split(',')
    (this_ID)[-1] =  (this_ID)[-1].rstrip("\n")

    IDs_list.append(this_ID)
    IDs_length.append(len(this_ID))

    n_gram_length.append(len(n_gram_splitted_words))
    n_gram_words.append(words)

# Finding the max length, its associated word by indexing with the same index number as the other list.
max_n_gram = max(n_gram_length)
max_n_gram_word = n_gram_words[n_gram_length.index(max_n_gram)]
max_IDs_Length = max(IDs_length)
max_IDs_Length_word = n_gram_words[IDs_length.index(max_IDs_Length)]
max_IDs_ID = IDs_list[IDs_length.index(max_IDs_Length)]

# To print the length of the n_gram, the word and its ID's.
print(str(max_IDs_Length)+" "+max_IDs_Length_word, end = " ")
print(max_IDs_ID)
print()

# Requirement 3

with open('NounsData.txt', "r", encoding="utf-8") as f:
    data = f.readlines()
    
# Takes the data line by line
for k in data:
    
    # Splits by '|' to get the ID and its associated definition.
    k_split = k.split('|')
    ID = k_split[0]
    
    # Checks if the ID in the particular line is an ID that defines the word 'head' by comparing it's ID's. 
    if ID in max_IDs_ID:
        print(str(ID) +" "+ k_split[-1], end="")


