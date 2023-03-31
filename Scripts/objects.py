from settings import *
from random import choice


class Block(pg.sprite.Sprite):
    def __init__(self, tetromino, pos, img):
        offset_x = INITIAL_TETROMINO_OFFSET_X
        offset_y = INITIAL_TETROMINO_OFFSET_Y
        self.tetromino = tetromino
        super().__init__(self.tetromino.tetris.sprite_g)

        self.pos = vec(pos) + vec(offset_x, offset_y)
        self.next_pos = vec(pos)
        
        self.image = img.convert_alpha()
        self.rect = self.image.get_rect()
        
        self.alive = True
        
    
    def rotate(self, pivot_pos):
        translated = self.pos - pivot_pos
        rotated = translated.rotate(90)
        return rotated + pivot_pos
    

    def update(self):
        if self.tetromino.current:
            self.rect.topleft = self.pos * TILE_SIZE
            self.image =  self.tetromino.img
        else:
            self.rect.topleft = self.next_pos * TILE_SIZE
            self.image =  self.tetromino.img
        
        if not self.alive:
            self.kill()
        
            
    def is_collide(self, pos):
        fx = GAME_AREA_TILE_X
        fy = GAME_AREA_TILE_Y
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < fx and y < fy and (
                y < 0 or not self.tetromino.tetris.field_array[y][x]):
            return False
        return True

class Tetromino:
    def __init__(self, tetris, current=True):
        self.current = current
        self.tetris = tetris
        self.shape = choice([*TETROMINO_SHAPES.keys()])
        
        self.img = choice(self.tetris.app.images)
        self.img_minimized = pg.transform.scale(self.img, MINIMIZED_BLOCK_SIZE)
            
        self.blocks = [Block(self, pos, self.img)
                       for pos in TETROMINO_SHAPES[self.shape]]
        
        self.landing = False

    def update(self):
        self.move()
        
    def is_collide(self, new_block_positions):
        return any(map(Block.is_collide, self.blocks, new_block_positions))
    
    def rotate(self):
        pivot_pos = self.blocks[0].pos
        new_block_positions = [block.rotate(pivot_pos) for block in self.blocks]

        if not self.is_collide(new_block_positions):
            for i, block in enumerate(self.blocks):
                block.pos = new_block_positions[i]
        
    def move(self, direction="down"):
        # adding new position to the block
        move_direction = MOVEMENT[direction]
        
        #next step positions
        new_block_positions = [block.pos + move_direction for block in self.blocks]
        
        is_collide = self.is_collide(new_block_positions)
        if not is_collide:
            for block in self.blocks:
                block.pos += move_direction
        
        elif direction == 'down':
            self.landing = True

    def controls(self, e):
        #key map
        keys = pg.key.get_pressed()
        
        if e.type == self.tetris.app.animation_event:
            self.tetris.app.anim_trigger = True
            self.handle_user_controls(keys, type="normal")
        
        elif e.type == self.tetris.app.fast_movement_event:
            self.tetris.app.fast_anim_trigger = True
            self.handle_user_controls(keys, type="fast")
        
        elif keys[pg.K_UP]:
            self.rotate()
            
    
    def handle_user_controls(self, keys, type):
        if type == "normal":
            if keys[pg.K_a] or keys[pg.K_LEFT]:
                self.move("left")
            elif keys[pg.K_d] or keys[pg.K_RIGHT]:
                self.move("right")
        
        elif type == "fast":
            if keys[pg.K_d] or keys[pg.K_DOWN]:
                self.move("down")