
def switcher(keys, methods):
    if type(keys) is not list or type(methods) is not list:
        print("Invalid arguments for switcher. Please send two lists.")
        return None
    objDict = {}
    count = 0
    for key in keys:
        objDict[key] = methods[count]
        count += 1
    return objDict

def request_for_input(msg):
    return input(msg)

def parse(string, dictionary):
    if dictionary[string]:
        dictionary[string]()
    return None    
