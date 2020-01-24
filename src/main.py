from utils.helper import switcher, request_for_input, parse
from utils.events import help, start_task, get_task, stop_task, list_tasks

import json
with open('default.json', 'r') as data:
        json_dict = json.load(data)

def main_loop():
    print(json_dict["commandList"])
    commands_dict = switcher(json_dict["commandList"], [help])
    cmd = None
    while cmd != "exit":
        cmd = request_for_input(json_dict["messages"]["default"])
        parse(cmd, commands_dict)

try:
    main_loop()
    pass
except KeyboardInterrupt as identifier:
    print(json_dict["messages"]["exit"])
    pass
