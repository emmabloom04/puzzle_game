# this will be the main file where code will run.
import arcade
import arcade.gui
import random
import os
import re

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
        self.held_piece = None
        self.piece_list = None

    def setup(self):
        # method used to initalize or reset the game.
        # typically you'd load sprites, set up the board, and initalize variables here.
        # initializing background variable
        if self.current_screen == "WELCOME":
            self.show_welcome_screen()
        self.background = arcade.load_texture("assets/table.jpg")
        self.piece_list = arcade.SpriteList()
        self.piece_grid = {}

        piece_folder = "assets/puzzle_pieces"
        filenames = sorted(os.listdir(piece_folder))
        for filename in filenames:
            if filename.lower().endswith(".jpg"):
                path = os.path.join(piece_folder, filename)

                match = re.search(r"image(\d+)x(\d+)", filename.lower())
                if not match:
                    continue

                row = int(match.group(2))
                col = int(match.group(1))
            

                piece = arcade.Sprite(path, scale=0.2)

                offset_x = 200
                offset_y = 100
                piece_spacing = 130

                correct_x = offset_x + (col - 1) * piece_spacing
                correct_y = offset_y + (row - 1) * piece_spacing

                piece.correct_x = correct_x
                piece.correct_y = correct_y

                piece.center_x = random.randint(50, SCREEN_WIDTH - 50)
                piece.center_y = random.randint(50, SCREEN_HEIGHT - 50)

                piece.row = row
                piece.col = col
                piece.group = set([piece])

                self.piece_list.append(piece)
                self.piece_grid[(row, col)] = piece

    
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

    def on_mouse_press(self, x, y, button, modifiers):
        pieces = arcade.get_sprites_at_point((x, y), self.piece_list)
        if pieces:
            self.held_piece = pieces[-1]

            self.piece_list.remove(self.held_piece)
            self.piece_list.append(self.held_piece)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        if self.held_piece:
            for piece in self.held_piece.group:
                piece.center_x += dx
                piece.center_y += dy

    def on_mouse_release(self, x, y, button, modifiers):
        if self.held_piece:
            snap_distance = 40
            directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
            snapped = False

            for d_row, d_col in directions:
                neighbor_pos = (self.held_piece.row + d_row, self.held_piece.col + d_col)
                neighbor = self.piece_grid.get(neighbor_pos)


                if neighbor:
                    offset_x = d_col * (self.held_piece.width / 2 + neighbor.width / 2)
                    offset_y = -d_row * (self.held_piece.height / 2 + neighbor.height / 2)
                    
                    expected_x = neighbor.center_x + offset_x
                    expected_y = neighbor.center_y + offset_y

                    dx = self.held_piece.center_x - expected_x
                    dy = self.held_piece.center_y - expected_y
                    distance = (dx**2 + dy**2) ** 0.5

                    if distance < snap_distance:
                        self.held_piece.center_x = expected_x
                        self.held_piece.center_y = expected_y
                        combined_group = self.held_piece.group.union(neighbor.group)
                        for p in combined_group:
                            p.group = combined_group
                        snapped = True
            

            self.held_piece = None

    def on_draw(self):
        # method automatically called to draw everything on screen.
        self.clear()
        # this line clears the screen and gets it ready for new drawings.
        # after this you might draw sprites and text
        if self.current_screen == "WELCOME":
            arcade.set_background_color(arcade.color.PINK_LAVENDER)
            self.ui_manager.draw()
        elif self.current_screen == "GAME":
            arcade.draw_texture_rect(self.background, rect=arcade.LBWH(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT))
            self.piece_list.draw()
        # sets the background image

    def on_update(self, delta_time):
        # this is automatically called many times per second.
        # delta_time is how much time has passed since the last frame.
        # mostly used for animations/movement
        # you would add game logic here, such as update
        self.piece_list.update()

    # will need to add some more functions such as on_mouse_press() or on_mouse_drag() to support dragging.

if __name__ == "__main__":
    game = MyGame()
    game.setup()
    arcade.run()