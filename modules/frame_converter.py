import cv2
import pygame


class FrameConverter:
    def cv_to_pygame(self, frame, screen_size):
        frame = cv2.flip(frame, 1)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        h, w = frame.shape[:2]
        new_w = int(screen_size[0])
        new_h = int(screen_size[0] / w * h)
        frame = cv2.resize(frame, (new_w, new_h), interpolation=cv2.INTER_NEAREST)

        shape = (new_w, new_h)
        surface = pygame.image.frombuffer(frame.data, shape, 'RGB')

        return surface, frame
