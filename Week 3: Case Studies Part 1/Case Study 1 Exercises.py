# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 14:39:36 2022

@author: ingri
"""

#Exercise 1
#In Exercise 1, we will define the alphabet used in the cipher.
#The sample code imports the string library has been imported. 
#Create a string called alphabet consisting of the space character (' ') 
#followed by (concatenated with) the lowercase letters. 
#Note that we're only using the lowercase letters in this exercise.

import string
alphabet =  " " + string.ascii_lowercase



#Exercise 2
#1 point possible (graded)
#In Exercise 2, we will define a dictionary that specifies the index of each character in alphabet.
#Note that alphabet is as defined in Exercise 1. 
#Create a dictionary with keys consisting of the characters in alphabet and 
#values consisting of the numbers from 0 to 26. Store this as positions.
#What is the value of the key n in the positions dictionary?

position = {}
p=0
for c in alphabet:
    position[c]=p
    p+=1 # p = p + 1
position['n']   
    
#Exercise 3
#1 point possible (graded)
#In Exercise 3, we will encode a message with a Caesar cipher.

#Note that alphabet and positions are as defined in Exercises 1 and 2. Use positions to create an encoded message based on message where each character in message has been shifted forward by 1 position, as defined by positions.

#Note that you can ensure the result remains within 0-26 using result % 27.

#Store this as encoded_message.

#Use this code to get started:
    
    
message = "hi my name is caesar"
encoded_message = ''
for c in message:
  for key, values in position.items():
    if values == (position[c] + 1) % 27:
      encoded_message += key
encoded_message



#Exercise 4

def encoding(message, encription_key):
  encoded_message = ''
  for c in message:
    for key, values in position.items():
      if values == (position[c] + encription_key) % 27:
        encoded_message += key
  return encoded_message
encoded_message = encoding(message, 3)
encoded_message



#Exercise 5
#1 point possible (graded)
#In Exercise 5, we will decode an encoded message.

#Instructions
#Use encoding to decode encoded_message.
#Store your encoded message as decoded_message.
#Print decoded_message. Does this recover your original message?
#What key can be used to decode the message and recover the original message shifting backwards?

def decoding(encoded_message, decription_key):
  decoded_message = ''
  for c in encoded_message:
    for key, values in position.items():
      if values == (position[c] - decription_key) % 27:
        decoded_message += key
  return decoded_message
decoding(encoded_message, 3)