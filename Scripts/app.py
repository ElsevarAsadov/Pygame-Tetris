from settings import *
from tetris import Tetris
from os import path
class App:
  def __init__(self) -> None:
    pg.init()
    pg.display.set_caption(CAPTION)
    
    self.window = pg.display.set_mode(WIN_RES, vsync=FPS)
    self.tetris_screen = pg.Surface(WIN_RES)
    
    self.clock = pg.time.Clock()
    
    #game objects
    self.tetris = Tetris(self)
    
  def run(self) -> None:
    while 1:
      self.handle_events()
      self.update()
      self.draw()
      
      pg.display.update()
      self.clock.tick(FPS)
  
  def handle_events(self) -> None:
    #window events
    for event in pg.event.get():
      if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
        pg.quit()
        exit(0)
        
    #game events
    
  def update(self) -> None:
    self.tetris.update()
  
  def draw(self) -> None:
    self.show_surface(self.window, self.tetris_screen, (0, 0))
    self.show_background()
    self.tetris.draw()
  
  def show_surface(self, root, surface, pos):
    root.blit(surface, pos)
    
  def show_background(self):
    bg = pg.image.load(path.join("Assets", "background.jpg")).convert_alpha()
    self.tetris_screen.blit(bg, (0, 0))
    
    
  
  
  