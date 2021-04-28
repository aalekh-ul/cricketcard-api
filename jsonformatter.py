import jsons
from pprint import pprint

with open('aus_apidata3.json') as f:
    data = jsons.loads("[" + 
        f.read().replace("}\n{", "},\n{") + 
    "]")

    print(data)