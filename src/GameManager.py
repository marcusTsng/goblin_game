import pygame
from enum import Enum

GRAVITY = 0.3
TIME_STEP_SIZE = 0.05

class GameState(Enum):
    NONE = 0
    MENU = 1
    INGAME = 2

class Game:
    instance = None
    def __init__(self, screen, player):
        # singleton
        if Game.instance != None and Game.instance != self: 
            del self
        Game.instance = self
        
        # game setup
        self.screen : pygame.Surface = screen
        self.clock = pygame.time.Clock()

        # game properties
        self.state = GameState.NONE
        self.player = player

        self.delta_time = None
        self.time_passed = 0
        self.time_steps = 0

        self._last_time_step = 0
    
    @staticmethod
    def get_instance() -> Game:
        return Game.instance
    
    def start_game(self):
        self.state = GameState.INGAME

    def tick(self):
        if self.state != GameState.INGAME:
            self.delta_time = self.clock.tick(60) / 10
            self.time_passed = pygame.time.get_ticks() / 1000

            if self.time_passed - self._last_time_step >= TIME_STEP_SIZE:
                self._last_time_step = self.time_passed
                self.time_steps += 1