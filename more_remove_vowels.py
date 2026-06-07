#Remove Vowels
#A Python program that takes a string, makes the character lowercase, removes its vowel characters ("a", "e", "i", "o", and "u") and prints the result. 
#For example, given the string "Hello", the program should print "hll".

def remove_vowels(word):
    vowels = 'aeoiuAEIOU'
    consonants = lambda letter: letter not in vowels
    return ''.join(filter(consonants, word))

remove_vowels(str.lower(input('Enter word: ')))