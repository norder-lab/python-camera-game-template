import sys

import pygame

from modules.camera import Camera
from modules.event import Event
from modules.game_data import GameData
from modules.input import Input
from modules.keys import Keys
from modules.scene_manager import SceneManager
from modules.window import Window


class Game:

    def __init__(self):
        self.running=True
        self.camera=Camera(0)
        self.window=Window()
        self.input=Input()
        self.event=Event(self.input)
        self.game_data=GameData()
        self.scene_manager=SceneManager(self.game_data)

        self.clock=pygame.time.Clock()
    
    def run(self):

        self.scene_manager.change_scene(self.scene_manager.get_title_scene());

        # mainループ
        while self.running:
            
            current_scene=self.scene_manager.get_current_scene()
            
            
            # イベント処理
            self.event.check_event()
            
            # カメラフレーム取得
            surface, frame=self.camera.get_frame(self.game_data.SCREEN_SIZE)

            # ロジック処理
            current_scene.logic(self.input)
            
            # 描画処理
            self.window.render(current_scene, surface)
            
            # fps処理
            self.clock.tick(self.game_data.FPS)
            
            
            # 終了処理
            if self.input.get_key_state(Keys.ESC):
                self.running=False
            
        self.exit()

    def exit(self):
        self.camera.close()
        pygame.quit()
        sys.exit()
