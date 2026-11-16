import pygame


class Window:
    
    def __init__(self):
        # 初期化
        pygame.init()
        
        # 画面の情報を取得
        info = pygame.display.Info()
        
        # 画面のサイズ定義
        self.SCREEN_SIZE=(info.current_w,info.current_h)
        
        # スクリーンのサイズ設定･取得
        self.screen=pygame.display.set_mode(self.SCREEN_SIZE,pygame.FULLSCREEN|pygame.SCALED)
        
        # タイトル設定
        pygame.display.set_caption("game")

    def render(self, current_scene, surface):
        #背景:黒
        self.screen.fill((200,200,200)) 
        
        # カメラフレーム描画
        self.screen.blit(surface,(0,0))
        
        # 現在の画面を描画
        current_scene.render(self.screen)
        
        pygame.display.update()
