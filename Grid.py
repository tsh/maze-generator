from Cell import Cell


class Grid(object):
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.array = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        array = []
        for row in self.rows:
            row = []
            for col in self.columns:
                row.append(Cell(row, col))
            array.append(row)
        return array

    def configure_cells(self):
        for irow, row in enumerate(self.array):
            for icolumn, cell in enumerate(row):
                cell.north = self.array[irow - 1][icolumn]
                cell.south = self.array[irow + 1][icolumn]
                cell.west = self.array[irow][icolumn - 1]
                cell.east = self.array[irow][icolumn + 1]