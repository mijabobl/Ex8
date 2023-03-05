#!/usr/bin/python
# Example Python script
import sys                    #import the sys module
argc = len(sys.argv)          #create variable storing sys.argv

if argc > 1:                  #if too many args print too many
    print("Too many args")
    print("In fact there are", argc, "arguments")  # print how many args there are
else:                         #otherwise print hello and variable where
    where = 'World'           #variable where is string world
    print("Hello", where)
print('Goodbye from ' + sys.argv[0])      #print goodbye and the sys.argv data which is file name
