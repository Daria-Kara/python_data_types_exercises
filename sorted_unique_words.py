#Print Sorted Unique Words
#A Python program that takes a string containing some words that are separeted with whitespace, removes all duplicate words, sorts the remaining words alphanumerically, and prints the result. 
#For example, given the string "hello world and practice makes perfect and hello world again", the program should print "again and hello makes perfect practice world".

def sorting(a):
    words = a.split()
    unique_words = set(words)
    sorted_words = sorted(unique_words)
    result = " ".join(sorted_words)
    return result

b = input("Enter a sentence: ")
print(sorting(b))