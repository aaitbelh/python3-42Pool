import math
#need to get checked again
def isNaN(value):
    return value != value


def NULL_not_found(object: any) -> int:
    types = {
        None    : "Nothing",
        "NaN"   : "Cheese",
        '0'       : "Zero",
        ''      : "Empty",
        False   : "Fake",
    }
    typeOfObject = types.get(object, "Type not Found")
    if type(object) == float and isNaN(object) :
        print(f"{types["NaN"]}: {object} {type(object)}")
    elif type(object) == int and object == 0:
        print(f"{types['0']}: {object} {type(object)}" )
    elif typeOfObject == "Type not Found":
        print(f"Type not Found")
    else:
        print(f"{typeOfObject}: {object} {type(object)}")
    return 1
    
    

Nothing = None
Garlic = float("NaN")
Zero = 0
Empty = ''
Fake = False
NULL_not_found(Nothing)
NULL_not_found(Garlic)
NULL_not_found(Zero)
NULL_not_found(Empty)
NULL_not_found(Fake)
print(NULL_not_found("Brian"))


# $>python tester.py | cat -e
# Nothing: None <class 'NoneType'>$
# Cheese: nan <class 'float'>$
# Zero: 0 <class 'int'>$
# Empty: <class 'str'>$
# Fake: False <class 'bool'>$
# Type not Found$
# 1$
# $>
