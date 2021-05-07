import yaml
from pprint import pprint

yaml_example = open("example_YAML_file.yaml").read()
pprint(yaml_example)

print("\n\n\n\n")


yaml_dict = yaml.load(yaml_example)
pprint(yaml_dict)

print(yaml_dict[0]['vars']['var_dic']['name'])