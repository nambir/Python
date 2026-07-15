import sys
import re

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
    password = raw_input("Please enter weak password: ")
    if re.match(r'((?=.*\d)((?=.*[a-z])|(?=.*[A-Z])).{8,20})', password):
        print 'Success! your weak password is:',password
    else:
        print 'It is not a weak password'
        WeakPasswordMethod()

def StrongPasswordMethod():
    password = raw_input("Please enter strong password: ")
    if re.match(r"((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%]).{8,20})",password):
        print 'Success! your strong password is:',password
    else:
        print 'It is not a strong password'
        StrongPasswordMethod()
    
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
