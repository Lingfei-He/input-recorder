import os
import json


def get_config_path():
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    return os.path.join(static_dir, 'config.json')

def print_config_path():
    print(f'The config file is located in {get_config_path()}')

def load_config():
    with open(get_config_path())as f:
        config = json.load(f)
        print(config)