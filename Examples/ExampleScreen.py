from PyUI.Screen import Screen
from PyUI.PageElements import *

class BounceScreen(Screen):
    def __init__(self, window):
        super().__init__(window, (0,0,0))
        self.state = {
            "screen" : ""
        }

    def elementsToDisplay(self):
        self.elements = [

        ]
