from settings import *
from tetris import Tetris
from sys import exit
import os
import pathlib

class Game:
  def __init__(self):
    pg.init()
    pg.display.set_caption(CAPTION)
    
    self.screen = pg.display.set_mode(SCREEN_SIZE, vsync=FPS)
    self.game_srf = pg.Surface(GAME_FIELD_SIZE)
    self.clock = pg.time.Clock()
    
    self.images = self.load_images()
    self.sounds = self.load_sounds()
    self.set_timer()
    
    pg.display.set_icon(pg.transform.scale(self.images[0], (25,25)))
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
        exit()
        
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
  
  def load_images(self):
    
    images = pathlib.Path("Assets").rglob(r"[0-5].png")
    
    images = [pg.image.load(image).convert_alpha() for image in images]
    
    images = [pg.transform.scale(image, (TILE_SIZE, TILE_SIZE)) for image in images]
    
    return images
  

  def load_sounds(self):
    sounds = {}
    for root, dirnames, file in os.walk("Music"):
      for filename in file:
        path = os.path.join(root, filename)
        name = filename.split(".")[0]
        sounds[name] = pg.mixer.Sound(path)
    
    return sounds
  