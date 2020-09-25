# Program: Ch 4 Ex 51
# Author:  Myron Moss
# Date:    09/25/2020
# Description: Program to validate if a sentence begins with a capital letter and ends with punctuation.

import string

# take in sentence as variable
sentence = input("Enter a sentence: ")

# take words in sentence and place in array[] with split() function
word = sentence.split()[0]  # first word in array will be 0
capitalWord = word.capitalize()  # capitalize() function puts first character of a string to uppercase

# check for capital letter in first word in sentence
if word != capitalWord:
    print("This sentence does not begin with a capital letter.")
    # make the first word with a capital letter with replace() function
    sentence = sentence.replace(word, capitalWord)

# check for punctuation mark at the end of sentence
if not sentence[-1] in string.punctuation:  # -1 is the last element in array using the punctuation() function
    print("This sentence does end with punctuation.")
    # add punctuation to sentence
    sentence = sentence + '.'

print(sentence)
