
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
    if type(msg) != str:
        return None
    return input(msg)


def parse(string, dictionary):
    try:
        if len(string.split(' ')) > 1:
            if dictionary[string.split(' ')[0]]:
                dictionary[string.split(' ')[0]](string.split(' ')[1])
        elif string == 'help':
            string = 'help_commands'
            dictionary[string]()
        else: 
            print('Please point a target to your command.')    
    except Exception as e:
        # TODO Treat other exception types
        print(">> Invalid command", e)        

