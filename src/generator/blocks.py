class Blocks():
    def __init__(self, x: int, y: int, valid: bool = False):
        self.x = x
        self.y = y
        self.valid = valid

    def get_position(self):
        return self.x, self.y
    
    def get_valid(self):
        return self.valid