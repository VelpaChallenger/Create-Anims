class Frame:
    
    def __init__(self, frame_bytes):
        self.metadata = FrameMetaData(frame_bytes)
        self.tiles = frame_bytes[6:] #The tiles that give shape to the frame.

class FrameMetaData: #To make it clear that it's not the frame itself.

    def __init__(self, frame_bytes):
        self.x_length = frame_bytes[0]
        self.y_length = frame_bytes[1]
        self.x_offset = frame_bytes[2]
        self.chr_bank = frame_bytes[3]
        self.y_offset = (frame_bytes[4] & 0xF) * (-1 if (frame_bytes[4] & 0x10) else 1) #I don't usually use ternary in Python but here it is pretty convenient.
        self.special_palette_id = 0 #Unused, but we may give it an use later on.

class Anim: #Similar structure to TileUtils. You have the main class, which then uses data from other classes to do its stuff.

    def __init__(self, createanims):
        self.createanims = createanims

    def refresh(self):
        initial_y = 20
        frame = self.createanims.characters[self.createanims.current_character].frames[self.createanims.current_frame]
        cell_id = 0 #Let's call it this way, probably the most accurate. tile_id could be confused with the tile_id stored in the cell, frame_tile_id would be another candidate to refer to the tile_id stored in the frame, but mixing frame and tile can be a bit confusing as with row and tile in the same name (I did it for TileUtils).
        for row in range(frame.metadata.y_length):
            initial_x = 50
            initial_y += 16
            for col in range(frame.metadata.x_length):
                tile_id = frame.tiles[cell_id]
                if tile_id != 0xFF: #So 0x7F is still a valid tile. So, we need to do it before & 0x7F.
                    tile_image = self.createanims.tiles_images[tile_id & 0x7F] #Let's move it here to have cleaner checks. #We only care about bits 0-6. Actually I think I was going to run a script to fix that for all frames. But meanwhile we can do this. The idea is to remove the and #$7F in the code, I think it's still there for now.
                    self.createanims.anim_canvas.create_image(initial_x, initial_y, anchor="nw", image=tile_image.final_img)
                initial_x += 16
                cell_id += 1