import pynecone as pc


class pageList(pc.Base):
    title:str
    abbre:str
    path:str

class inputText(pc.Base):
    title:str
    author:str
    content:str
    header:list[str]