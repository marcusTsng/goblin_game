import pygame
from Sprites import Sprite
from GameManager import Game, GRAVITY

SPEED = 0.8
FLOOR_Y = 600
BRIDGE_Y = 300
JUMP_POWER = 6
FALL_POWER = 4

class Player(Sprite):
    def __init__(self, x, y, active=True):
        super().__init__("Assets/placeholder.png", x, y, active)
        self._jumping = False
        self.on_bridge = False
        self._jump_movement = 0

    def update(self):
        keys = pygame.key.get_pressed()
        
        if not self._jumping:
            if keys[pygame.K_a]:
                self.move(-SPEED, 0)
            if keys[pygame.K_d]:
                self.move(SPEED, 0)
        if keys[pygame.K_w] or self._jumping:
            self.jump_onto_bridge()
        if keys[pygame.K_s] or self._jumping:
            self.jump_off_bridge()

    def jump_onto_bridge(self):
        if self.on_bridge: return
        if self._jumping: 
            done_jumping = (self._jump_movement < 0) and (self.pos[1] >= BRIDGE_Y)
            
            self.move(0, -self._jump_movement)
            self._jump_movement -= GRAVITY

            if done_jumping: 
                self._jumping = False 
                self.set_pos(self.pos[0], BRIDGE_Y)
                self.on_bridge = True

            return 
        self._jumping = True
        self._jump_movement = JUMP_POWER

    def jump_off_bridge(self):
        if not self.on_bridge: return
        if self._jumping: 
            done_jumping = self.pos[1] >= FLOOR_Y

            self.move(0, -self._jump_movement)
            self._jump_movement -= GRAVITY

            if done_jumping:
                self._jumping = False
                self.set_pos(self.pos[0], FLOOR_Y)
                self.on_bridge = False
            
            return
        self._jumping = True
        self._jump_movement = -FALL_POWER