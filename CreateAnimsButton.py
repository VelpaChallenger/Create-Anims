class CreateAnimsButton:

    def __init__(self, createanims):
        self.createanims = createanims

    def chr_left_arrow_button(self, event=None):
        new_chr_bank = self.createanims.current_chr_bank - 2
        self.createanims.tile_utils.load_new_chr_bank(new_chr_bank)

    def chr_right_arrow_button(self, event=None):
        new_chr_bank = self.createanims.current_chr_bank + 2
        self.createanims.tile_utils.load_new_chr_bank(new_chr_bank)