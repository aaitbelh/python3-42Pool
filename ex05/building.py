import sys

string = sys.argv

def calculate_fun(string):
    types = {
        "lowerCases": 0,
        "uperCases" : 0,
        "spaces"  : 0,
        "numeric": 0,
        "panctuation": 0,
    }
    for i in string:
        if i.islower():
            types["lowerCases"] += 1
        elif i.isupper():
            types["uperCases"] +=1
        elif i.isspace():
            types["spaces"] +=1
        elif i.isnumeric():
            types["numeric"] +=1
        else:
            print(f"--->{i}")
            types["panctuation"] +=1
    return types


def building(args:any):
    string = ''
    try:
        if args and len(args) > 2:
            raise "AssertionError: more than one argument is provided"
        elif args == None or len(args) == 1:
            string = input("What is the text to count?\n")
        else:
            string = args[1]
        type = calculate_fun(string)
        print(type)
        print(f"The text contains {len(string)} characters:\n \
              {type["uperCases"]} upper letters\n \
              {type["lowerCases"]} lower letters\n \
              {type["panctuation"]} punctuation marks\n \
              {type["spaces"]}  spaces\n \
              {type["numeric"]} digits\n\
            ")
    except AssertionError:
        print(AssertionError) 
