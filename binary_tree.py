from random import choice


class BinaryTree(object):
    def on(self, grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)
            try:
                neighbor = choice(neighbors)
                cell.link(neighbor)
            except IndexError:
                pass
