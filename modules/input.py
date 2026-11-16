from modules.keys import Keys

class Input:
    
    def __init__(self):
        # キーの状態
        self.is_keys_pressed={key: False for key in Keys}
    
    # 指定のキーを押す
    def key_pressed(self,key):
        self.is_keys_pressed[key]=True
            
    # 指定のキーを離す
    def key_released(self,key):
        self.is_keys_pressed[key]=False
            
    # キーの状態を返す
    def get_key_state(self,key):
        return self.is_keys_pressed[key]
        