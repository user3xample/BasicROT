#!/usr/bin/env python3

#Print Out ROT output of all possibilities 
#Created by user3xample
#date:      18 may 2021
#Licence:   For education purposes only
#Use at your own risk
####


### Clear the screen
import os
os.system('cls||clear')

## header
print ("\n\n")
print("--------------------------------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------------------------------")
print("Program:     ROT Encryption Tool\n")
print("Creator:     user3xample")
print("Date:        May 2021")
print("Version:     0.1 \n")
print("Licence:     For education purposes only")
print("--------------------------------------------------------------------------------------------------------")
"""
         

"""
print("--------------------------------------------------------------------------------------------------------")
print("\n\n")

### start of program
while True:
    try:
        rotation = int(input("Please add the ROT number to use [0-26]:  ")) # collect what rotation count we want to use.
        break
    except ValueError:                      #Error catcher will loop till a number added.
        print("Please Input numbers only.")
        continue

plainText = input("\nPlease enter the plain text to encrypt: \n\n") # Collect input data from user to ROT.
plainText = plainText.lower() # This converts the text to all lower case letters.
print("\n--------------------------------------------------------------------------------------------------------\n")

cipherText = "" # this will be our encripted text


# Create our alphabets
abc = "abcdefghijklmnopqrstuvwxyz" # used again.
ROTabc = abc[rotation:26]+ abc[0:rotation] # used again.

#### Decrypt

#take our plain text and map letters to positions
i = len(plainText)
count = 0
 # this will count up till it matches the length of our plainText

while count <= i-1:
    pTxtLocation = plainText[count:count+1] #each loop selects the next letter
    
    location = abc.find(pTxtLocation) # we now have the index of the plaintext letter in abc

    if location == -1:  #this catches all plainText not in abc variable.
        MutatedText = pTxtLocation
        cipherText += MutatedText # add it our cipherText
        count =count+1

    else:
        MutatedText = ROTabc[location:location+1] # we take that index and find the matching poition
        cipherText += MutatedText # add it our cipherText
        count = count+1
        

#Data returned to user.
print( "\nOutput was set to ROT" + (str(rotation)) + " Output text:\n\n" + cipherText +"\n\n\n\n\n" )
print("--------------------------------------------------------------------------------------------------------")
print("Program Terminated\n\n\n\n\n")
