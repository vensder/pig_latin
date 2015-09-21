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



