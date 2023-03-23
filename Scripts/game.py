from settings import *
import pathlib
import sys


class Tetris():
  def __init__(self) -> None:
    #initiliaze pygame
    pg.init()
    
    self.screen = pg.display.set_mode(WINDOW_RES, vsync=True)
    #FPS locker.
    self.clock = pg.time.Clock()
    
    #loading images:
    self.images = self.__load_images()
    
    
  def run(self):
    pass
  
  
  def __load_images(self):
    files = [file for file in pathlib.Path(ASSET_PATH).rglob(["*.png", "*.jpg"])]