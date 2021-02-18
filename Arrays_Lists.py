#This lesson will be going over Arrays also known as lists in Python.

#________________________________________________________________________#

#Ex. 1 This example will show you how to define an array. 

print(["Football", "Video Games", "Python"])
    #This will print the list ["Football", "Video Games", "Python"]. 

#________________________________________________________________________#

#Ex. 2 This example will be building off of ex. 1. Lets say in this list we only wanted to print the word Football. We would use an index with the characters [] and the number of 
#the index variable we want.

print(["Football", "Video Games", "Python"] [0])
    #This will print the index of Football. In programming the number system starts at 0,1,2,3... Since we declared the index located at the 0 position we returned the word Football.

#________________________________________________________________________#.

#Ex. 3 This example will display how to concatenated a string with an array and use an index value to complete the concatenation.  

print("I like to play " + ["Football" , "Video Games" , "Python"] [1] + ".")
    #This will return the string I like to play Video Games. We are combining the string "I like to play" with the index value located at position 1 "Video Games" and the string "."
    #If you move the "." before the index value "[1]" it will give you the error message cannot concatenate a list with a string. Moving it before the added string value of "." will 
    #Select the string value of "Video Games" from the list and add it to the concatenated string instead of generating a list this choosing the indexed value generating that error.