
class Player:
    def __init__(self, movable, view_range):
        self.movable = movable
        self.view_range = view_range
        # self.position = position
        self.view_range
        self.died = False 
    def set_position(self, position):
        self.position = position

    def set_id(self, id):
        self.id = id 
           
    def dead(self):
        self.died = True 
        self.movable = False 

    def move(self, direction):
        return 
    
