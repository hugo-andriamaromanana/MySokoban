import time

class Player():

    def __init__(self, facing: str = "RIGHT", x: int = 1, y: int = 1, time_elapsed: float = 0.0):
        self.facing = facing
        self.x = x
        self.y = y
        self.time_elapsed = time_elapsed

    def move(self, direction: str):
        if direction == "UP":
            self.y -= 1
            self.facing = "UP"
        elif direction == "DOWN":
            self.y += 1
            self.facing = "DOWN"
        elif direction == "LEFT":
            self.x -= 1
            self.facing = "LEFT"
        elif direction == "RIGHT":
            self.x += 1
            self.facing = "RIGHT"
        else:
            raise ValueError("Invalid direction")
        
    def get_position(self):
        return self.x, self.y
    
    def get_facing(self):
        return self.facing