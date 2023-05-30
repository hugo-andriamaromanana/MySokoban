from utils.json_func import get_json
from os import path

class Map():

    def __init__(self,current_map: str, size: int = 10):
        self.grid = [[0 for _ in range(size)]
                     for _ in range(size)]
        self.grid = [[1]+row[1:] for row in self.grid]
        self.grid = [row[:-1]+[1] for row in self.grid]
        self.grid[0] = [1 for _ in range(size)]
        self.grid[-1] = [1 for _ in range(size)]
        self.add_obstacles(self.select_level(current_map))

    def select_level(self,current_map: str):
        return get_json(path.join(path.dirname(__file__), '..', '..', 'src', 'generator', 'base', 'obstacles.json'))[current_map]
    
    def add_obstacles(self,obstacles: list):
        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[1]] = 1

    def print_map(self):
        for row in self.grid:
            print(row)

first_map = Map("Easy")

first_map.print_map()

# print(get_json(path.join(path.dirname(__file__), '..', '..', 'src', 'generator', 'base', 'obstacles.json'))['Easy'])
