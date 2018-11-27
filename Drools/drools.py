import itertools
class Drools:
    def __init__(self,rules,golfisti,colori,n):
        self.rules = rules
        self.golfisti = golfisti
        self.colori = colori
        self.n = n
    def eval(self):
        golfers = list(itertools.permutations(self.golfisti))
        colors = list(itertools.permutations(self.colori))
        for i in list(itertools.product(golfers,colors)):
            if all([rule(i[0],i[1],self.n) for rule in self.rules]):
                print(i)

if __name__=='__main__':
    rules = [lambda pl, pa, n: "red" in pa, #un golfista ha i pantaloni rossi
        lambda pl, pa, n: len(set(pa)) == 4, #ho 4 pantaloni
        lambda pl, pa, n: len(set(pl)) == 4, #e 4 golfisti
        lambda pl, pa, n: pl.index("fred")+1<len(pl) and pa[pl.index("fred")+1] == "blue", #quello alla destra di fred indossa pantaloni blu
        lambda pl, pa, n: pl.index("joe")==1, #joe è il secondo in fila
        lambda pl, pa, n: pa[pl.index("bob")]=="plaid", #bob indossa pantaloni plaid
        lambda pl, pa, n: 0<pl.index("tom")<3 and pa[pl.index("tom")]!="orange" #tom non è in posizione 1 o 4 e non indossa pantaloni arancioni
        ]
        #pa = pants
        #pl = golfisti
    d = Drools(rules,["bob", "joe", "fred", "tom"], ["red", "orange", "blue", "plaid"], list(range(1,5)))
    d.eval()
