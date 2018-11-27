import collections
class sorted_dict(dict):
    def __init__(self):
        super().__init__(self)
        self.ordered = []
    def __setitem__(self,key,value):
        dict.__setitem__(self,key,value)
        self.ordered=sorted(self.ordered+[key])
    def items(self):
        return collections.ItemsView(self)
    def keys(self):
        return collections.KeysView(self)
    def __iter__(self):
        return self.ordered.__iter__()
    def __delitem__(self,key):
        dict.__delitem__(self,key)
        self.ordered.remove(key)
