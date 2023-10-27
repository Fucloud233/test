import json

def read_json(file_path: str):
    with open(file_path, 'r') as f:
        return json.load(f)

class Config:
    __info: dict = None

    @classmethod
    @property
    def info(cls):
        print("get: ", id(cls), cls.__info)
        return cls.__info

    @staticmethod
    def load_info(file_path: str):
        Config.__info = read_json(file_path)
        print("load:", id(Config), Config.__info)
