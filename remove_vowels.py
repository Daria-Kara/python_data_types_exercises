#Remove Vowels
#A Python program that takes a string, makes the character lowercase, removes its vowel characters ("a", "e", "i", "o", and "u") and prints the result. 
#For example, given the string "Hello", the program should print "hll".

x = str.lower(input("Input a string: "))
vowels = ("a", "e", "i", "o", "u")

for i in x:
  if i in vowels:
    x = x.replace(i, "")
print(x)