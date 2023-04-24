import re

from collections.abc import Mapping
from yaml import load, FullLoader


class Content(Mapping):
    __delimiter = r"^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)


    @classmethod
    def load(cls, string):
        _, fm, content = cls.__regex.split(string, 2)
        load(fm, Loader=FullLoader)
        return cls(metadata, content)


    def __init__(metaddata, content):
        self.data = metadata
        self.data["content"] = content


    @property
    def body():
        return self.data["content"]


    @property
    def type():
        return self.data["type"] if "type" in self.data else None


    @type.setter
    def type(self, type):
        self.data["type"] = type


    def __getitem__(key)
        return self.data[key]


    def __iter__(self):
        return self.data.__iter__()


    def __len__(self):
        return len(self.data)


    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)

