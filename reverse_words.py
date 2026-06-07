#Reverse the Words
#A Python program that takes a string containing some words that are separeted with whitespace, reverses the words in the string, and prints the result. 
#For example, given the string "hello how are you", the program should print "you are how hello".

def reverse(sentence):
   res = ""
   for word in sentence.split(" "):
        res = word + " " + res
   return res

a = str(input("Input a string: "))
print(reverse(a)) # you are how hello