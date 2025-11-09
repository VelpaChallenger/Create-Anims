class CreateAnimsButton:

    def __init__(self, createanims):
        self.createanims = createanims

    def chr_left_arrow_button(self, event=None):
        new_chr_bank = self.createanims.current_chr_bank - 2
        self.createanims.tile_utils.load_new_chr_bank(new_chr_bank)

    def chr_right_arrow_button(self, event=None):
        new_chr_bank = self.createanims.current_chr_bank + 2
        self.createanims.tile_utils.load_new_chr_bank(new_chr_bank)

    def frame_id_left_arrow_button(self, event=None):
        new_frame_id = self.createanims.current_frame_id - 1
        self.createanims.anim.load_new_frame_id(new_frame_id)

    def frame_id_right_arrow_button(self, event=None):
        new_frame_id = self.createanims.current_frame_id + 1
        self.createanims.anim.load_new_frame_id(new_frame_id)

    def frame_left_arrow_button(self, event=None):
        new_frame = self.createanims.current_frame - 1
        self.createanims.anim.load_new_frame(new_frame)

    def frame_right_arrow_button(self, event=None):
        new_frame = self.createanims.current_frame + 1
        self.createanims.anim.load_new_frame(new_frame)