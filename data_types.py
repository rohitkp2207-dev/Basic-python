#Datatypes
#A datatypes represents the type of data stored into a variable or memory. In python there are various built-in datatypes,
#  also user can create the datatypes which are called User-defined datatypes

# BUIT-TN datatypes  :
# 1. NONTYPE 
# In python,the "NonType" datatype represent an object that does not contain any value

# 2. NUMERIC TYPES 
# The numeric types represent numbers. There are three sub types:
# int , float , complex

#int : The int datatype represent an integer number.

a = 200
print(type(a))
b = -38
print(type(b))
c = 0
print(type(c))

#All have same output that the class of the data is int.

#float : The float datatype represents the floating value.

num = 9.8 
print(type(num))

#complex : This datatype represents the type of complex numbers.

num1 = 2.5 + 2.5J
num2 = 3.0 - 0.5J
sum = num1 + num2
print("The sum is :", sum)

# 3. BOOL DATATYPE : The bool datatype represents the boolean values.

A = 10
B = 20
print(A>B)
print(A==B)
print(A<B)

# 4. str : This datatype represent string data .  A string is the group of character

str = "Welcome"
print(type(str))

# 5. list datatype 
# list is the  group of element which stores different types of elements.

list = [10, -20, 15, 5, "Vijay", "Ajay"]
print(list)
print(type(list))

# 6. tuple datatype 
# A tuple is similar to a list, can store different tyoe sof elements, but it can't modify. we cannot do any changes in tuple.

tuple = (10, 20, "Vijay", "Ajay")
print(tuple)
print(type(tuple))

# 7. Set datatype
# To create a set, we should enter the elements seprated by commas inside curly braces{}.

s = {10,20,30,40,50,}
print(s)
print(type(s))
