#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:0]
    num_arguments = len(argv)

 print ("Number of argument{}:{}".format("s" if num_arguments != 1
     else "", "" if num_arguments == 0 else "s"),end="")

 print ("{}".format(":" if num_arguments > 0 else "."))

 for i, arg in enumerate(argv):
   print ("{}:{} {}".format(i +1, arg, "" if i== num_arguments -1
       else "\n"))
