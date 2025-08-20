import pyray as rp
import random

y = random.randint(15,775)
x = random.randint(15,430)

SQUARE_SIZE = 15

class Food:
    def __init__(self):
        self.position = rp.Vector2(0, 0)
        self.size = rp.Vector2(SQUARE_SIZE, SQUARE_SIZE)
        self.color = rp.DARKBLUE
        self.position_alea = rp.Vector2(x , y )
        self.is_deleted = False


    def draw(self):
        if not self.is_deleted:
            rp.draw_rectangle_v(self.position_alea, self.size, self.color)


    def respawn(self):
         self.position_alea = rp.Vector2(random.randint(0, 800), random.randint(0, 450))


    def check_collision(self,position,snake):
        food_rect = rp.Rectangle(self.position_alea.x, self.position_alea.y, self.size.x, self.size.y)
        head = rp.Rectangle(position.x, position.y, SQUARE_SIZE, SQUARE_SIZE)

        if rp.check_collision_recs(head,food_rect):
            self.is_deleted = True
            self.draw()
            return True
        self.is_deleted = False

        return False 



