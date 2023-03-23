import pygame as pg

GAME_TITLE = "TETRIS"
TILE_SIZE = 50

FIELD_SIZE = FIELD_W, FIELD_H = 10, 16 #500x800 resolution
FIELD_RES = FIELD_W * TILE_SIZE, FIELD_H * TILE_SIZE
FIELD_SCALE_W, FIELD_SCALE_H = 1.0, 1.0

WINDOW_RES = WIN_W, WIN_H = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

GAME_FPS = 60
