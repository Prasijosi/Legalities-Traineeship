# 2. Simple Calculator

num = float(input("Enter a number: "))
operator = input("Enter (+,-,*,/): ")
num2 = float(input("Enter second number: "))

#In lines of code above we simply just take input from user using input() function
#We have used float() function for two reasons.
# 1.input() takes values as string 
# 2.for divisions its better to use float

def calc(num,num2,operator):
#created a function which takes three parameters num,num2 and operator and returns the calculations
    if operator == "+":
        return num + num2
    elif operator == "-":
        return num - num2
    elif operator == "*":
        return num * num2
    elif operator == "/":
        return num / num2
    else:
        print("Invalid Operator") #if input doesnt match any of mentioned operator this is printed
        
        
#calls the calc() function and printing the results of calculations
print(calc(num,num2,operator))