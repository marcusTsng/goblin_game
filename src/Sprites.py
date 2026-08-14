import pygame
from enum import Enum

pygame.init() 

class Sprite(pygame.sprite.Sprite):
    all_sprites = pygame.sprite.Group()

    def __init__(self, image, x, y, active=True):
        super().__init__() 

        self.active = active

        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = (x, y)

        if active:
            Sprite.all_sprites.add(self)

    def set_pos(self, x, y):
        self.pos = (x,y)
        self.rect.center = (x, y)

    def move(self, x, y):
        self.set_pos(self.pos[0] + x, self.pos[1] + y)

    def set_active(self, active : bool):
        self.active = active
        if active: 
            Sprite.all_sprites.add(self)
        else: 
            Sprite.all_sprites.remove(self)

    def destroy(self):
        Sprite.all_sprites.remove(self)
        del self

class Fonts(Enum):
        default = pygame.font.SysFont("Arial", 50)
class Text:
    all_text = []
    
    def __init__(self, text, font : Fonts, pos : tuple, color : tuple):
        self.active = True

        self.surface = font.value.render(text, True, color)
        self.rect = self.surface.get_rect()
        self.rect.center = pos
        
        Text.all_text.append(self)

    def set_pos(self, x, y):
        self.rect.center = (x, y)

    def set_active(self, active: bool):
        self.active = active

    def destroy(self):
        Text.all_text.remove(self)
        del self

    def draw(self, screen : pygame.Surface):
        screen.blit(self.surface, self.rect)
    
    @staticmethod
    def draw_all(screen):
        for x in Text.all_text:
            if x.active:
                x.draw(screen)

class Button(Sprite):
    buttons = []
    def __init__(self, image, x, y, text="", font=Fonts.default, text_color=(255, 255, 255), callback=None):
        super().__init__(image, x, y)
        self.callback = callback
        self.is_hovered = False

        self.text_label = None
        if text:
            self.text_label = Text(text, font, (x, y), text_color)

        Button.buttons.append(self)

    def set_pos(self, x, y):
        super().set_pos(x, y)
        if self.text_label:
            self.text_label.set_pos(x, y)

    def set_active(self, active: bool):
        super().set_active(active)
        if self.text_label:
            self.text_label.set_active(active)

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)

    def handle_event(self, event):
        if not self.active:
            return False

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # 1 = Left Click
            if self.rect.collidepoint(event.pos):
                if self.callback:
                    self.callback()
                return True
        return False

    def destroy(self):
        if self.text_label:
            self.text_label.destroy()
            self.text_label = None
        super().destroy()

    @staticmethod
    def handle_buttons(event):
        for button in Button.buttons:
            if button.active:
                button.handle_event(event)