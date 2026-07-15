import sys

def main():
  dict ={}
  dict['a']='alpha'
  dict['g']='gamma'
  dict['o']='omega'

 ## .items() is the dict expressed as (key, value) tuples
  print dict.items()##  [('a', 'alpha'), ('o', 'omega'), ('g', 'gamma')]

  ## This loop syntax accesses the whole dict by looping
  ## over the .items() tuple list, accessing one (key, value)
  ## pair on each iteration.
  for k, v in dict.items():print k,'>', v
  ## a > alpha    o > omega     g > gamma


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
