import pygame
from .namusi_gui import NamusiGUI as namusi_gui

class NamusiNotes():

    COLOR_DEF = (255, 80, 80)
    SIZE = 20
    MAX_LENGTH = 32
    notes = []

    def __init__(self, window):
        # self.notes = []
        self.window = window
    
    def add_note(self, position, length=1):
        self.notes.append({'position': (position[0]-self.SIZE/2, position[1]-self.SIZE/2), 'length': length})
    
    def get_notes(self):
        return self.notes
    

class NamusiNotesActions():
    def __init__(self, window, mouse, notes):
        self.notes = notes
        self.window = window
        self.mouse = mouse

    def draw(self):
        for note in self.notes.get_notes():
            # print(f"draw: {button['id']}")
            is_mouse_on_object = namusi_gui.is_mouse_on_object(self.mouse, note['position'], (NamusiNotes.SIZE*note['length'], NamusiNotes.SIZE))
            color = namusi_gui.get_hover_color(NamusiNotes.COLOR_DEF) if is_mouse_on_object else NamusiNotes.COLOR_DEF

            if is_mouse_on_object:
                namusi_gui.any_note_hovered = True
            
            pygame.draw.rect(self.window, color, pygame.Rect(note['position'][0], note['position'][1], NamusiNotes.SIZE*note['length'], NamusiNotes.SIZE))

            
            font = pygame.font.SysFont('Helvetica', 16)
            if note['length'] > 1:
                text = font.render("-" , True , (0, 0, 0))
                note_center = namusi_gui.get_center_point(note['position'], (NamusiNotes.SIZE, NamusiNotes.SIZE), (text.get_width(), text.get_height()))
                self.window.blit(text, (note['position'][0] + 4, note_center[1]))

            text = font.render("+" , True , (0, 0, 0))
            note_center = namusi_gui.get_center_point(note['position'], (NamusiNotes.SIZE, NamusiNotes.SIZE), (text.get_width(), text.get_height()))
            self.window.blit(text, (note['position'][0]  + NamusiNotes.SIZE*note['length'] - text.get_width() - 4, note_center[1]))

        # if any_note_is_hovered:
        #     pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZEALL)
            # pygame.SYSTEM_CURSOR_SIZEALL
        # pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZEALL if any_note_is_hovered else pygame.SYSTEM_CURSOR_ARROW)
    
    def note_pressed(self):
        note_id = -1
        for note in self.notes.get_notes():
            # print(f"button_pressed: {button['id']}")
            if namusi_gui.is_mouse_on_object(self.mouse, note['position'], (NamusiNotes.SIZE*note['length'], NamusiNotes.SIZE)):
                    note_id = self.notes.get_notes().index(note)
        return note_id
    
    def set_length(self, note_id):
        note = self.notes.notes[note_id]
        length = note['length']
        increase = 1
        if length > 1:
            # if clicked on a left part of a note
            if self.mouse[0] < (note['position'][0] + (NamusiNotes.SIZE*length)/2):
                increase = -1
            # print(f"note position {note['position'][0]}")
            # print(f"mouse position {self.mouse[0]}")
            

        length += increase
        if length > NamusiNotes.MAX_LENGTH:
            length = NamusiNotes.MAX_LENGTH
        if length < 1:
            length = 1
        
        self.notes.notes[note_id]['length'] = length

    def remove(self, note_id):
        self.notes.notes.remove(self.notes.notes[note_id])
    
    def move(self, note_id, mouse_event, mouse_offset):
        mouse_x, mouse_y = mouse_event.pos
        mouse_offset_x, mouse_offset_y = mouse_offset
        note_length = self.notes.notes[note_id]['length']*NamusiNotes.SIZE

        if mouse_x > namusi_gui.WIDTH - note_length + mouse_offset_x:
            mouse_x = namusi_gui.WIDTH - note_length
            mouse_offset_x = 0
        if mouse_x < mouse_offset_x:
            mouse_x = 0
            mouse_offset_x = 0
        if mouse_y > namusi_gui.HEIGHT - NamusiNotes.SIZE - namusi_gui.BUTTON_HEIGHT + mouse_offset_y:
            mouse_y = namusi_gui.HEIGHT - NamusiNotes.SIZE - namusi_gui.BUTTON_HEIGHT
            mouse_offset_y = 0
        if mouse_y < mouse_offset_y:
            mouse_y = 0
            mouse_offset_y = 0
        self.notes.notes[note_id]['position'] = (mouse_x-mouse_offset_x, mouse_y-mouse_offset_y)
    
    def note_mouse_offset(self, note_id):
        try:
            note = self.notes.notes[note_id]
            return (self.mouse[0]-note['position'][0], self.mouse[1]-note['position'][1])
        except Exception as ex:
            return (0, 0)

 