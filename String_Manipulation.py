#This lab is going over variable manipulation using python

#This section will go over how to concatenate a string. 

#ex. 1 this is combining the strings Hello and Nick together to say Hello Nick.

print ("Hello, " + "Nick.")

#ex. 2 This is combining three strings This costs, 6, and bucks. This example will give you a
#error message stating intergers cannot be combined with a string. 

#print ("This costs" + 6 + "bucks")


# ex. 3 This is combining the following strings together and changing the interger to a string with the use
# of str(6). This will change the interger value to a string. 

print ("This costs " + str(6) + " bucks")

# ex. 4 This example goes how to split strings apart. This would be the opposite of concatenating the string. 
# This will display the string as an array (list) at the : character.

print ("Hello:Ken" .split(":"))

# ex. 5 This example will be similar to example 4 but uses a index value to call the result of the array
# at the index numbered value. This example will have to be run in Python IDE it will return the error value
# Cannot concatenate string and list value. If you are running this in a script you will want to use an if/else statement

print ("Hello my name is " + "Ken:John:William".split(":")[0])

