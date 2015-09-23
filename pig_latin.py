#!/usr/bin/env python
# -*- coding: utf-8 -*-

print '--== Pig Latin (oo) Igpay Atinlay ==--'
print 'Welcome to the Pig Latin Translator!'

def username():
    uname = raw_input("Enter Your Name, Please:\n")
    return (uname)

def check_username(uname):
    while len(uname) == 0 or not uname.isalpha():
        if len(uname) == 0:
            print "Please Try again. You should type your name and press Enter key"
        elif not uname.isalpha():
            print "Please use only alphabetical characters."

        uname = raw_input("Enter Your Name, Please:\n")
    else:       
        print "Hi " + uname + "! I want to play a game"

def pyg():
    pyg = 'ay'
    original = raw_input('Enter any one word:\n ')

    if len(original) > 0 and original.isalpha():
        print original + "?"
    else:
        print 'You should type any English word'
        
    word = original.lower()
    first = word[0]
    new_word = word + first + pyg
    new_word = new_word[1:len(new_word)]

    print "In Pig Latin language " + original + " will be: " + new_word

n = username()
check_username(n)
pyg()

print 'End of code'
