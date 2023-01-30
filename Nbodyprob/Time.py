import datetime

class Time:
    def __init__(self, x):
        self.x = x
    
    def update(self, dt):
        self.x = self.x + datetime.timedelta(seconds=dt)
