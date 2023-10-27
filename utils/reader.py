import json

def read_json(file_path: str):
    with open(file_path, 'r') as f:
        return json.load(f)

class Reader:
    __line: dict = None

    @classmethod
    @property
    def line(cls):
        print("get: ", id(cls), cls.__line)

        return cls.__line

    @staticmethod
    def load_line(file_path: str):
        #     Reader.__line = f.readlines(-1)[0]
        Reader.__line = read_json(file_path)
        print("load:", id(Reader), Reader.__line)
