from settings import *
from tetris import Tetris
from objects import Tetromino

class Game:
  def __init__(self):
    pg.init()
    pg.display.set_caption(CAPTION)
    
    self.screen = pg.display.set_mode(SCREEN_SIZE, vsync=FPS)
    self.game_srf = pg.Surface(GAME_FIELD_SIZE)
    self.clock = pg.time.Clock()
    
    self.set_timer()
    
    #game objects
    self.tetris = Tetris(self)
    
  def run(self):
    while 1:
      self.handle_events()
      self.update()
      self.draw()
      
      pg.display.flip()
      self.clock.tick(FPS)
  
  def handle_events(self):
    #user events flags
    self.anim_trigger = False
    self.fast_anim_trigger = False
    #game window events
    for e in pg.event.get():
      
      if e.type == pg.QUIT:
        pg.quit()
        exit(0)
        
      self.tetris.controls(e)
        
  def update(self):
    self.tetris.update()
  
  def draw(self):
    self.tetris.draw()
    
  def set_timer(self):
    self.animation_event = pg.USEREVENT + 0
    pg.time.set_timer(self.animation_event, ANIM_TIME_INTERVAL)
    self.fast_movement_event = pg.USEREVENT + 1
    pg.time.set_timer(self.fast_movement_event, FAST_ANIM_INTERVAL)