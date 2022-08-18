MAX_LIST_LENGTH = 536870912

class Record:
    def __init__(self, path, _list, *args) -> None:
        self.cachePath = path
        self.tape = []
        self.update(_list, *args)
        
    def update(self, _list, *args):
        self.tape = self.tape + _list + list(args)
    
    def cache(self):
        with open(self.cachePath, "a") as fd:
            for t in self.tape:
                fd.write(t)
        self.tape.clear()