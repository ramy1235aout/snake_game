import pyray as rp
from game import Game

def main():
    game = Game() 
    game.init() 
    while not rp.window_should_close():
        Game.update(game)
        Game.draw(game)
    rp.close_window()

if __name__ == "__main__":
    main()