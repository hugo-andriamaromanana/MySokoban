from utils.json_func import get_json
from os import path
from player import Player
import time
from blocks import Blocks
from plates import Plates


class Map():

    def __init__(self, current_map: str, size: int = 10, player: Player = Player(), blocks: list = [], plates: list = []):

        self.grid = [[0 for _ in range(size)]
                     for _ in range(size)]
        self.grid = [[1]+row[1:] for row in self.grid]
        self.grid = [row[:-1]+[1] for row in self.grid]
        self.grid[0] = [1 for _ in range(size)]
        self.grid[-1] = [1 for _ in range(size)]

        self.add_obstacles(self.select_map(current_map))
        self.player = player
        self.blocks = blocks
        self.plates = plates

    def select_map(self, current_map: str):

        return get_json(path.join(path.dirname(__file__), '..', '..', 'src', 'generator', 'base', 'obstacles.json'))[current_map]

    def plates_generator(self, current_map: str):

        plates_pos = get_json(path.join(path.dirname(
            __file__), '..', '..', 'src', 'generator', 'base', 'plates.json'))[current_map]
        for plate in plates_pos:
            self.plates.append(Plates(plate[0], plate[1]))
        return plates_pos

    def blocks_generator(self, current_map: str):

        blocks_pos = get_json(path.join(path.dirname(
            __file__), '..', '..', 'src', 'generator', 'base', 'blocks.json'))[current_map]
        for block in blocks_pos:
            self.blocks.append(Blocks(block[0], block[1]))
        return blocks_pos

    def add_obstacles(self, obstacles: list):

        for obstacle in obstacles:
            self.grid[obstacle[0]][obstacle[-1]] = 1

    def add_blocks(self, blocks: list):

        for block in blocks:
            self.grid[block[0]][block[-1]] = 2

    def add_plates(self, plates: list):

        for plate in plates:
            self.grid[plate[0]][plate[-1]] = 3

    def add_player_on_map(self):

        self.grid[self.player.y][self.player.x] = 4

    def print_map(self):

        self.refresh_map_state()
        for row in self.grid:
            print(row)

    def get_map(self):

        return self.grid

    def move_player(self, direction: str):

        if direction == "UP" and not (self.detect_collision("UP")):
            self.player.move("UP")
        elif direction == "DOWN" and not (self.detect_collision("DOWN")):
            self.player.move("DOWN")
        elif direction == "LEFT" and not (self.detect_collision("LEFT")):
            self.player.move("LEFT")
        elif direction == "RIGHT" and not (self.detect_collision("RIGHT")):
            self.player.move("RIGHT")

    def refresh_map_state(self):

        self.grid = [[0 for _ in range(len(self.grid))]
                     for _ in range(len(self.grid))]
        self.grid = [[1]+row[1:] for row in self.grid]
        self.grid = [row[:-1]+[1] for row in self.grid]
        self.grid[0] = [1 for _ in range(len(self.grid))]
        self.grid[-1] = [1 for _ in range(len(self.grid))]

        self.add_obstacles(self.select_map("Easy"))
        self.add_blocks(self.blocks)
        self.add_plates(self.plates_generator("Easy"))
        self.add_player_on_map()

    def detect_collision(self, direction: str):
            
        if direction == "UP":
            return self.grid[self.player.y-1][self.player.x] == 1
        elif direction == "DOWN":
            return self.grid[self.player.y+1][self.player.x] == 1
        elif direction == "LEFT":
            return self.grid[self.player.y][self.player.x-1] == 1
        elif direction == "RIGHT":
            return self.grid[self.player.y][self.player.x+1] == 1


map = Map("Easy")

map.move_player("UP")
map.move_player("UP")
map.move_player("UP")

map.print_map()