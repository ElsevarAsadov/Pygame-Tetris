from settings import *
from objects import Tetromino

class Tetris:
  def __init__(self, app) -> None:
    self.app = app
  
    self.sprite_group = pg.sprite.Group()
    
    #game objects
    self.tetromino = Tetromino(self)
  def update(self) -> None:
    self.sprite_group.update()
    self.tetromino.update()
  def draw(self) -> None:
    self.sprite_group.draw(self.app.tetris_screen)
    
  