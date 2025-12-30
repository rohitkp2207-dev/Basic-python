#An operator is a symbol that performs an operation.
#Types
#1 Arithmetic operators: These are the used to perfom basic arithmetic operations like +,-,*,/,%,**,// etc.
# For : addition = +
# For : subtraction = -
# For : multiplication = *
# For : Division = /
# For : remainder = %
# For : exponential = **
# For : integer division = //

a = 20
b = 10

print("The addition is :",a+b)
print("The subtraction is :",a-b)
print("The multipication is :",a*b)
print("The division is :",a/b)
print("The remainder is :", a%b)
print("The exponential is :",a**b)
print("The integer division is :",a//b)

#Assingment operators :These operators are use to assign the value to the variable or the expressions like =, +=, -=, *=, /=, 
# %=, **=, //= .

# For : equal to =("=")
# For : addtion assigment =("+=")
# For : subtraction assigment =("-=")
# For : multiplication assigment=("*=")
# For : Division assigment =("/=") 
# For : remainder assigment =("%=")
# For : exponential assigment = ("**=")
# For : integer division assigment =("//=") 

# Logical operators: Logical operators are useful to construct compound conditions.
# |_Operator_|__Example_____|___________Meaning______________________________________|__Result_____|
# |__and_____|___x and y____|__and oprator. If x is false, it returns x,_otherwise y_|_____2_______|
# |__or______|___x or y_____|__or operator. If x is false, it returns y,otherwise x__|_____1_______|
# |__not_____|___not x______|__not operator. If x is false, it returns TRUE,otherwise              |
# |__________|______________| false__________________________________________________|___False_____|

x = 100
y = 200
print(x and y)    #will display 200
print(x or y)     #will display 100
print(not x)      #will display false

