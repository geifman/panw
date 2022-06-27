import os
import json


class Properties:

    __shared_instance = 'none'

    @staticmethod
    def get():
        """Static Access Method"""
        if Properties.__shared_instance == 'none':
           Properties()
        return Properties.__shared_instance

    def __init__(self):
        script_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = 'properties.json'
        abs_file_path = os.path.join(script_dir, rel_path)

        f = open(abs_file_path)
        data = json.load(f)
        self.envProperties = data
        f.close()
        Properties.__shared_instance = self

