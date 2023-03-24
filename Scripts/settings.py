import pygame as pg

vec = pg.math.Vector2

FPS = 60
WIN_RES = WIN_X, WIN_Y = 590, 960
GAME_FIELD_RES = GAME_FIELD_X, GAME_FIELD_Y = 400, 850

GAME_FIELD_OFFSET = 13, 97
TILE_SIZE = 25
CAPTION = "TETRIS"

ASSET_PATH = "Assets"


TETROMINOES = {
    'T': [(0, 0), (1, 0), (1, -1), (2, 0)],
    'O': [(0, 0), (1, 0), (0, 1), (1, 1)],
    'J': [(0, 0), (0, 1), (1, 1), (2, 1)],
    'L': [(0, 0), (0, 1), (-1, 1), (-2, 1)],
    'I': [(0, 0), (1, 0), (2, 0), (3, 0)],
    'S': [(0, 0), (-1, 0), (-1, 1), (-2, 1)],
    'Z': [(0, 0), (1, 0), (1, 1), (2, 1)]
}

MOVEMENT = {"left" : vec(-1, 0), "right" : vec(1, 0), "down" : (0, 1)}
