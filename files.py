import json

f = open("c:/temp/py/config.json")
try:
    res = json.load(f)
except ValueError as ex:
    print(ex)
    res = {}
finally:
    f.close()

print(res)
