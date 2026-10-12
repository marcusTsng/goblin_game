import pygame
from Sprites import Sprite, scale_image
from GameManager import Game, GRAVITY

SPEED = 6
FLOOR_Y = 600
BRIDGE_Y = 300
JUMP_POWER = 12
FALL_POWER = 15

PLAYER_ASSET = "Goblin_1"

last_time_step = 0

class Player(Sprite):
    def __init__(self, x, y, active=True):

        super().__init__(f"Assets/Characters/{PLAYER_ASSET}/idle.png", x, y, active, scale=True)

        self._frames = {
            "idle" : scale_image(pygame.image.load(f"Assets/Characters/{PLAYER_ASSET}/idle.png").convert_alpha()),
            "walk1" : scale_image(pygame.image.load(f"Assets/Characters/{PLAYER_ASSET}/walk1.png").convert_alpha()),
            "walk2" : scale_image(pygame.image.load(f"Assets/Characters/{PLAYER_ASSET}/walk2.png").convert_alpha())
        }
        self.set_frame("idle")

        self._moving = False
        self._jumping = False
        self.on_bridge = False
        self._jump_movement = 0

    def set_frame(self, frame):
        if frame in self._frames:
            self._current_frame = frame
            self.image = self._frames[frame]

    def _handle_animations(self):
        game = Game.get_instance()
        global last_time_step

        if self._jumping:
            self.set_frame("idle") # change later
        elif self._moving:
            if last_time_step < game.time_steps:
                last_time_step = game.time_steps
                if self._current_frame == "walk1": self.set_frame("walk2")
                else: self.set_frame("walk1")
        else:
            self.set_frame("idle")

    def update(self):
        keys = pygame.key.get_pressed()
        dt = Game.get_instance().delta_time

        self._moving = False
        
        if not self._jumping:
            if keys[pygame.K_a]:
                self.move(-SPEED * dt, 0)
                self._moving = True
            if keys[pygame.K_d]:
                self.move(SPEED * dt, 0)
                self._moving = True
        if keys[pygame.K_w] or self._jumping:
            self.jump_onto_bridge()
        if keys[pygame.K_s] or self._jumping:
            self.jump_off_bridge()

        self._handle_animations()

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