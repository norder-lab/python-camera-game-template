import time


class AnimationTime:
    def __init__(self, animation_time):
        self.is_animating = False
        self.start_time = time.time()
        self.animation_time = animation_time

    def start(self):
        self.is_animating = True
        self.start_time = time.time()

    def get_is_animating(self):
        if self.animation_time < (time.time() - self.start_time):
            self.is_animating = False
        return self.is_animating

    def get_elapsed_time(self):
        if self.is_animating:
            return time.time() - self.start_time
        else:
            return 0
    
    def get_progress(self):
        if self.is_animating:
            return (time.time() - self.start_time) / self.animation_time
        else:
            return 0.0

