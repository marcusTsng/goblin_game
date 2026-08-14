import pygame
from enum import Enum

class GameState(Enum):
    NONE = 0
    MENU = 1
    INGAME = 2

class Game:
    instance = None
    def __init__(self, screen):
        # singleton
        if Game.instance != None and Game.instance != self: 
            del self
        Game.instance = self
        
        # game setup
        self.screen : pygame.Surface = screen

        # game properties
        self.state = GameState.NONE
    
    @staticmethod
    def get_instance() -> Game:
        return Game.instance
    
    def start_game(self):
        self.state = GameState.INGAME