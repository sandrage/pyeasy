class UpDownFile:
    def __init__(self,filename):
        self.filename = filename
    def __iter__(self):
        self.alreadyread = []
        #il numero delle word lette
        self.lastread=0
        self.fileopened = open(self.filename)
        return self
    def __next__(self):
        #se il numero delle words lette è inferiore al totale dell'array vuol dire che
        #ho fatto degli ungetw perciò mi basta leggere dalla cache
        if self.lastread<=(len(self.alreadyread)-1):
            self.lastread+=1
            return self.alreadyread[self.lastread-1]
        text = ""
        #leggo un carattere
        chr = self.fileopened.read(1)
        #controllo se è già vuoto, se lo è ho finito il file
        if chr is '': raise StopIteration
        #potrebbero esserci spazi o altri quindi li svuoto prima
        while chr!='' and (chr.isspace() or not(chr.isalnum())):
            chr = self.fileopened.read(1)
        #controllo se ho terminato il file leggendo quegli spazi
        if chr is '': raise StopIteration
        #se non è ancora terminato il file allora leggo le lettere che effettivamente mi servono
        while (not chr.isspace()) and chr.isalnum():
            text=text+chr
            chr = self.fileopened.read(1)
        self.alreadyread+=[text]
        self.lastread+=1
        return text
    def ungetw(self):
        if self.lastread<0: raise StopIteration
        self.lastread-=1
