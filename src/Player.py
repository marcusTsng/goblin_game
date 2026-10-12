import pygame
from Sprites import Sprite
from GameManager import Game, GRAVITY

SPEED = 6
FLOOR_Y = 600
BRIDGE_Y = 300
JUMP_POWER = 12
FALL_POWER = 15

PLAYER_ASSET = "Goblin_1"

class Player(Sprite):
    def __init__(self, x, y, active=True):
        super().__init__(f"Assets/Characters/{PLAYER_ASSET}/idle.png", x, y, active, scale=True)
        self._jumping = False
        self.on_bridge = False
        self._jump_movement = 0

    def update(self):
        keys = pygame.key.get_pressed()
        dt = Game.get_instance().delta_time
        
        if not self._jumping:
            if keys[pygame.K_a]:
                self.move(-SPEED * dt, 0)
            if keys[pygame.K_d]:
                self.move(SPEED * dt, 0)
        if keys[pygame.K_w] or self._jumping:
            self.jump_onto_bridge()
        if keys[pygame.K_s] or self._jumping:
            self.jump_off_bridge()

    def jump_onto_bridge(self):
        if self.on_bridge: return
        if self._jumping: 
            dt = Game.get_instance().delta_time
            done_jumping = (self._jump_movement < 0) and (self.pos[1] >= BRIDGE_Y)
            
            self.move(0, -self._jump_movement * dt)
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
            dt = Game.get_instance().delta_time
            done_jumping = self.pos[1] >= FLOOR_Y

            self.move(0, -self._jump_movement  * dt)
            self._jump_movement -= GRAVITY

            if done_jumping:
                self._jumping = False
                self.set_pos(self.pos[0], FLOOR_Y)
                self.on_bridge = False
            
            return
        self._jumping = True
        self._jump_movement = -FALL_POWER