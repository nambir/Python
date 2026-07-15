import sys

def main():
  #squares = [1, 4, 9, 16]
  #sum = 0
  #for num in squares:
   #  print num
   # sum += num
  #print sum  ## 30
   




    hash ={}
    hash['noun']='pizza'
    hash['number']= 5
    hash['verb'] = 'eat'
    s = 'I usually %(verb)s %(number)d slices of %(noun)s' % hash
    print s

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
