#!/usr/bin/env python3

def printName(n, f):
  file = open (f, 'w')
  file.write(n)
  file.close()
  
if __name__ == '__main__':
  name = input("Please enter your name: ")
  filename = input("Please enter a filename: ")
  printName(name, filename)
