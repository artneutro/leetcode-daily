# https://leetcode.com/problems/design-spreadsheet/
class Spreadsheet:

    def __init__(self, rows: int):
        self.sheet = {}

    def setCell(self, cell: str, value: int) -> None:
        if cell[0] in self.sheet :
            self.sheet[cell[0]][cell[1:]] = value
        else :
            self.sheet[cell[0]] = {cell[1:]: value}

    def resetCell(self, cell: str) -> None:
        if cell[0] in self.sheet :
            self.sheet[cell[0]][cell[1:]] = 0

    def getValue(self, formula: str) -> int:
        get_add = formula[1:].split('+')
        add1 = get_add[0]
        add2 = get_add[1]
        # Number + Number
        if add1[0].isdigit() and add2[0].isdigit() :
            return int(add1) + int(add2)
        # Number + Cell
        elif add1[0].isdigit() and not add2[0].isdigit() :
            if add2[0] in self.sheet :
                if add2[1:] in self.sheet[add2[0]] :
                    return int(add1) + self.sheet[add2[0]][add2[1:]]
            return int(add1)
        # Cell + Number
        elif not add1[0].isdigit() and add2[0].isdigit() :
            if add1[0] in self.sheet :
                if add1[1:] in self.sheet[add1[0]] :
                    return self.sheet[add1[0]][add1[1:]] + int(add2)
            return int(add2)
        # Cell + Cell
        else :
            sum1 = 0
            sum2 = 0
            if add1[0] in self.sheet :
                if add1[1:] in self.sheet[add1[0]] :
                    sum1 = self.sheet[add1[0]][add1[1:]]
            if add2[0] in self.sheet :
                if add2[1:] in self.sheet[add2[0]] :
                    sum2 = self.sheet[add2[0]][add2[1:]]
            return sum1 + sum2
        


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
