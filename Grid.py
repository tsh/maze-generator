import random

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

    def get(self, row, col):
        """ same as def [](row, column) """
        if 0 <= row < self.rows and 0 <= col < len(self.array[row]):
            return self.array[row][col]
        else:
            return None

    def random_cell(self):
        return self.array[random.randint(0, self.rows - 1)][random.randint(0, self.columns - 1)]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in self.array:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                yield cell