#This exercise will go over dictionaries. This is how to create comma seperated values in python. This will be similar to a term with a definition. 

#_______________________________________________________________________________________#

#Ex. 1 

print ({"Name": "Ken" , "Age": "28" , "Hobby": "Coding"}['Hobby'])
    #This will print the value associated to with the term Hobby. 

#_______________________________________________________________________________________#

#Ex. 2 This example will go over how to create a variable.

greeting = "Hello my name is Ken."

print(greeting)
    #This will print the string "Hello my name is Ken." when calling the variable greeting. We can use this cariable to maniplulate the string shown in the next example. 

#________________________________________________________________________________________#

#Ex. 3 This example will be manipulating the string we created using the variable greeting.

print(greeting.split (" ")[4])
    #This will print the work Ken. We used the split function to manipulate the string to print the word located at the 5th (0,1,2,3,4) space. 

#________________________________________________________________________________________#

#Ex. 4 This example will concatenate the variable with another string. 
print(greeting + " I like to program in Python. ")
    #This will print Hello my name is Ken. I like to program in Python. This combines our declared variable with the string we added in the print function. 