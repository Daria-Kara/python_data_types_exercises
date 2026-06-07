#Count Common Elements of 2 Lists
#A Python program that prints the number of common elements in two given lists. 
#For example, given [1, 2, 3] and [5, 1, 3], the program should print 2.

l1 = (input("Enter a list of numbers: ")).split()
l2 = (input("Enter a second list of numbers: ")).split()

common_elements = set(l1) & set(l2)
print(len(common_elements))