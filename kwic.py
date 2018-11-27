import re, operator
class Kwic:
    def __init__(self, filename):
        self.filename=filename
        self.index=self.build_index()


    def get_keywords(self, line, doc):
        keywords = re.split('\s',line.strip())
        index_per_doc = []
        for i in range(0,len(keywords)):
            if len(keywords[i])>=3 and keywords[i].lower() != 'the' and keywords[i].lower() != 'and':
                index_per_doc.append((doc, keywords[i], keywords[0:i+1],keywords[i+1:len(keywords)]))
        return index_per_doc

    def sort_keywords(self):
        return self.index
    def build_index(self):
        with open(self.filename) as file:
            lines = file.read().split('\n')
            index = sum([self.get_keywords(lines[i],i) for i in range(0,len(lines))],[])
            return sorted(index, key= lambda a : operator.itemgetter(1, a).item.lower())

    def __str__(self):
        output=[]
        for (doc, keyword, first, second) in self.index:
            output.append("{0:<5} {1:>40.33} {2:<40.40}".format(doc,' '.join(first),' '.join(second)))
        return "{0}".format('\n'.join(output))


obj = Kwic("titles")
print("{0}".format(obj))
