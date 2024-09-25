import sys
args = sys.argv

if len(args) != 2:
    print("AssertionError: more than one argument is provided")
    exit(1)

try:
    num = int(args[1])
    if num % 2 == 0:
        print ("I'm Even.")
    else:
        print ("I'm Odd.")
except :
    print("AssertionError: argument is not an integer")
