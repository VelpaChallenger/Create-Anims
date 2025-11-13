import os

from CreateAnims import *
from Character import *

def load_game_anims(createanims): #Another idea was to have a call to this in init_state, which makes sense considering we're initializing values. But then I would sort of have a circular dependency. I would have to put that stuff in yet another file, and I kinda like it here in the main file, so to speak. So that's why I ended up doing this way. It still makes sense: all the data has to go to createanims.
    characters_name_list = os.listdir(createanims.root_dir)
    for character_name in characters_name_list:
        character = Character(createanims.root_dir, character_name)
        createanims.characters.append(character)

def main():
    createanims = CreateAnims()
    createanims.root_dir = "../characters"
    load_game_anims(createanims)
    createanims.current_anim = 0x00
    createanims.current_frame = 0x00
    createanims.current_frame_id = 0x01
    createanims.anim.load_new_character(0)
    createanims.root.mainloop()
main()