from labyrinth import Labyrinth
import pygame
import constantes


class Main:

    def init_pygame(self):
        pygame.init()
        pygame.time.Clock().tick(30)
        # Opening the Pygame window (square: width = height)
        window = pygame.display.set_mode((constantes.WINDOW_SIZE, constantes.WINDOW_SIZE))

        icon = pygame.image.load(constantes.ICON_PATH)
        pygame.display.set_icon(icon)

        pygame.display.set_caption(constantes.WINDOW_TITLE)
        self.pygame_images["wall"] = pygame.image.load(constantes.WALL_PICTURE).convert()
        self.pygame_images["start"] = pygame.image.load(constantes.PATH_PICTURE).convert()
        self.pygame_images["hero"] = pygame.image.load(constantes.HERO_PICTURE).convert()
        self.pygame_images["boss"] = pygame.image.load(constantes.GUARDIAN_PICTURE).convert()
        self.pygame_images["arm"] = pygame.image.load(constantes.WEAPONS_PICTURE).convert_alpha()
        self.pygame_images["ether"] = pygame.image.load(constantes.ETHER_PICTURE).convert_alpha()
        self.pygame_images["tube"] = pygame.image.load(constantes.TUBE_PICTURE).convert_alpha()
        self.pygame_images["seringue"] = pygame.image.load(constantes.SYRINGE_PICTURE).convert_alpha()

        self.times_newarial = pygame.font.Font("timesnewarial.ttf", 25)

        return window

    def display(self, lab, counter_items):
        for y, line in enumerate(lab.structure):
            for x, case in enumerate(line):
                if case == "#":
                    self.window.blit(self.pygame_images["wall"], (x * 30, y * 30))
                elif case == 'G':
                    self.window.blit(self.pygame_images["boss"], (x * 30, y * 30))
                elif case == 'A':
                    self.window.blit(self.pygame_images["ether"], (x * 30, y * 30))
                elif case == 'B':
                    self.window.blit(self.pygame_images["tube"], (x * 30, y * 30))
                elif case == 'C':
                    self.window.blit(self.pygame_images["seringue"], (x * 30, y * 30))
                elif case == " ":
                    self.window.blit(self.pygame_images["start"], (x * 30, y * 30))
                elif case == "M":
                    self.window.blit(self.pygame_images["hero"], (x * 30, y * 30))

        self.window.blit(self.pygame_images["arm"], [0, 420])

        text_counter = self.times_newarial.render("Armes:{}".format(counter_items), True, (255, 255, 0))
        self.window.blit(text_counter, (30, 425))

        pygame.display.flip()

    def __init__(self):
        self.pygame_images = dict()
        self.window = self.init_pygame()

        lab = Labyrinth()
        y, x = lab.find_macgyver()
        counter_items = 0

        self.display(lab, counter_items)

        while True:

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        if lab.check_move(y - 1, x):
                            if lab.is_item(y - 1, x):
                                counter_items += 1
                            if lab.is_guardian(y - 1, x):
                                self.end_game(counter_items)
                            lab.structure[y - 1][x] = "M"
                            lab.structure[y][x] = " "
                            y = y - 1

                    elif event.key == pygame.K_DOWN:
                        if lab.check_move(y + 1, x):
                            if lab.is_item(y + 1, x):
                                counter_items += 1
                            if lab.is_guardian(y + 1, x):
                                self.end_game(counter_items)
                            lab.structure[y + 1][x] = "M"
                            lab.structure[y][x] = " "
                            y = y + 1

                    elif event.key == pygame.K_LEFT:
                        if lab.check_move(y, x - 1):
                            if lab.is_item(y, x - 1):
                                counter_items += 1
                            if lab.is_guardian(y, x - 1):
                                self.end_game(counter_items)
                            lab.structure[y][x - 1] = "M"
                            lab.structure[y][x] = " "
                            x = x - 1

                    elif event.key == pygame.K_RIGHT:
                        if lab.check_move(y, x + 1):
                            if lab.is_item(y, x + 1):
                                counter_items += 1
                            if lab.is_guardian(y, x + 1):
                                self.end_game(counter_items)
                            lab.structure[y][x + 1] = "M"
                            lab.structure[y][x] = " "
                            x = x + 1

                    self.display(lab, counter_items)

                elif event.type == pygame.QUIT:
                    exit()

    def end_game(self, counter_items):
        you_win = self.times_newarial.render("Vous avez gagné!", True, (52, 200, 35))
        you_lose = self.times_newarial.render("Vous avez perdu!", True, (255, 0, 0))

        if counter_items == 3:
            self.window.blit(you_win, [150, 150])
        else:
            self.window.blit(you_lose, [150, 150])

        pygame.display.flip()

        exit()


if __name__ == '__main__':
    Main()