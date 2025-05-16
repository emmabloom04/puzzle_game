# this will be the main file where code will run.
import arcade

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Puzzle Game"

class MyGame(arcade.Window):
    def __init__(self):
        # constructor for the class
        # will need to add variables here to store sprites and game data
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background = None

    def setup(self):
        # method used to initalize or reset the game.
        # typically you'd load sprites, set up the board, and initalize variables here.
        # initializing background variable
        self.background = arcade.load_texture("assets/table.jpg")

    def on_draw(self):
        # method automatically called to draw everything on screen.
        # arcade.start_render()
        self.clear()
        # this line clears the screen and gets it ready for new drawings.
        # after this you might draw sprites and text
        arcade.draw_texture_rect(self.background, rect=arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
        # sets the background image

    def on_update(self, delta_time):
        # this is automatically called many times per second.
        # delta_time is how much time has passed since the last frame.
        # mostly used for animations/movement
        # you would add game logic here, such as update
        pass

    # will need to add some more functions such as on_mouse_press() or on_mouse_drag() to support dragging.

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()