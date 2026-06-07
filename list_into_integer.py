#Convert a List of Integers to an Integer
#A Python program to convert a given list of integers to an integer. 
#For example, given [11, 2, 54], the program should assign 11254 into an integer variable

def integer(a):
  b = a.split()
  c = set(b)
  result = "".join(c)
  return result

x = input("Enter a list of integers: ")
print(integer(x))