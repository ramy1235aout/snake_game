import pyray as rp
from snake import Snake
from food import Food

class Game:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 450
        self.snake = Snake()
        self.food = Food()
        self.game_over = False
        self.pause = False
        self.move_delay = 0.000001
        self.last_move_time = rp.get_time()
        self.score = 0

    def init(self):
        rp.init_window(self.screen_width, self.screen_height, "Snake Game")
        rp.set_target_fps(60) 

    def update(self):
        if not self.game_over:
            if rp.is_key_pressed(rp.KEY_P):
                self.pause = not self.pause

            if not self.pause:
                if rp.is_key_down(rp.KEY_RIGHT):
                    self.snake.change_direction("RIGHT")
                if rp.is_key_down(rp.KEY_LEFT):
                    self.snake.change_direction("LEFT")
                if rp.is_key_down(rp.KEY_UP):
                    self.snake.change_direction("UP")
                if rp.is_key_down(rp.KEY_DOWN):
                    self.snake.change_direction("DOWN")

                if rp.get_time() - self.last_move_time >= self.move_delay:
                    self.snake.move()
                    self.last_move_time = rp.get_time()

                    if self.food.check_collision(self.snake.body[0], self.snake):
                        self.snake.grow()
                        self.food.respawn()
                        self.score += 10

                
                    head = self.snake.body[0]
                    if head.x >= self.screen_width or head.y >= self.screen_height or head.x < 0 or head.y < 0:
                        self.game_over = True

        else:
            if rp.is_key_pressed(rp.KEY_ENTER):
                self.__init__() 
                self.game_over = False

    def draw(self):
        rp.begin_drawing()
        rp.clear_background(rp.RAYWHITE)

        if not self.game_over:
            self.food.draw()
            self.snake.draw()

            rp.draw_text(f"Score: {self.score}", 10, 10, 20, rp.BLACK)

            if self.pause:
                rp.draw_text("GAME PAUSED", self.screen_width // 2 - 100, self.screen_height // 2 - 40, 40, rp.GRAY)
        else:
            rp.draw_text("PRESS [ENTER] TO PLAY AGAIN", self.screen_width // 2 - 100, self.screen_height // 2 - 50, 20, rp.GRAY)

        rp.end_drawing()