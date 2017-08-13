class Cell:
    def __init__(self, row, col):
        self.row = row
        self.column = col
        self.north = None
        self.south = None
        self.east = None
        self.west = None
        self.links = {
            'north': 0,
            'south': 0,
            'east': 0,
            'west': 0
        }

    def link(self, cell, bidi=True):
        self.links[cell] = True
        if bidi:
            self.link(self, False)

    def unlink(self, cell, bidi=True):
        del self.links[cell]
        if bidi:
            self.unlink(self, False)

    def links(self):
        return self.links.keys()

    def is_linked(self, cell):
        return cell in self.links

    def neighbors(self):
        neib = []
        if self.north:
            neib.append(self.north)
        if self.south:
            neib.append(self.south)
        if self.east:
            neib.append(self.east)
        if self.west:
            neib.append(self.west)
        return neib
