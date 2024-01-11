import pygame, json
from lib.tile import Tile

class TileManager:

    def __init__(self, jsonfile, tilemap):
        self.tilepallet = []
        self.tiles = []
        self.initTiles(tilemap)
        self.loadTiles(jsonfile)

    def loop(self):
        for tile in self.tiles:
            tile.loop()

    def loadTiles(self, jsonfile):
        x, y = 0, 0
        with open(jsonfile) as f:
            content = f.read()
        data = json.loads(content)
        for tileindex in data["tiles"]:
            tile = Tile(self, tileindex)
            tile.x = tile.image.get_width() * x
            tile.y = tile.image.get_height() * y
            self.tiles.append(tile)
            x += 1
            if x >= 40:
                x = 0
                y += 1

    def initTiles(self, tilemap):
        ss = pygame.image.load(tilemap)
        for y in range(20):
            for x in range(9):
                self.tilepallet.append(ss.subsurface((16 * x, 16 * y, 16, 16)))
        blanks = [5,6,7,8,31,40,44,53,58,78,90,91,95,96,97,107,116,125,134,143,152,161,170,179]
        self.tilepallet = self.remove_elements_at_indices(self.tilepallet, blanks)

    def remove_elements_at_indices(self, test_list, idx_list):
        if not idx_list:
            return test_list
        first_idx = idx_list[0]
        rest_of_indices = idx_list[1:]
        sub_list = self.remove_elements_at_indices(test_list, rest_of_indices)
        sub_list.pop(first_idx)
        return sub_list