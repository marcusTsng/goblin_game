import pygame
from enum import Enum

GRAVITY = 0.3

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
    
    @staticmethod
    def get_instance() -> Game:
        return Game.instance
    
    def start_game(self):
        self.state = GameState.INGAME

    def tick(self):
        self.delta_time = self.clock.tick(60) / 10