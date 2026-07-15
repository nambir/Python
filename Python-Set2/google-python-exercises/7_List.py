import sys

def main():
   list =['a','b','c','d','e']
   print list[1:-1]## ['b', 'c']
   list[0:2]='z'## replace ['a', 'b'] with ['z']
   print list         ## ['z', 'c', 'd']



# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
