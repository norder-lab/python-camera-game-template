import pygame


class GameData:
    
    def __init__(self):
        self.running=True

        # フレームレート
        self.FPS=30.0
        
        # 画面の情報を取得
        info = pygame.display.Info()
        
        # 画面のサイズ定義
        self.SCREEN_SIZE=(info.current_w,info.current_h)

