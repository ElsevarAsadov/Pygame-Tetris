import pygame as pg
from math import gcd

vec = pg.math.Vector2

FPS = 60
CAPTION = "TETRIS"
SCREEN_SIZE = SCREEN_X, SCREEN_Y = 590, 960
GAME_FIELD_SIZE = GAME_FIELD_X, GAME_FIELD_Y = 400, 850

"""

  gcd(420, 860) = 20
  width = (21 - 1) * TILE
  height = (43 - 1) * TILE
  
"""
  
TILE_SIZE = gcd(GAME_FIELD_X, GAME_FIELD_Y)

GAME_AREA_TILE_X, GAME_AREA_TILE_Y = vec(GAME_FIELD_SIZE) / TILE_SIZE
GAME_AREA_TILE_X = int(GAME_AREA_TILE_X)
GAME_AREA_TILE_Y = int(GAME_AREA_TILE_Y)

GAME_AREA_OFFSET = GAME_AREA_OFFSET_X, GAME_AREA_OFFSET_Y = 15, 88 

INITIAL_TETROMINO_OFFSET_X, INITIAL_TETROMINO_OFFSET_Y = GAME_AREA_TILE_X // 2, -2

GAME_AREA_COLOR = "#30272a"
GRID_COLOR = "#000000"


TETROMINO_SHAPES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

MINIMIZED_BLOCK_SIZE = (23, 23)

NEXT_TETROMINO_LOCATION = (485, 235)

MOVEMENT = {"left" : vec(-1, 0), "right" : vec(1, 0), "down" : (0, 1)}

ANIM_TIME_INTERVAL = 150 #millisecond
FAST_ANIM_INTERVAL = 20 #millisecond