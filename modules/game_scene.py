from modules.keys import Keys
from modules.scene import Scene
from modules.ui_compornents import *


class GameScene(Scene):

    def __init__(self, scene_manager, game_data):
        self.scene_manager=scene_manager
        self.game_data=game_data

    def logic(self,input):
        pass # TODO: write logic

    def render(self,screen):
        # SAMPLE
        draw_ui_sample(screen, self.game_data.SCREEN_SIZE, (200, 200, 200))
        pass # TODO: write render
