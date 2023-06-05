import pygame
# from math import floor
from .namusi_gui import NamusiGUI as namusi_gui

class NamusiGrid:
    def __init__(self, window):
        self.window = window
        self.points = {}

    def get_points(self, axis:str = ""):
        self.generate_points()
        if axis != "":
            return self.points[axis]
        else:
            return self.points
        
    def generate_points(self):
        self.points = {'x': [], 'y': []}

        region_start_x = namusi_gui.region[0][0]
        region_start_y = namusi_gui.region[0][1]
        region_end_x = namusi_gui.region[1][0]
        region_end_y = namusi_gui.region[1][1]

        region_width = region_end_x-region_start_x
        region_height = region_end_y-region_start_y

        grid_size_x = 16
        grid_cell_size_x = region_width/(grid_size_x)

        grid_size_y = 12
        grid_cell_size_y = region_height/(grid_size_y)

        for i in range(0, grid_size_x+1):
            self.points['x'].append(region_start_x + (i * grid_cell_size_x))

        for i in range(0, grid_size_y+1):
            self.points['y'].append(region_start_y + (i * grid_cell_size_y))

    def draw(self):
        self.generate_points()
        for line_x in self.points['x']:
            pygame.draw.line(self.window, (220, 180, 180, 50), (line_x, 0), (line_x, namusi_gui.HEIGHT))

        for line_y in self.points['y']:
            pygame.draw.line(self.window, (220, 180, 180, 50), (0, line_y), (namusi_gui.WIDTH, line_y))
