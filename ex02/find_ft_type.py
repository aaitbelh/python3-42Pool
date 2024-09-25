def all_thing_is_obj(object: any) -> int:
    types = {
        list: "List",
        tuple: "Tuple",
        set: "Set",
        dict: "Dict"
    }
    typeOfObject = type(object)
    myObjectType = types.get(typeOfObject, "Type not found")
    if typeOfObject == str:
        print(f"{object} is in the kitchen: {typeOfObject}")
    elif typeOfObject != "Type not found":
        print(f"{myObjectType} : {typeOfObject}")
    else:
        print(myObjectType)
    return 42

