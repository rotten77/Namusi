class NamusiGUI:

    # defaults
    WIDTH = 1200 * 0.8
    HEIGHT = WIDTH * 3/4# 9/16
    BACKGROUND = (232, 232, 232)
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 32
    HEIGHT += BUTTON_HEIGHT

    any_note_hovered = False
    any_button_hovered = False
    region = ((0, 0), (WIDTH, HEIGHT))
    region_selection_start = False
    region_selection = False

    @staticmethod
    def get_center_point(wrapper_position, wrapper_size, object_size):
        wrapper_center = (int(wrapper_size[0]/2), wrapper_size[1]/2)
        object_center = (int(object_size[0]/2), object_size[1]/2)
        return (wrapper_position[0]+wrapper_center[0]-object_center[0], wrapper_position[1]+wrapper_center[1]-object_center[1])

    
    @staticmethod
    def is_mouse_on_object(mouse, object_position, object_size):
        if (
            mouse[0] >= object_position[0] and
            mouse[0] <= object_position[0]+object_size[0] and
            mouse[1] >= object_position[1] and
            mouse[1] <= object_position[1]+object_size[1]
            ):
            return True
        else:
            return False
    
    @staticmethod
    def get_hover_color(color):
        return (color[0]*0.6, color[1]*0.6, color[2]*0.6)