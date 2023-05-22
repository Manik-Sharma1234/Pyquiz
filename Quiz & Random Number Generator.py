import random

print("|Welcome to this quiz!|")
name=input("|What is your name?| \n")
print("What is 3x2?")
print("a - 6")
print("b - 2")
print("c - 8")
choice=input("Enter the correct choice; a, b or c \n")
if choice == "a" :
  print("Correct!")
elif choice == "b" :
  print("Wrong!")
elif choice == "c" :
  print("Wrong!")
else : 
  print("Not an Option!")
  
print("Thank you for playing",name,"! \n \n \n \n \n \n \n \n \n \n")

print("|Random Number Generator|")
yes=input("Yes or no? \n")
if yes == "Yes" or "yes" or "Y" or "y" :
   print("|Random number genertator from which to which?| \n")
else :
  print("|Goodbye|")
  
  o = str
  t = str

o=input("|Enter Number One| \n") 
t=input("|Enter Number Two| \n")

co =int(o)
ct =int(t)

x = (random.randint(co,ct))
print(x)

print("\n \n \n Thank you for playing! \n Made by Manik Sharma. \n \n \n")
