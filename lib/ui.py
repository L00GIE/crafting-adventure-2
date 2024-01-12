from lib.toolbar import Toolbar
import pygame

class UI:

    def __init__(self, core):
        self.core = core
        self.toolbar = Toolbar(self.core)

    def loop(self):
        self.toolbar.loop()