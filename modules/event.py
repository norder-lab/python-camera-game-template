from pygame.locals import *
from modules.keys import Keys
import pygame

class Event:
    def __init__(self,input):
        self.input=input

    def check_event(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:  # キーを押したとき
                self.input.key_pressed(Keys.convert_key(event.key))
            if event.type == KEYUP: #キーを離したとき
                self.input.key_released(Keys.convert_key(event.key))