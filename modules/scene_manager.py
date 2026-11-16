from modules.game_scene import GameScene
from modules.title_scene import TitleScene


class SceneManager:
    def __init__(self, game_data):
        self.game_data = game_data
        self.TITLE_SCENE = TitleScene(self, game_data)
        self.GAME_SCENE = None
        self.current_scene=None

    def change_scene(self,scene):
        self.current_scene=scene

    def get_current_scene(self):
        return self.current_scene

    def get_title_scene(self):
        return self.TITLE_SCENE
    
    def get_game_scene(self):
        return GameScene(self, self.game_data)
