import pygame
from Sprites import Sprite
from GameManager import Game, GRAVITY

PEBBLE_SPEED = 20
PEBBLE_WEIGHT = GRAVITY * 8
PEBBLE_DESPAWN_HEIGHT = 700

class Item:
    items = []
    holding = None
    def __init__(self, source_image : str, source_pos : tuple):
        self.source = Sprite(source_image, source_pos[0], source_pos[1], False)
        Item.items.append(self)

        self.equipped = False

    def activate(self): pass

    def set_equip(self, bool : bool): 
        self.equipped = bool
        if bool: Item.holding = self
        else: Item.holding = None

    @staticmethod
    def update():
        if Item.holding: Item.holding.update()

class Pebble(Item):
    def __init__(self, source_pos):
        super().__init__("Assets/placeholder.png", source_pos)
        self.pebble = None
        self._dir = (0,0)

    def activate(self):
        if self.pebble:
            self.pebble.move(self._dir[0], self._dir[1])
            self._dir = (self._dir[0], self._dir[1]+PEBBLE_WEIGHT)

            if self.pebble.pos[1] >= PEBBLE_DESPAWN_HEIGHT:
                self.pebble.destroy()
                self.pebble = None
        else:
            plr = Game.get_instance().player
            x, y = plr.pos
            self.pebble = Sprite("Assets/placeholder.png", x, y)

            mx, my = pygame.mouse.get_pos()
            self._dir = pygame.math.Vector2(mx - x, my - y).normalize() * PEBBLE_SPEED

    def set_equip(self, bool):
        return super().set_equip(bool)
        # discard/drop pebble

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q] or self.pebble:
            self.activate()