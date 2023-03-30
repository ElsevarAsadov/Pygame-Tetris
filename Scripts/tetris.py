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
        self.next_tetromino = Tetromino(self, current=False)

        # game map grid:
        self.field_array = self.get_field()

    def update(self):
        if self.app.anim_trigger:
            self.tetromino.update()
            self.check_tetromino_landing()
            self.check_full_lines()
        self.sprite_g.update()
        
    def draw(self):
        self.show_background()
        self.show_game_area()
        self.draw_grid()
        self.sprite_g.draw(self.app.game_srf)

    def show_background(self):
        bg_path = os.path.join("Assets", "background.jpg")
        bg_img = pg.image.load(bg_path).convert_alpha()
        self.app.screen.blit(bg_img, (0, 0))

    def get_field(self):
        x = GAME_AREA_TILE_X
        y = GAME_AREA_TILE_Y

        return [[0 for i in range(0, x)] for j in range(0, y)]

    def put_tetromino_blocks_in_array(self):
        for block in self.tetromino.blocks:
            x, y = int(block.pos.x), int(block.pos.y)
            self.field_array[y][x] = block

    def show_game_area(self):
        
        area_path = os.path.join("Assets", "gamearea.jpg")
        area_img = pg.image.load(area_path).convert_alpha()
        
        x = GAME_AREA_OFFSET_X
        y = GAME_AREA_OFFSET_Y
        self.app.screen.blit(self.app.game_srf, (x, y))
        self.app.game_srf.blit(area_img, (0,0))
        #self.app.game_srf.fill("green")
        #self.app.game_srf.set_colorkey("green")

    def draw_grid(self):
        x = GAME_FIELD_X
        y = GAME_FIELD_Y

        color = GRID_COLOR

        for i in range(0, GAME_FIELD_X // TILE_SIZE):
            for j in range(0, GAME_FIELD_Y // TILE_SIZE):
                pg.draw.rect(self.app.game_srf, color, (i * TILE_SIZE,
                             j * TILE_SIZE, TILE_SIZE, TILE_SIZE), 1)

    # def show_next_tetromino(self):
    #     blocks = self.next_tetromino.blocks
    #     for block in blocks:
    #         self.app.screen.blit(block, "")
    
    def check_tetromino_landing(self):
        if self.tetromino.landing:
            if self.is_game_over():
                pg.time.wait(300)
                self.__init__(self.app)
            else:
                self.put_tetromino_blocks_in_array()
                self.tetromino = self.next_tetromino
                self.tetromino.current = True
                self.next_tetromino = Tetromino(self, current=False)

    def check_full_lines(self):
        fx = GAME_AREA_TILE_X
        fy = GAME_AREA_TILE_Y
        row = fy - 1
        for y in range(fy - 1, -1, -1):
            for x in range(fx):
                self.field_array[row][x] = self.field_array[y][x]

                if self.field_array[y][x]:
                    self.field_array[row][x].pos = vec(x, y)

            if sum(map(bool, self.field_array[y])) < fx:
                row -= 1
            else:
                for x in range(fx):
                    #self.field_array[row][x].alive = False
                    self.field_array[row][x] = 0

                #self.full_lines += 1

    def is_game_over(self):
        for block in self.tetromino.blocks:
            if block.pos.y < 0:
                pg.time.wait(300)
                return True

    def controls(self, e):
        self.tetromino.controls(e)
