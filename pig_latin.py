#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '--== Pig Latin (oo) Igpay Atinlay ==--'
print 'Welcome to the Pig Latin Translator!'

username = raw_input("Enter Your Name, Please:")

if len(username) > 0 and username.isalpha():
    print username
elif len(username) == 0:
    print "Please Try again. You should type your name and press Enter key"
elif not username.isalpha():
    print "Please don't use only alphabetical characters."

pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    print original
else:
    print 'empty'
    
word = original.lower()
first = word[0]
new_word = word + first + pyg
new_word = new_word[1:len(new_word)]

print new_word
