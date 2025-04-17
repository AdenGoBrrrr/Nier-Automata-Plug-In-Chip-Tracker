class PlugInChip:
    def __init__(self, name, chip_level):
        self.name = name
        self.level = chip_level

class PlugInChipNeeded(PlugInChip):
    def __init__(self, name, chip_level):
        super().__init__(name, chip_level)
        self.chips_gotten = {
            "0": 0,
            "1": 0,
            "2": 0,
            "3": 0,
            "4": 0,
            "5": 0,
            "6": 0,
            "7": 0,
            "8": 0
        }

    def add_chips(self, chip):
        if not isinstance(chip, PlugInChip):
            raise TypeError("chip must be an instance of PlugInChip")
        if chip.name != self.name:
            raise ValueError("chip name does not match the required chip name")
        
        self.chips_gotten[str(chip.level)] += 1
        print(f"Added {chip.name} to chips gotten. Current count of level"
              + f": {self.chips_gotten[str(chip.level)]}")

    def __str__(self):
        output = f"Plug-In Chip Needed: {self.name} (Level {self.level})\n"

        output += "Total chips needed in level 0s:\n"
        total_level_0s = 0
        
        for level, count in self.chips_gotten.items():
            
                total_level_0s += count * (2 ** int(level))

        output += f"{256 - total_level_0s} chips\n"

        return output
    
