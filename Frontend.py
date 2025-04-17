from Backend import PlugInChipNeeded, PlugInChip
from tkinter import (Tk, Label, Button, Frame)

class PlugInChipNeededApp:

    def __init__(self, chip_needed):
        self.root = Tk()
        self.root.title("Nier: Automata Plug-In Chip Needed Calculator")
        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=5, pady=5)
        self.widgets = []
        self.plug_in_chip_needed = chip_needed

    def run(self):
        self.create_widgets()
        self.root.mainloop()
    
    def create_widgets(self):
        self.delete_device_widgets()

        chip_needed_label = Label(
            self.main_frame, 
            text="Plug-In Chip Needed:"
            )
        chip_needed_label.grid(row=0, column=0, padx=5, pady=5)
        self.widgets.append(chip_needed_label)

        chip_name_label = Label(
            self.main_frame, 
            text=(f"{self.plug_in_chip_needed.name} "
                  + f"(Level: {self.plug_in_chip_needed.level})")
            )
        chip_name_label.grid(row=0, column=1, padx=5, pady=5)
        self.widgets.append(chip_name_label)

        chips_gotten_label = Label(
            self.main_frame, 
            text="Chips Gotten:",
            anchor="w"
            )
        chips_gotten_label.grid(row=1, column=0, padx=5, pady=5)
        self.widgets.append(chips_gotten_label)

        for chip_level, count in self.plug_in_chip_needed.chips_gotten.items():
            label = Label(
                self.main_frame, 
                text=f"Level {chip_level}: {count}",
                anchor="w"
                )
            label.grid(row=int(chip_level) + 2, column=0, padx=5, pady=5)
            self.widgets.append(label)

            button = Button(
                self.main_frame, 
                text="Add Chip",
                command=lambda level=chip_level: self.add_chip(level)
                )
            button.grid(row=int(chip_level) + 2, column=1, padx=5, pady=5)
            self.widgets.append(button)

        remaining_chips_label = Label(
            self.main_frame, 
            text=(f"Remaining chips needed: "
                  +f"{self.plug_in_chip_needed.get_remaining_chips_needed()}")
            )
        remaining_chips_label.grid(
            row=11, 
            column=0, 
            padx=5, 
            pady=5, 
            columnspan=2
            )
        self.widgets.append(remaining_chips_label)

    def add_chip(self, level):
        chip = PlugInChip(self.plug_in_chip_needed.name, int(level))
        self.plug_in_chip_needed.add_chips(chip)
        self.create_widgets()
        #try:
        #    chip = PlugInChip(self.plug_in_chip_needed.name, int(level))
        #    self.plug_in_chip_needed.add_chips(chip)
        #    messagebox.showinfo("Success", f"Added {chip.name} (Level {level})")
        #    self.create_widgets()
        #except TypeError as e:
        #    messagebox.showerror("Error", str(e))
        #except ValueError as e:
        #    messagebox.showerror("Error", str(e))

    def delete_device_widgets(self):
         for widget in self.widgets:
              widget.destroy()

def main():
    chip_needed = PlugInChipNeeded("Drop-Rate Up", 8)

    app = PlugInChipNeededApp(chip_needed)
    app.run()

main()
