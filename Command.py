from tkinter import filedialog
import os

class Command:

    def __init__(self, createanims):
        self.createanims = createanims

    def save_palette(self):
        initial_directory = self.createanims.palette_directory
        if self.createanims.palette_directory is None:
            initial_directory = os.getcwd()
        pal_filename = filedialog.asksaveasfilename(
            defaultextension=".pal",
            filetypes=[("Palette files", ".pal"), ("All files", "*.*")],
            initialdir=initial_directory,
            title="Save palette",
            parent=self.createanims.root
        )
        if not pal_filename: #Then save was aborted.
            return
        self.createanims.palette_directory = os.path.dirname(pal_filename) #Directory where the file selected is.
        with open(pal_filename, "wb") as pal_file:
            pal_file.write(bytearray(self.createanims.characters[self.createanims.current_character].palette))

    def save_chr_palette(self):
        initial_directory = self.createanims.chr_palette_directory
        if initial_directory is None:
            initial_directory = os.getcwd()
        chr_pal_filename = filedialog.asksaveasfilename(
            defaultextension=".pal",
            filetypes=[("CHR Palette files", ".chr.pal"), ("All files", "*.*")],
            initialdir=initial_directory,
            title="Save CHR palette",
            parent=self.createanims.root
        )
        if not chr_pal_filename: #Then save was aborted.
            return
        self.createanims.chr_palette_directory = os.path.dirname(chr_pal_filename) #Directory where the file selected is.
        with open(chr_pal_filename, "wb") as chr_pal_file:
            chr_pal_file.write(bytearray(self.createanims.characters[self.createanims.current_character].chr_palettes[self.createanims.current_chr_bank]))

    def toggle_anim_transparency(self, event=None): #When it's called from keyboard shortcut, event is sent. So we need event=None, we won't use it anyways.
        self.createanims.anim.transparency ^= 1 #Let's make it a literal toggle.
        self.createanims.anim.refresh() #But, as usual, a refresh also.

    def toggle_draw_frame_rectangle(self, event=None): #When it's called from keyboard shortcut, event is sent. So we need event=None, we won't use it anyways.
        self.createanims.anim.draw_frame_rectangle ^= 1 #Let's make it a literal toggle.
        self.createanims.anim.refresh() #But, as usual, a refresh also.

    def toggle_draw_empty_cells(self, event=None):
        self.createanims.anim.draw_empty_cells ^= 1
        self.createanims.anim.refresh()