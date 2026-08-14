import pygame

from Sprites import Sprite, Text, Fonts, Button
from GameManager import Game, GameState
from Player import Player

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("goblin game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    game = Game(screen=screen)
    game.state = GameState.MENU

    # Menu sprites
    play_button = Button("Assets/Buttons/test_button.png", 400, 400, "play", callback=game.start_game)
    title = Text("goblin game title", Fonts.default, (200, 100), (255,255,255))
    menu_elements = [play_button, title]
    # In game sprites
    player = Player(400, 600, False)

    # GAME LOOP
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            Button.handle_buttons(event)

        # MENU SCREEN
        if game.state == GameState.MENU:
            for x in menu_elements:
                x.set_active(True)
        elif game.state == GameState.INGAME: 
            for x in menu_elements:
                x.set_active(False)
            player.set_active(True)
        
        screen.fill((255,255,255))
        Sprite.all_sprites.update()
        Sprite.all_sprites.draw(screen)
        Text.draw_all(screen)
        pygame.display.flip()
    pygame.quit()