from settings import *
from random import choice

class Block(pg.sprite.Sprite):
  def __init__(self, tetromino, pos) -> None:
    self.tetromino = tetromino
    
    super().__init__(tetromino.tetris.sprite_group)
    
    self.pos = vec(pos) + (9, 0)
    
    self.image = pg.Surface((TILE_SIZE,TILE_SIZE))
    self.image.fill("orange")
    self.rect = self.image.get_rect()
    
  def update(self):
    self.rect.topleft = self.pos * TILE_SIZE + GAME_FIELD_OFFSET
    
class Tetromino:
  def __init__(self, tetris) -> None:
    self.tetris = tetris
    shape = choice([*TETROMINOES.keys()])
    self.blocks = [Block(self, pos) for pos in TETROMINOES["L"]]


  def move(self, direction):
    for block in self.blocks:
      block.pos += MOVEMENT[direction]
  
  
  def update(self):
    self.move("down")
  