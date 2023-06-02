import pygame
from namusi_gui import NamusiGUI as namusi_gui

class NamusiButtons():
    COLOR_TEXT = (255, 255, 255)
    COLOR_DEF = (80, 80, 80)

    def __init__(self, window):
        self.buttons = []
        self.window = window
    
    def add_button(self, id:str, label:str, position, size, color=COLOR_DEF):
        self.buttons.append({'label': label, 'id': id, 'position': position, 'size': size, 'color': color})
    
    def get_buttons(self):
        return self.buttons
    
class NamusiButtonsActions():
    def __init__(self, window, mouse, buttons):
        self.buttons = buttons
        self.window = window
        self.mouse = mouse

    def draw(self):
        # any_button_is_hovered = False
        for button in self.buttons.get_buttons():
            # print(f"draw: {button['id']}")
            is_mouse_on_object = namusi_gui.is_mouse_on_object(self.mouse, button['position'], button['size'])
            try:
                color = namusi_gui.get_hover_color(button['color']) if is_mouse_on_object else button['color']
            except:
                color = namusi_gui.get_hover_color(NamusiButtons.COLOR_DEF) if is_mouse_on_object else NamusiButtons.COLOR_DEF

            if is_mouse_on_object:
                namusi_gui.any_button_hovered = True
            pygame.draw.rect(self.window, color, pygame.Rect(button['position'][0], button['position'][1], button['size'][0], button['size'][1]))

            font = pygame.font.SysFont('Helvetica', 16)
            text = font.render(button['label'] , True , NamusiButtons.COLOR_TEXT)
            self.window.blit(text, namusi_gui.get_center_point(button['position'], button['size'], (text.get_width(), text.get_height())))

    def button_pressed(self):
        button_pressed = ''
        for button in self.buttons.get_buttons():
            # print(f"button_pressed: {button['id']}")
            if namusi_gui.is_mouse_on_object(self.mouse, button['position'], button['size']):
                    button_pressed = button['id']
        return button_pressed
