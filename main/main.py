from utils.helper import switcher, request_for_input, parse
from utils.events import eventSwitch
from utils.loader import getJson
from sys import exit
from utils.sqlite import sql

jsonInstance = getJson().doc
events = eventSwitch(jsonInstance, None)

def main_loop():
    askDb = request_for_input(
        "\n>> Welcome to DTM! Do you want to store your data in a local SQLite file or a JSON file? (json/sql)\n")
    if askDb == "json":
        print(">> So json it is.")
    elif askDb == "sql":
        print(">> So sql it is.")
        db = sql()
        db.run_test_queries()
        events.db = db;
    else:
        print(">> You entered an invalid command, so I'm choosing the 'json' option for you!")
        storeChoice = "json"

    event_arr_aux = events.keys()
    event_arr = []

    event_arr_aux.sort()
    jsonInstance["commandList"].sort()

    for evt in event_arr_aux:
        evt = events.get(evt)
        event_arr.append(evt)

    commands_dict = switcher(jsonInstance["commandList"], event_arr)
    cmd = None

    while cmd != "exit":
        try:
            cmd = request_for_input(jsonInstance["messages"]["default"])
            parse(cmd, commands_dict)
        except KeyboardInterrupt as ex:
            print(jsonInstance["messages"]["exit"])
            exit()


try:
    main_loop()
    pass
except Exception as ex:
    print(ex)
    print(jsonInstance["messages"]["exit"])
    pass
