#!/usr/bin/env python3
import sys
def printVars:
  var1 = sys.argv[1]
  var2 = sys.argv[2]
  print('Variable1 = ' + var1)
  print('Variable2 = ' + var2)
  print('The script and variables used are', str(sys.argv))
  
if __name__ == '__main__':
  printVars()
