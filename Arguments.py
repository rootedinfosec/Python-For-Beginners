#This project will go over adding arguments used in functions.

#___________________________________________________________________________________#

#Example 1 goes over adding arguments in the function to complete the printing of string sentences declared in the function (my_function). 

def my_function (str1,str2):
    print(str1)
    print(str2)


my_function("Hello World", "This is on the second Line")

#This example will print out (Hello World) on line 1 and (This is on the second Line) on line 2.

#____________________________________________________________________________________#

#Default Arguments

def print_something (name = "Someone", age = "Unknown"):
    print("My name is",name,"and my age is",age,".")

print_something ("Ken",28)

#The commas (,) in this example just means continue to print the next. So instead of concatenating the variables we can combine them together. 

#____________________________________________________________________________________#

#Default Argument Continued

def print_something (name = "Someone", age = "Unknown"):
    print("My name is",name,"and my age is",age,".")

print_something ("Ken")

#In this example in the argument we have declared a function for name (=Someone) and for age (=Unknown). If we do not declare the value for the function it will choose the 'default' 
#value for that function. This will print out (My name is Ken and my age is Unknown.)

#___________________________________________________________________________________#

#Keyword Arguments

def print_something (name = "Someone", age = "Unknown"):
    print("My name is",name,"and my age is",age,".")

print_something (age = 28)

#In arguments there is no way to skip declaring the first argument without using what is called a "Keyword Argument". In this example we used the key word for age (age =) the default value we 
#created in our function (age ="Unknown") to bypass the first argument in our function (name ="Someone"). This will print (My name is Someone and my age is 28.) 

#___________________________________________________________________________________#

#Infinite Arguments

def print_people (*people):
    for person in people:
        print("This person is", person)

print_people ("Nick", "Dan", "Jack", "Adam", "Leslie")

#How a FOR loop work is it uses an array (list) that is declared in the argument of the function (*people). It will take all of the values we call in the function and create a list called (people). 
#In this example we used the function (print_people) with the argument ("Nick", "Dan", "Jack", "Adam", "Leslie") to create 5 different print strings of the sentence (This person is "name in argument")
