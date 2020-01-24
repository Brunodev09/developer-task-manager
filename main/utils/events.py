class eventSwitch:
    def __init__(self, doc):
        self.doc = doc

    def help_commands(self):
        print(self.doc["messages"]["help"])
        return True

    def new_task(self, task):
        print('>> Starting a new task...')    

    def start_task(self):
        print(self.doc["messages"]["start_task"])
        return True

    def get_task(self, task):
        print(self.doc["messages"]["get_task"])
        if (task in self.doc["tasks"]):
            print('>> Task ' + task + ' has been found.')
            keys = self.doc["tasks"][task].keys()
            finalStr = ""
            for k in keys:
                finalStr += "\n>> " + k + ": " + self.doc["tasks"][task][k]
            print(finalStr)
            return True    
        print('>> ' + task + ' is not in cache.')        
        return False

    def finish_task(self):
        print(self.doc["messages"]["stop_task"])
        return True

    def list_tasks(self):
        print(self.doc["messages"]["list_tasks"])
        return True

    def pause_task(self):
        print(self.doc["messages"]["pause_task"])
        return True

    def keys(self):
        return [k for k in dir(self) if not k.startswith('__') and k != 'doc' and k != 'keys' and k != 'get']

    def get(self, f):
      return getattr(self, f) 
     
    @staticmethod
    def exit():
        return
