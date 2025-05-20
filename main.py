# this will be the main file where code will run.
import arcade
import arcade.gui

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Puzzle Game"

class MyGame(arcade.Window):
    def __init__(self):
        # constructor for the class
        # will need to add variables here to store sprites and game data
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.current_screen = "WELCOME"
        self.ui_manager = arcade.gui.UIManager()
        self.start_button = None
        self.background = None

    def setup(self):
        # method used to initalize or reset the game.
        # typically you'd load sprites, set up the board, and initalize variables here.
        # initializing background variable
        if self.current_screen == "WELCOME":
            self.show_welcome_screen()
        self.background = arcade.load_texture("assets/table.jpg")
    
    def show_welcome_screen(self):
        self.ui_manager.clear()
        self.ui_manager.enable()

        # create a vertical box for layout
        v_box = arcade.gui.UIBoxLayout()

        # welcome label
        welcome_label = arcade.gui.UILabel(text="Welcome to the game!", font_size=30)
        v_box.add(welcome_label)

        # start button
        self.start_button = arcade.gui.UIFlatButton(text="Start Game")
        self.start_button.on_click = self.on_start_click
        v_box.add(self.start_button)

        # center layout on screen
        anchor = arcade.gui.UIAnchorLayout()
        anchor.add(child=v_box, anchor_x="center_x", anchor_y="center_y")
        self.ui_manager.add(anchor)
    
    def on_start_click(self, event):
        self.current_screen = "GAME"
        self.ui_manager.clear()

    def on_draw(self):
        # method automatically called to draw everything on screen.
        # arcade.start_render()
        self.clear()
        # this line clears the screen and gets it ready for new drawings.
        # after this you might draw sprites and text
        if self.current_screen == "WELCOME":
            arcade.set_background_color(arcade.color.PINK_LAVENDER)
            self.ui_manager.draw()
        elif self.current_screen == "GAME":
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