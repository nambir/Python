import sys

def main():
# Echo the contents of a file
  f = open(r'D:\Nambi\CD1\Learning\Python\google-python-exercises\foo.txt','rU')
  for line in f:## iterates over the lines of the file
    print line,## trailing , so print does not add an end-of-line char
                   ## since 'line' already includes the end-of line.
  f.close()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
