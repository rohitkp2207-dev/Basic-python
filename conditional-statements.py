# Conditional Statements : 
# if-else:
#syntax for if else statement is = if condition:
                                          # statements

# Write a program to check eligible for vote or not.

Age = int(input("Enter your Age :"))
if (Age>18):
    print("You are egible for vote")
else:
    print("You are not eligible")    


# if-elif-else:
# Write a program to check number is zero, positive, negative.

num = int(input("Enter the number :"))
if num == 0:
    print("The number is zero")
elif num > 0 :
    print("The numnber is Positive")
else:
    print("The number is Negative")


#While Loop: The statement is executed only once from top to bottom.
# The syntax for while loop is, while condition:
                                      #statement

Num = int(input("Enter the value of num :"))

while Num<=10:
    print(Num)
    Num += 1
print("End")