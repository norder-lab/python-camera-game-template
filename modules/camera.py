import cv2

from modules.frame_converter import FrameConverter

class Camera:
    def __init__(self,camera_number):
        self.frame_converter=FrameConverter()
        self.cap=cv2.VideoCapture(camera_number)
        self.cap.set(cv2.CAP_PROP_FPS,30)
        
        """ 解像度を設定する場合
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,480)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,640)
        
        print(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        print(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        """
        
    def get_frame(self,size):
        success,frame = self.cap.read() # カメラフレーム取得
        
        if(success):
            converted_frame=self.frame_converter.cv_to_pygame(frame,size)# pygameのsurfaceに変換する
            return converted_frame
        else:
            return None
        
    def close(self):
        self.cap.release()
        cv2.destroyAllWindows()