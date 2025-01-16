import os
import json


def get_config_path():
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    return os.path.join(static_dir, 'config.json')

def print_config_path():
    print(f'The config file is located in {get_config_path()}')

def load_json(path):
    with open(path)as f:
        return json.load(f)

def load_config():
    return load_json(get_config_path())
    
def edit_json(path, k, newV, check_exist=True):
    data = load_json(path)
    if check_exist and k not in newV:
        raise IndexError(f'There is no key named "{k}" in json data ({path}).')
    else:
        data[data]