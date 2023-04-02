import json
from datetime import datetime



def replace_in_json(json: dict, replace_fild: str, replace_to: str) -> dict:
    for i in json:
        if i == replace_fild: json[i] = replace_to
        elif isinstance(json[i], dict): json[i] = replace_in_json(json[i], replace_fild, replace_to)
    return json

json_path: str = "task4.json"
date_iso: str = str(datetime.now())

with open(json_path, 'r+') as f:
    data: dict = json.load(f)
    replaced_json = replace_in_json(data, "updated", date_iso)
    with open(json_path, 'w') as f2:
        json.dump(replaced_json, f2)
