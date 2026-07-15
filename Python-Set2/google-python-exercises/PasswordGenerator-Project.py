import sys
import re
import os, random, string

def main():

        pwdtype=raw_input('Dear user what type of password would you like to generate (weak or strong): ')
        SelectPasswordType(pwdtype)


def SelectPasswordType(pwdtype):
        if pwdtype.lower()=='strong':
            StrongPasswordMethod()
        elif pwdtype.lower()=='weak':
            WeakPasswordMethod()
        else:
           print 'You have entered invalid password preference'
           pwdtype=raw_input('Please enter weak or strong: ')
           SelectPasswordType(pwdtype)
           
def WeakPasswordMethod():
    length = 8
    Lower = string.lowercase 
    Upper = string.uppercase
    digit = string.digits 
    random.seed = (os.urandom(1024))
    pwd=''.join(random.choice(Lower) for i in range(3))
    pwd=pwd+''.join(random.choice(Upper) for i in range(3))
    pwd=pwd+''.join(random.choice(digit) for i in range(2))
    
    print 'Your weak Password is:',pwd 

def StrongPasswordMethod():
    length = 8
    Lower = string.lowercase 
    Upper = string.uppercase
    Symbol = '!@#$%^&*()'
    digit = string.digits 
    random.seed = (os.urandom(1024))
    pwd=''.join(random.choice(Lower) for i in range(2))
    pwd=pwd+''.join(random.choice(Upper) for i in range(2))
    pwd=pwd+''.join(random.choice(Symbol) for i in range(2))
    pwd=pwd+''.join(random.choice(digit) for i in range(2))
    
    print 'Your strong Password is:',pwd 
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
