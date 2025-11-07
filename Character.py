from Anim import *

class Character:

    def __init__(self, createanims, character_name):
        self.name = character_name #Not sure if we'll need it but... maybe for display purposes? We could add a dictionary or something... anyways, don't want to include too much in this final commit before going back to main.
        self.createanims = createanims
        self.palette = self.get_palette(character_name)
        self.anims = self.get_anims(character_name, [0x00])
        self.frames = self.get_frames(character_name, [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07])
        chr_ids = [self.frames[1].metadata.chr_bank, 0x9E] #When I add more characters, there'll be more and they'll be obtained after we parse the anim file.
        self.chr_palettes, self.chrs = self.get_chrs_and_palettes(character_name, chr_ids) #Whatever, the and makes it clear. Any other name to include both just doesn't make it clear.

    def get_chrs_and_palettes(self, name, chr_ids): #Yeah, after all we're kinda going to do the loop thing now, though not entirely but leaving the bases.
        chr_palettes = {}
        chrs = {}
        for chr_id in chr_ids:
            chr_palette = self.get_chr_palette(name, chr_id)
            chr_palettes[chr_id] = chr_palette
            character_chr = self.get_chr(name, chr_id)
            chrs[chr_id] = character_chr
        return chr_palettes, chrs

    def get_palette(self, name):
        with open(f"{self.createanims.root_dir}/{name}/pal/{name}_usual.pal", "rb") as character_pal:
            palette = list(character_pal.read())
        return palette

    def get_chr_palette(self, name, chr_id): #When we include absolutely every CHR_PALETTE with its corresponding CHR (I used uppercase cause I wanted to), we can iterate over a loop and then append to a chr_palettes and character_chrs. Awesome.
        with open(f"{self.createanims.root_dir}/{name}/chr/{name}_chr_pal_{chr_id:03d}.chr.pal", "rb") as character_chr_pal:
            chr_palette = list(character_chr_pal.read())
        return chr_palette

    def get_chr(self, name, chr_id):
        with open(f"{self.createanims.root_dir}/{name}/chr/{name}_chr_{chr_id:03d}.chr", "rb") as character_chr:
            character_chr = list(character_chr.read())
        return character_chr #Added character cause otherwise chr, you know, reserved keyword.

    def get_frames(self, name, frame_ids):
        frames = [] #This one will be 0-indexed. Frame 00, frame 01 etc.
        for frame_id in frame_ids: #Potentially range(frame_ids) or something of the sort.
            frame = self.get_frame(name, frame_id)
            frames.append(frame)
        return frames

    def get_frame(self, name, frame_id):
        with open(f"{self.createanims.root_dir}/{name}/frames/{name}_frame_{frame_id:02d}.frame", "rb") as character_frame:
            frame = Frame(list(character_frame.read()))
        return frame

    def get_anims(self, name, anim_ids):
        anims = [] #This one will be 0-indexed too. Anim 00, Anim 01 etc. #Might change this soon enough because some anims don't have files, like I removed them, like anim 0xF I believe. Yeah just checked.
        for anim_id in anim_ids: #Potentially range(frame_ids) or something of the sort.
            anim = self.get_anim(name, anim_id)
            anims.append(anim)
        return anims

    def get_anim(self, name, anim_id):
        with open(f"{self.createanims.root_dir}/{name}/anims/{name}_anim_{anim_id:02d}.anim", "rb") as character_anim:
            anim = CharacterAnim(list(character_anim.read()))
        return anim