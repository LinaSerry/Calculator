''' Program make a simple calculator that can add, subtract, multiply and divide using functions '''

# define functions
def add(x, y):
   """This function adds two numbers"""
   return x + y

def subtract(x, y):
   """This function subtracts two numbers"""
   return x - y

def multiply(x, y):
   """This function multiplies two numbers"""
   return x * y

def divide(x, y):
   """This function divides two numbers"""
   return x / y

def simpleInput():
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))

def listInput():
   n = 0
   myList = []
   while(n< 6):
     i = int(input("Enter a number: "))
     myList.append(i)
     n+=1
   return myList

# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Factorial")
print("6. Sum of all Consecutive numbers")
print("7. Product of all Consecutive numbers")
print("8. Sum of all even numbers")
print("9. Sum of all odd numbers")

choice = input("Enter choice(1/2/3/4/5/6/7/8/9):")


if choice == '1':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   add(num1,num2)

elif choice == '2':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   subtract(num1,num2)

elif choice == '3':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   num1 = int(input("Enter first number: "))
   num2 = int(input("Enter second number: "))
   print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
   myList = listInput()


elif choice == '6':
   myList = listInput()

elif choice == '7': 
   myList = listInput()

elif choice == '8':
   myList = listInput()

elif choice == '9':
   myList = listInput()

else:
   print("Invalid input")