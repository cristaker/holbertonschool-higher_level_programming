#!/usr/bin/python3
"""function that writes an Object"""

import json


def save_to_json_file(my_obj, filename):
    """function"""

    with open(filename, 'w', encoding='UTF8') as f:
        return json.dump(my_obj, f)
