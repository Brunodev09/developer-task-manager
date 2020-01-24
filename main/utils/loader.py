import json

class jsonLoader:
    def __init__(self):
        with open('main/utils/default.json', 'r') as data:
            self.doc = json.load(data)

def getJson():
    jsonInstance = jsonLoader()
    return jsonInstance

