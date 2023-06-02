import pygame
from namusi_gui import NamusiGUI as namusi_gui

class NamusiImage:
    def __init__(self, window):
        self.image = None
        self.window = window
    
    def load(self, file_path):
        self.image = pygame.image.load(file_path).convert()
    
    def is_set(self):
        if self.image:
            return True
        else:
            return False

    def draw(self):
        if self.is_set():
            scaled_image = self.scaled()
            self.window.blit(scaled_image[0], (0, 0))
        else:
            font = pygame.font.SysFont('Helvetica', 32)
            text = font.render('No image', True , (168, 168, 168))
            self.window.blit(text, namusi_gui.get_center_point((0, 0), self.window.get_size(), (text.get_width(), text.get_height())))

    
    def scaled(self):
        # https://stackoverflow.com/questions/20002242/how-to-scale-images-to-screen-size-in-pygame
        swidth, sheight = self.window.get_size()
        sheight -= namusi_gui.BUTTON_HEIGHT # menu bar
        iwidth, iheight = self.image.get_size()
        scale = min(swidth / iwidth, sheight / iheight)
        new_size = (round(iwidth * scale), round(iheight * scale))
        scaled_image = pygame.transform.smoothscale(self.image, new_size) 
        image_rect = scaled_image.get_rect(center = (swidth // 2, sheight // 2))
        return scaled_image, image_rect