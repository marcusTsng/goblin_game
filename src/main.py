import pygame

from Sprites import Sprite, Text, Fonts, Button
from Items import Item, Pebble
from GameManager import Game, GameState
from Player import Player
from Enemies import Enemy

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 800

if __name__ == "__main__":
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption("goblin game")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(400, 600, False)
    game = Game(screen=screen, player=player)
    game.state = GameState.MENU

    # In game sprites
    pebbles = Pebble((100, 600))
    Item.holding = pebbles

    # Menu sprites
    play_button = Button("Assets/Buttons/test_button.png", 400, 400, "play", callback=game.start_game)
    title = Text("goblin game title", Fonts.default, (200, 100), (255,255,255))
    menu_elements = [play_button, title]

    # GAME LOOP
    running = True
    while running:
        game.tick()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                running = False

            Button.handle_buttons(event)

        # MENU SCREEN
        if game.state == GameState.MENU:
            for x in menu_elements:
                x.set_active(True)
            for x in Item.items:
                x.source.set_active(False)
        elif game.state == GameState.INGAME: 
            for x in menu_elements:
                x.set_active(False)
            for x in Item.items:
                x.source.set_active(True)
            player.set_active(True)
        
        # ENEMY SPAWN
        Enemy.handle_enemy_spawns()

        screen.fill((255,255,255))
        Sprite.all_sprites.update()
        Item.update()
        Sprite.all_sprites.draw(screen)
        Text.draw_all(screen)
        pygame.display.flip()
    pygame.quit()