import random

ITEMS = ["A", "B", "C"]


class Labyrinth:

    def __init__(self):
        self.structure = self.load("map.txt")
        self.add_items()

    def load(self, file):
        # We open the file
        with open(file, "r") as file:
            level_structure = []
            # We browse the lines of the file
            for line in file:
                level_line = []
                # We browse the sprites (letters) contained in the file
                for char in line:
                    # We ignore the "\ n" at the end of the line
                    if char != '\n':
                        # We add the sprite to the line list
                        level_line.append(char)
                # We add the line to the level list
                level_structure.append(level_line)
            # We save this structure
            return level_structure

    def find_macgyver(self):
        """
        Find MacGyver position in labyrinth.

        :return: MacGyver position
        """

        for y, line in enumerate(self.structure):
            for x, column in enumerate(line):
                if column == "M":
                    return y, x
        return 1, 1

    def check_move(self, new_y, new_x):
        if 0 <= new_y < len(self.structure) \
                and 0 <= new_x < len(self.structure[new_y]) \
                and self.structure[new_y][new_x] != "#":
            return True
        else:
            return False

    def add_items(self):
        for item in ITEMS:
            y = random.randint(0, len(self.structure) - 1)
            x = random.randint(0, len(self.structure[y]) - 1)
            while self.structure[y][x] != " ":
                y = random.randint(0, len(self.structure) - 1)
                x = random.randint(0, len(self.structure[y]) - 1)

            self.structure[y][x] = item

    def is_item(self, y, x):
        if self.structure[y][x] in ITEMS:
            return True
        else:
            return False

    def is_guardian(self, y, x):
        if self.structure[y][x] == "G":
            return True
        else:
            return False
