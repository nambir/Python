# Defines a "repeat" function that takes 2 arguments.

import re

def main():
  ## ^ = matches the start of string, so this fails:

  #match = re.search(r'^b\w+','foobar')#=>not found, match ==None
  #print match

  ## but without the ^ it succeeds:
  #match = re.search(r'b\w+','foobar')#=>  found, match.group()=="bar"
  #print match


  #str ='purple alice-b@google.com monkey dishwasher'
  #match = re.search(r'\w+@\w+', str)
  #if match:
   # print match.group()## 'b@google'

    password = '123456$$'
    if re.match(r'((?=.*\d)((?=.*[a-z])|(?=.*[A-Z])).{8,20})', password):
        print 'It is a weak password'
    else:
        print 'It is not a weak password'
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
