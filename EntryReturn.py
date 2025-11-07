class EntryReturn:

    def __init__(self, createanims):
        self.createanims = createanims

    def chr_entry(self, event=None): #chr is reserved keyword and should not matter in this context but I still feel more comfortable, if not technically then aesthetically when I see chr_entry.
        chr_entry_value = self.createanims.chr_entry.get()
        if not chr_entry_value:
            self.createanims.chr_entry.configure(highlightcolor="red", highlightbackground="red")
            self.createanims.chr_info_text.configure(text="You haven't entered a CHR Bank number yet.", fg="red")
            return False
        if int(chr_entry_value) % 2 == 1: #Validation 4: number must be even. Though for this, it will have to be on enter, there's no other way to know the input is finished.
            self.createanims.chr_entry.configure(highlightcolor="red", highlightbackground="red")
            self.createanims.chr_info_text.configure(text="CHR Bank must be an even number.", fg="red")
            return False
        new_chr_bank = int(chr_entry_value)
        self.createanims.tile_utils.load_new_chr_bank(new_chr_bank) #New because it's not exactly the same thing we do on init. We don't display the text for example. Nor we care if the character has the CHR or not.

    def anim_entry(self, event=None):
        pass

    def frame_entry(self, event=None):
        pass

    def frame_id_entry(self, event=None):
        frame_id_entry_value = self.createanims.frame_id_entry.get()
        if not frame_id_entry_value:
            self.createanims.frame_id_entry.configure(highlightcolor="red", highlightbackground="red")
            return False
        new_frame_id = int(frame_id_entry_value)
        self.createanims.anim.load_new_frame_id(new_frame_id)