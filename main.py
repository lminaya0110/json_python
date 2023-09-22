import json
from structure_elems import take

def read_json_return_structure(file_name):
    
    with open(file_name, encoding="utf8") as fn:
        return json.load(fn)
    
countries_list = read_json_return_structure("countries.json")
countries_states_list = read_json_return_structure("countries_states_cities.json")

take(3, countries_states_list)
take(3, countries_states_list)

