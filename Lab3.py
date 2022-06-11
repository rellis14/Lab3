#!/usr/bin/env python3

def printName(n, f):
  file = open (f, 'w')
  file.write(n)
  file.close()
  
def helloWorld():
  print('Hello World')
  
if __name__ == '__main__':
  name = input("Please enter your name: ")
  filename = input("Please enter a filename: ")
  printName(name, filename)
  helloWorld()
