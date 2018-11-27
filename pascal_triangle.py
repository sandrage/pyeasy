import copy
class PascalTriangle():
    def __init__(self):
        self._row_number=0
        self._prec=None
        self._row=[1]
    def __iter__(self):
        return self
    def __next__(self):
        self._prec=copy.deepcopy(self)
        previous_row = self._row
        self._row=[]
        for i in range(0,self._row_number+1):
            if i-1 >=0:
                firstOp = previous_row[i-1]
            else:
                firstOp = 0
            if i>=len(previous_row) :
                secondOp = 0
            else:
                secondOp = previous_row[i]
            self._row = self._row+[firstOp + secondOp]
        self._row_number=self._row_number+1
        return self._row
    def prev(self):
        prev = copy.deepcopy(self._prec)
        self._row=prev._row
        self._prec=prev._prec
        self._row_number=self._row_number-1
        return self._row
    def __str__(self):
        return "current row: {0} - previous row: {1} - row number: {2}".format(self._row,self._prec._row, self._row_number)


if __name__=='__main__':
    triangle = PascalTriangle()
    print(next(triangle))
    print(next(triangle))
    print(next(triangle))
    print(next(triangle))

    print(triangle.prev())
    print(triangle.prev())
    print(triangle.prev())
