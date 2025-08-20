import pyray as rp

SQUARE_SIZE = 15
SPEED = 5

class Snake:
    def __init__(self):
        self.body = [rp.Vector2(400, 225)] 
        self.direction = rp.Vector2(1, 0)  
        self.new_segment = False 

    def change_direction(self, direction):
        if direction == "UP" and self.direction.y == 0:
            self.direction = rp.Vector2(0, -1)
        elif direction == "DOWN" and self.direction.y == 0:
            self.direction = rp.Vector2(0, 1)
        elif direction == "LEFT" and self.direction.x == 0:
            self.direction = rp.Vector2(-1, 0)
        elif direction == "RIGHT" and self.direction.x == 0:
            self.direction = rp.Vector2(1, 0)

    def move(self):
        new_head = rp.Vector2(self.body[0].x + self.direction.x * SPEED,
                              self.body[0].y + self.direction.y * SPEED)
        
        self.body.insert(0, new_head) 

        if not self.new_segment:
            self.body.pop() 
        else:
            self.new_segment = False

    def grow(self):
        self.new_segment = True

    def draw(self):
        for segment in self.body:
            rp.draw_rectangle_v(segment, rp.Vector2(SQUARE_SIZE, SQUARE_SIZE), rp.GREEN)
            