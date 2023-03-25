import os
from settings import *
from objects import Tetromino


class Tetris:
    def __init__(self, app):
        # application class
        self.app = app
        # block sprites is located here.
        self.sprite_g = pg.sprite.Group()

        # game objects
        self.tetromino = Tetromino(self)

    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()

        self.sprite_g.update()

    def draw(self):
        self.show_background()
        self.draw_grid()
        self.sprite_g.draw(self.app.game_srf)
        self.show_game_area()

    def show_background(self):
        bg_path = os.path.join("Assets", "background.jpg")
        bg_img = pg.image.load(bg_path).convert_alpha()
        self.app.screen.blit(bg_img, (0, 0))

    def show_game_area(self):
        x = GAME_AREA_OFFSET_X
        y = GAME_AREA_OFFSET_Y
        self.app.screen.blit(self.app.game_srf, (x, y))
        self.app.game_srf.fill(GAME_AREA_COLOR)

    def draw_grid(self):
        x = GAME_FIELD_X
        y = GAME_FIELD_Y

        color = GRID_COLOR

        for i in range(0, GAME_FIELD_X // TILE_SIZE):
            for j in range(0, GAME_FIELD_Y // TILE_SIZE):
                pg.draw.rect(self.app.game_srf, color, (i * TILE_SIZE,
                             j * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    def handle_user_controls(self, keys):
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.tetromino.move("left")
        elif keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.tetromino.move("right")
            
