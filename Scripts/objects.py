from settings import *
from random import choice


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos):
        offset_x = INITIAL_TETROMINO_OFFSET_X
        offset_y = INITIAL_TETROMINO_OFFSET_Y

        self.tetromino = tetromino
        super().__init__(self.tetromino.tetris.sprite_g)

        self.pos = vec(pos) + vec(offset_x, offset_y)
        self.image = pg.Surface((TILE_SIZE, TILE_SIZE))
        self.image.fill("orange")
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = self.pos * TILE_SIZE


class Tetromino:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = choice([*TETROMINO_SHAPES.keys()])
        self.blocks = [Block(self, pos)
                       for pos in TETROMINO_SHAPES[self.shape]]

    def update(self):
        self.move()

    def move(self, direction="down"):
        # adding new position to the block
        move_direction = MOVEMENT[direction]
        for block in self.blocks:
            block.pos += move_direction
