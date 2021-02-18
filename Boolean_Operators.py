#This project will be going over Boolean Operators aka True and False
#__________________________________________________________________________________________#

#Ex. 1 This will return the value of True. Notice True is not in quotations. This returns the value of True as the Boolean type. 

print(True)

#__________________________________________________________________________________________#

#Ex 2. You can compare two objects to each other to receive a true or false statement. 

print(5 == 5)
    #This will return true

print(5 ==4)
    #This will return false

#_____________________________________________________________________________________________#

#Ex. 3 This will compare two strings with each other using "is" and " is not". 

print(5 is 5) 
    #This will print true

print(5 is not 4)
    #This will print true


#_____________________________________________________________________________________________#

#Ex. 4 This example will show you what will happen when you compare two different variables of the same value. We will be comparing the boolean True value vs. the String True value

print(True == "True")
    #This will return false because they are not the same since they are two different variable types. The next example will show you how to make the two the same. 

print("True" == str(True))
    #This will return True because we changed the boolean value to True to a string variable type and compared it with the string variable value of true.


#____________________________________________________________________________________________#

#Ex. 5 This example will go over the "is not" value (!=) comparing two variables. 

print(5 != 6)
    #This will return the value of true.

print('Ken' != 'Bob')
    #This will return the value of true. 