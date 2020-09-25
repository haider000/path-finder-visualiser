import pygame
from queue import PriorityQueue
import math


SIDE = 800
Root = pygame.display.set_mode(SIDE,SIDE)
pygame.display.pygame.display.set_caption("Path-finder Visualiser")


class Spot:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.width = width
        self.x = row * width
        self.y = col * width
        self.color = (255,255,255) #White
        self.neighbors = []
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == () #Red

    def is_open(self):
        return self.color == () #Green

    def is_barrier(self):
        return self.color == () #Black

    def is_start(self):
        return self.color = () #Orange

    def is_end(self):
        return self.color == () #Turquoise

    def reset(self):
        self.color = () #White #look for future
        
    def make_closed(self):
        self.color = () #Red

    def make_open(self):
        self.color = () #Green

    def make_barrier(self):
        self.color = () #Black

    def make_end(self):
        self.color = () #Turquoise

    def make_path(self):
        self.color = () #Purple

    def draw(self,win):
        pygame.draw.pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self,grid):
        pass

    def __lt__(self,other):
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)


def make_grid(rows,width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Spot(i, j, gap, rows)
            grid[i].append(spot)
    
    return grid



        





