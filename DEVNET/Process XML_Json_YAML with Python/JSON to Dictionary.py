import json
from pprint import pprint

json_example = open("example_JSON_file.json").read()
pprint(json_example)

print("\n\n\n\n")


json_dict = json.loads(json_example)
pprint(json_dict)

print(json_dict['address']['city'])