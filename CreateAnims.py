#aka Editor as others might know it. But I like CreateAnims.

import tkinter
from tkinter import Tk

from TileUtils import *

FONT = ("TkDefaultFont", 16)

WIDTH = 860
HEIGHT = 600
INITIAL_X = 500
INITIAL_Y = 200

class CreateAnims:

    def __init__(self):
        self.init_state()
        self.init_anim_window()

    def init_state(self):
        self.root = Tk()
        self.tile_utils = TileUtils(self)
        self.characters_palettes = []

    def init_anim_window(self):
        self.root.title("Create Anims") #Sometimes dreams come true! Believe in them!
        self.root.geometry(f"{WIDTH}x{HEIGHT}+{INITIAL_X}+{INITIAL_Y}") #It's how my mind sees things. It's the initial, you might drag the window around and stuff. #Window x/y could be alternative name.

        frame_stage = tkinter.Frame(self.root, border=0) #Scenario also. But I like more stage. It's where the action happens.
        frame_stage.grid(row=0, column=0, sticky="w")
        self.stage_canvas = tkinter.Canvas(frame_stage, width=860, height=256, bg="#E0E0E0")
        self.stage_canvas.grid(row=0, column=0)

        frame_palette = tkinter.Frame(self.root, border=0)
        frame_palette.grid(row=1, column=0, sticky="w")
        self.pal_label = tkinter.Label(frame_palette, text="Palette:", anchor="w", font=FONT)
        self.pal_label.grid(row=0, column=0, sticky="w")
        self.character_palette_canvas = tkinter.Canvas(frame_palette, width=254, height=32, bg="#808080", cursor="hand2", borderwidth=0)
        self.character_palette_canvas.grid(row=1, column=0)

    def refresh_UI(self): #This will be part of CreateAnims. All directly UI-related, idea is that it's here. Maybe not the technical like more specific code per se, but at least the highest layer.
        self.tile_utils.refresh_palette() #Changed my mind, will be part of a refresh/update UI.