import pygame
from Sprites import Sprite, scale_image
from GameManager import Game, GRAVITY


class Enemy(Sprite):
    def __init__(self, x, y, frames : list, active=True):
        
        super().__init__(f"Assets/Enemies/{frames[0]}", x, y, active, scale=True)

        self._frames = frames
        self.set_frame(0)

    def set_frame(self, frame_no : int):
        if len(self._frames) <= frame_no:
            self._current_frame = self._frames[frame_no]
            self.image = self._frames[frame_no]

    def _handle_animations(self):
        pass
        # game = Game.get_instance()
        # global last_time_step

        # if self._jumping:
        #     self.set_frame("idle") # change later
        # elif self._moving:
        #     if last_time_step < game.time_steps:
        #         last_time_step = game.time_steps
        #         if self._current_frame == "walk1": self.set_frame("walk2")
        #         else: self.set_frame("walk1")
        # else:
        #     self.set_frame("idle")

    def update(self):
        dt = Game.get_instance().delta_time
        self._handle_animations()

    @staticmethod
    def handle_enemy_spawns():
        pass