import json
j = { "serverPort": 52333, "debugMode": True, "maxThread": 2, "log": ["rtf", ".jpg"], "eventTypes": "Output"}
x = json.dumps(j)
print(x)


def memory_options():
    with open("GUI_APP/file1.json") as f:
        data = json.load(f)
        print(data)

memory_options()




