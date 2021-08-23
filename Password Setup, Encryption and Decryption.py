#!/usr/bin/env python
# coding: utf-8

# # Validity of Password

# In[13]:


import re
def verify(): 
    UserName = input("Enter your username: ")
    p = input("Enter your password: ")
    if not re.search("[a-z]",p):
        print("Not a Valid Password \nAt least 1 letter between [a-z] ")
    elif not re.search("[0-9]",p):
        print("Not a Valid Password \nAt least 1 number between [0-9] ")
    elif not re.search("[A-Z]",p):
        print("Not a Valid Password \nAt least 1 letter between [A-Z] ")
    elif not re.search("[$#@]",p):
        print("Not a Valid Password \nAt least 1 character from [$#@] ")
    elif len(p)<6 :
        print("Not a Valid Password \nMinimum length of transaction password is 6 ")
    elif len(p)>12:
        print("Not a Valid Password \nMaximum length of transaction password is 12 ")
    else:
        print("Valid Password")
verify()       


# # Encryption

# In[2]:


Password = input("Re-enter the Valid Password you have entered before: ")
DOB = int(input("Enter your DOB as DDMMYYYY: "))
SumDigits = int(input("Add all the digits of your DOB: "))
distance = SumDigits % 26
def cipher(EncryptedText, distance):
    EncryptedText = ""
    for symbol in Password:
        if symbol.isnumeric():
            num = ord(symbol)
            num += distance
            
            if num > ord("9"):
                num -= 10
            if num < ord("0"):
                num += 10
            
            EncryptedText += chr(num)
            
        elif symbol.isalpha():
            num = ord(symbol)
            num += distance

            if symbol.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26  
                    
            EncryptedText += chr(num)
        else:
            EncryptedText += symbol
            
    return EncryptedText

print(cipher(Password, distance))       


# # Store Username and Encrypted Password

# In[5]:


file = open("MIT191358.txt","w")
file.write(input("Enter your username: ")  + ' ') 
# + " " is used to add space between username and password
file.write(input("Enter the Encrypted Password:"))
file = open("MIT191358.txt","r")
text = file.read()
print(text)


# # Decryption and Password Reveal Option

# In[3]:


UserName = input("Enter your username: ") 
EncryptedPassword = input("Enter your Encrypted Password: ")
SumDigits = int(input("Enter your sumdigits you have entered before: "))
distance = SumDigits % 26
def decrypt(DecryptedText, distance):
    DecryptedText = ""
    for symbol in EncryptedPassword:
        if symbol.isnumeric():
            num = ord(symbol)
            num -= distance
            
            if num < ord("0"):
                num += 10
            
            DecryptedText += chr(num)
            
        elif symbol.isalpha():
            num = ord(symbol)
            num -= distance

            if symbol.isupper():
                if num < ord('A'):
                    num += 26
            elif symbol.islower():
                if num < ord('a'):
                    num += 26  
                    
            DecryptedText += chr(num)
        else:
            DecryptedText += symbol
            
    return DecryptedText

def reveal():
    reveal = input("Do you want to print your password?: ")
    
    if reveal == "Yes":
        print(UserName)
        print(decrypt(EncryptedPassword,distance))
    
    elif reveal == "No":
        print(UserName)
        print("*"*8)  #8 is the length of *
        
reveal()      


# In[ ]:




