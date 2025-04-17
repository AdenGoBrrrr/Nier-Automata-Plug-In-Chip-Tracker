from Backend import PlugInChipNeeded, PlugInChip

def main():
    chip_needed = PlugInChipNeeded("Drop-Rate Up", 8)
    level_0 = PlugInChip("Drop-Rate Up", 0)
    level_1 = PlugInChip("Drop-Rate Up", 1)
    level_2 = PlugInChip("Drop-Rate Up", 2)
    level_3 = PlugInChip("Drop-Rate Up", 3)
    level_4 = PlugInChip("Drop-Rate Up", 4)
    level_5 = PlugInChip("Drop-Rate Up", 5)
    level_6 = PlugInChip("Drop-Rate Up", 6)
    level_7 = PlugInChip("Drop-Rate Up", 7)
    level_8 = PlugInChip("Drop-Rate Up", 8)

    for _ in range (3):
        chip_needed.add_chips(level_0)
    chip_needed.add_chips(level_1)
    
    print(chip_needed)

main()
