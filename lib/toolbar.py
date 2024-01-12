import pygame
from lib.plant import Plant

class Toolbar:

    def __init__(self, core):
        self.core = core
        self.initSprites()
        self.w = self.emptyimg.get_width() * 10
        self.selecteditem = 0
        self.initItems()
        self.font = pygame.font.SysFont("Helvetica", 14)
        self.inventoryOpen = False
        self.initInventoryWindow()

    def loop(self):
        self.checkMouseWheel()
        self.checkKeys()
        self.showTools()
        self.showInventory()

    def checkKeys(self):
        for event in self.core.events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    self.plantSelected()
                if event.key == pygame.K_ESCAPE:
                    for tile in self.core.scene.tilemanager.tiles:
                        tile.selected = False
                if event.key == pygame.K_TAB:
                    self.inventoryOpen = not self.inventoryOpen

    def checkMouseWheel(self):
        for event in self.core.events:
            if event.type == pygame.MOUSEWHEEL:
                if event.y < 0:
                    self.selecteditem += 1
                    if self.selecteditem > 8:
                        self.selecteditem = 0
                else:
                    self.selecteditem -= 1
                    if self.selecteditem < 0:
                        self.selecteditem = 8

    def showTools(self):
        screen = pygame.display.get_surface()
        index = 0
        for x in range(9):
            xpos = (self.emptyimg.get_width() * x) + ((screen.get_width() / 2) - (self.w / 2))
            ypos = screen.get_height() - self.emptyimg.get_height()
            screen.blit(self.emptyimg, (xpos, ypos))
            try:
                screen.blit(self.items[index].image, (xpos + 25, ypos + 20))
            except IndexError:
                pass
            if index == self.selecteditem:
                try:
                    type = self.items[self.selecteditem].text.split()[0].lower()
                    text = self.font.render(self.items[self.selecteditem].text, True, [0, 0, 0])
                    counttext = self.font.render(f"Inventory: {self.core.player.inventory['seeds'][type]}", True, [0, 0, 0])
                    screen.blit(text, (xpos, ypos - 20))
                    screen.blit(counttext, (xpos, ypos - 5))
                except IndexError:
                    pass
                screen.blit(self.border, (xpos, ypos))
            index += 1

    def initSprites(self):
        ss = pygame.image.load("data/assets/ui/base.png")
        self.emptyimg = pygame.transform.scale2x(ss.subsurface((0, 144, 48, 48)))
        self.border = pygame.transform.scale2x(ss.subsurface((48, 384, 48, 48)))

    def initItems(self):
        ss = pygame.image.load("data/assets/objects&items/plants.png")
        factor = 3
        self.items = [
            ToolbarItem("Pumpkin Seeds", pygame.transform.scale_by(ss.subsurface(0, 0, 16, 16), factor)),
            ToolbarItem("Strawberry Seeds", pygame.transform.scale_by(ss.subsurface(0, 16, 16, 16), factor)),
            ToolbarItem("Carrot Seeds", pygame.transform.scale_by(ss.subsurface(0, 32, 16, 16), factor)),
            ToolbarItem("Potato Seeds", pygame.transform.scale_by(ss.subsurface(0, 48, 16, 16), factor)),
            ToolbarItem("Cabbage Seeds", pygame.transform.scale_by(ss.subsurface(0, 64, 16, 16), factor)),
            ToolbarItem("Wheat Seeds", pygame.transform.scale_by(ss.subsurface(0, 80, 16, 16), factor)),
            ToolbarItem("Tomato Seeds", pygame.transform.scale_by(ss.subsurface(0, 96, 16, 16), factor)),
            ToolbarItem("Eggplant Seeds", pygame.transform.scale_by(ss.subsurface(0, 112, 16, 16), factor)),
            ToolbarItem("Onion Seeds", pygame.transform.scale_by(ss.subsurface(0, 128, 16, 16), factor)),
        ]

    def plantSelected(self):
        if self.selecteditem >= len(self.items):
            return
        item = self.items[self.selecteditem]
        type = item.text.split()[0].lower()
        for tile in self.core.scene.tilemanager.tiles:
            if tile.selected and tile.object is None:
                if self.core.player.inventory["seeds"][type] > 0:
                    tile.object = Plant(self.core, tile, type)
                    tile.selected = False
                    self.core.player.inventory["seeds"][type] -= 1

    def initInventoryWindow(self):
        ss = pygame.image.load("data/assets/ui/gui.png")
        self.inventoryWindowParts = []
        self.inventoryWindowParts.append(ss.subsurface((0, 0, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((16, 0, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((32, 0, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((0, 16, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((16, 16, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((32, 16, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((0, 32, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((16, 32, 16, 16)))
        self.inventoryWindowParts.append(ss.subsurface((32, 32, 16, 16)))
        

    def showInventory(self):
        if self.inventoryOpen:
            index = 0
            y = 0
            for part in self.inventoryWindowParts:
                x = part.get_width() * index
                pygame.display.get_surface().blit(part, (x, y))
                index += 1
                if index >= 3:
                    index = 0
                    y += 16

class ToolbarItem:

    def __init__(self, text, image):
        self.text = text
        self.image = image
