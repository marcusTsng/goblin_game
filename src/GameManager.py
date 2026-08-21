import pygame
from enum import Enum

GRAVITY = 0.05

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

        # game properties
        self.state = GameState.NONE
        self.player = player
    
    @staticmethod
    def get_instance() -> Game:
        return Game.instance
    
    def start_game(self):
        self.state = GameState.INGAME