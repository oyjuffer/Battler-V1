### MAIN GAME FILE ###

# IMPORT LIBRARIES
import pygame
import sys
from time import sleep

# IMPORT GAME FILES
from abilities import *
from characters import *
from items import *
from settings import *

# INITIALIZATION
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BATTLER V1")
clock = pygame.time.Clock()

font_name = pygame.font.match_font("arial")
all_sprites = pygame.sprite.Group()


# CLASS LIST
class User:
    def __init__(self):
        self.menu_location = [1, 1]
user = User()

class Button():
    def __init__(self, surface, text, colour, size, x, y, button_location):
        self.surface = surface
        self.text = text
        self.colour = colour
        self.size = size
        self.x = x
        self.y = y
        self.button_location = button_location

        self.button_actived = False

        # DRAW DATA
        self.font = pygame.font.Font(font_name, self.size)
        self.text_surface = self.font.render(self.text, True, self.colour)
        self.text_rect = self.text_surface.get_rect()
        self.text_rect.center = (self.x, self.y)

    def draw(self):
        self.surface.blit(self.text_surface, self.text_rect)

    def draw_left(self):
        self.text_rect.midleft = (self.x, self.y)
        self.surface.blit(self.text_surface, self.text_rect)

    def draw_image(self):
        pass

    def actived(self):
        pygame.draw.polygon(screen, BLACK, [[self.text_rect[0] - 15, self.text_rect.center[1] + 10],
                                            [self.text_rect[0] - 5, self.text_rect.center[1]],
                                            [self.text_rect[0] - 15, self.text_rect.center[1] - 10]])

    def function(self):
        pass

class Submenu():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        user.menu_location = [1, 1]

    def running(self):
        running = True
        while running:
            edge = pygame.Surface((480, 130))
            edge.fill(WHITE)
            screen.blit(edge, (10, 360))
            draw_text(self.title, 24, BLACK, screen, WIDTH * 0.50, HEIGHT * 0.75)

            self.inventory_display_location = [0.06, 0.79]
            self.inventory_button_location = [1, 1]
            self.menu_list = []
            self.menu_value_list = []

            for i in range(len(self.content)):

                self.item_infomation = str(self.content[i].name) + " " + str(
                    self.content[i].physical_damage_note[0]) + "-" + str(
                    self.content[i].physical_damage_note[1]) + "/" + str(
                    self.content[i].magic_damage_note[0]) + "-" + str(
                    self.content[i].magic_damage_note[1]) + " (" + str(self.content[i].strength) + "/" + str(
                    self.content[i].intelligence) + "/" + str(self.content[i].constitution) + ")"
                slot = Button(screen, self.item_infomation, BLACK, 18, WIDTH * self.inventory_display_location[0],
                              HEIGHT * self.inventory_display_location[1], self.inventory_button_location)
                slot.draw_left()

                if slot.button_location == user.menu_location:
                    slot.actived()
                    self.item_selected = self.content[i]

                self.menu_value_list.append(list(self.inventory_button_location))
                self.menu_list.append(slot)

                self.inventory_display_location[1] += 0.04
                self.inventory_button_location[1] += 1

                if self.inventory_button_location[1] >= 6:
                    self.inventory_display_location[0] += 0.50
                    self.inventory_display_location[1] = 0.79
                    self.inventory_button_location[0] += 1
                    self.inventory_button_location[1] = 1

            self.minmax_data = menu_control_minmax(self.menu_value_list)

            # EVENTS
            menu_control(self.minmax_data)
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if self.content == player.inventory_weapon:
                            player.equipped_weapon = self.item_selected
                            user.menu_location = [1, 3]
                            running = False
                        if self.content == player.inventory_armour:
                            player.equipped_armour = self.item_selected
                            user.menu_location = [2, 3]
                            running = False
                        if self.content == player.inventory_token:
                            player.equipped_token = self.item_selected
                            user.menu_location = [3, 3]
                            running = False
                        sleep(0.1)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            #pygame.display.flip()
            clock.tick(FPS)

class Submenu_new():
    def __init__(self, title, content):
        self.title = title
        self.content = content
        user.menu_location = [1, 1]

    def running(self):
        running = True
        while running: 
            edge = pygame.Surface((480, 130))
            edge.fill(WHITE)
            screen.blit(edge, (10, 360))
            draw_text(self.title, 24, BLACK, screen, WIDTH * 0.50, HEIGHT * 0.75)




class Nameplate():
    def __init__(self, x, y, nameplate):
        self.x = x
        self.y = y
        self.nameplate = nameplate

    def draw(self):
        pygame.draw.rect(screen, BLACK, [self.x, self.y, 250, 80], 4)
        draw_text_left(str(self.nameplate.name), 22, BLACK, screen, self.x + 7, self.y + 15)
        draw_text_left("Lv " + str(self.nameplate.level), 22, BLACK, screen, self.x + 200, self.y + 15)
        draw_text_left("HP", 22, BLACK, screen, self.x + 7, self.y + 65)

        if round(self.nameplate.health / self.nameplate.max_health * 100) >= 33:
            pygame.draw.rect(screen, GREEN,
                             [self.x + 35, self.y + 55, round(self.nameplate.health / self.nameplate.max_health * 207),
                              18])
        elif round(self.nameplate.health / self.nameplate.max_health * 100) >= 11:
            pygame.draw.rect(screen, YELLOW,
                             [self.x + 35, self.y + 55, round(self.nameplate.health / self.nameplate.max_health * 207),
                              18])
        elif round(self.nameplate.health / self.nameplate.max_health * 100) > 0:
            pygame.draw.rect(screen, RED,
                             [self.x + 35, self.y + 55, round(self.nameplate.health / self.nameplate.max_health * 207),
                              18])
        else:
            pass

        pygame.draw.rect(screen, BLACK, [self.x + 35, self.y + 55, 210, 20], 5)

    def update(self):
        self.nameplate.health -= 1

class Battletext():
    def __init__(self):
        self.text            = ""

    def plain(self, text): 
        self.text = text
        return self.text

    def physical_damage(self, name, damage_done):
        self.text = str(name) + " attacks for " + str(damage_done) + " physical damage!"
        return self.text

    def magical_damage(self):
        pass


# FUNCTION LIST
def draw_text(text, size, colour, surface, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    surface.blit(text_surface, text_rect)

def draw_text_left(text, size, colour, surface, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.midleft = (x, y)
    surface.blit(text_surface, text_rect)

def draw_edge(colour):
    screen.fill(colour)
    edge = pygame.Surface((480, 480))
    edge.fill(WHITE)
    screen.blit(edge, (10, 10))

def wait_for_key():
    waiting = True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False
                running = False
            if event.type == pygame.KEYDOWN:
                waiting = False

def menu_control(menu_values):
    minmax_data = menu_values
    keystate = pygame.key.get_pressed()
    if keystate[pygame.K_UP]:
        print("KEYSTATE: UP")
        if user.menu_location[1] <= minmax_data[1]:
            print("PASSED")
            pass
        else:
            print("UPDATED")
            print("MATRIX: " + str(user.menu_location))
            user.menu_location[1] -= 1
            sleep(0.1)
            print("MATRIX: " + str(user.menu_location))

    if keystate[pygame.K_DOWN]:
        print("KEYSTATE: DOWN")
        if user.menu_location[1] >= minmax_data[3]:
            print("PASSED")
            pass
        else:
            print("UPDATED")
            print("MATRIX: " + str(user.menu_location))
            user.menu_location[1] += 1
            sleep(0.1)
            print("MATRIX: " + str(user.menu_location))

    if keystate[pygame.K_LEFT]:
        print("KEYSTATE: LEFT")
        if user.menu_location[0] <= minmax_data[0]:
            print("PASSED")
            pass
        else:
            print("UPDATED")
            print("MATRIX: " + str(user.menu_location))
            user.menu_location[0] -= 1
            sleep(0.1)
            print("MATRIX: " + str(user.menu_location))

    if keystate[pygame.K_RIGHT]:
        print("KEYSTATE: RIGHT")
        if user.menu_location[0] >= minmax_data[2]:
            print("PASSED")
            pass
        else:
            print("UPDATED")
            print("MATRIX: " + str(user.menu_location))
            user.menu_location[0] += 1
            sleep(0.1)
            print("MATRIX: " + str(user.menu_location))

def draw_rect_center(surface, colour, x, y, sx, sy, edge):
    rect = pygame.Rect(0, 0, sx, sy)
    rect.center = (x, y)
    pygame.draw.rect(surface, colour, rect, edge)

def menu_control_minmax(menu_list):
    max_x = 1
    max_y = 1
    min_x = 1
    min_y = 1
    for i in range(len(menu_list)):
        submenu_list = menu_list[i]

        for i2 in range(len(submenu_list)):
            if min_x > submenu_list[0]:
                min_x = submenu_list[0]
            if min_y > submenu_list[1]:
                min_y = submenu_list[1]
            if max_x < submenu_list[0]:
                max_x = submenu_list[0]
            if max_y < submenu_list[1]:
                max_y = submenu_list[1]
    return min_x, min_y, max_x, max_y

def reduce_health(damage_done, player_nameplate, target_nameplate):
    for i in range(damage_done):
        target_nameplate.update()

        draw_edge(BLACK)
        pygame.draw.rect(screen, BLACK, [0, 350, 500, 10])

        player_nameplate.draw()
        target_nameplate.draw()

        pygame.display.update()
        clock.tick(FPS)

def draw_battle_text(text, player_nameplate, target_nameplate):
    
    display_text_1 = ""
    display_text_2 = ""
    display_text_3 = ""

    for i in text:

        draw_edge(BLACK)
        pygame.draw.rect(screen, BLACK, [0, 350, 500, 10])

        if len(display_text_1) <= 35:
            display_text_1 += i
            draw_text_left(display_text_1, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.77)
        elif len(display_text_2) <= 35:
            display_text_2 += i
            draw_text_left(display_text_1, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.77)
            draw_text_left(display_text_2, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.85)
        elif len(display_text_3) <= 35:
            display_text_3 += i
            draw_text_left(display_text_1, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.77)
            draw_text_left(display_text_2, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.85)
            draw_text_left(display_text_3, 32, BLACK, screen, WIDTH * 0.05, HEIGHT * 0.93)

        player_nameplate.draw()
        target_nameplate.draw()

        pygame.display.update()
        clock.tick(FPS)

        sleep(0.02)

    wait_for_key()


# MENU LIST
def main_menu():
    while True:

        # INITIALIZATION
        start_button = Button(screen, "START GAME", BLACK, 32, WIDTH * 0.5, HEIGHT * 0.40, [1, 1])
        compendium_button = Button(screen, "COMPENDIUM", BLACK, 32, WIDTH * 0.5, HEIGHT * 0.50, [1, 2])
        settings_button = Button(screen, "SETTINGS", BLACK, 32, WIDTH * 0.5, HEIGHT * 0.60, [1, 3])
        exit_button = Button(screen, "EXIT", BLACK, 32, WIDTH * 0.5, HEIGHT * 0.70, [1, 4])

        # EVENTS
        menu_control([1, 1, 1, 4])  # min_x, min_y, max_x, max_y of button locations.
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if start_button.button_location == user.menu_location:
                        user.menu_location = [1, 1]
                        start_game()

                    if compendium_button.button_location == user.menu_location:
                        user.menu_location = [1, 1]
                        compendium()

                    if settings_button.button_location == user.menu_location:
                        print("SETTINGS")

                    if exit_button.button_location == user.menu_location:
                        pygame.quit()
                        sys.exit()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # UPDATE

        # DRAW
        draw_edge(BLACK)
        draw_text("BATTLER V1", 64, BLACK, screen, WIDTH * 0.5, HEIGHT * 0.10)
        start_button.draw()
        compendium_button.draw()
        settings_button.draw()
        exit_button.draw()

        if start_button.button_location == user.menu_location:
            start_button.actived()
        if compendium_button.button_location == user.menu_location:
            compendium_button.actived()
        if settings_button.button_location == user.menu_location:
            settings_button.actived()
        if exit_button.button_location == user.menu_location:
            exit_button.actived()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)

def start_game():
    running = True
    while running:

        # INITIALIZATION
        character_name_button = Button(screen, "Name Here...", BLACK, 32, WIDTH * 0.6, HEIGHT * 0.10, [1, 1])
        character_name_button1 = Button(screen, "Name Here...", BLACK, 32, WIDTH * 0.6, HEIGHT * 0.10, [2, 1])
        character_name_button2 = Button(screen, "Name Here...", BLACK, 32, WIDTH * 0.6, HEIGHT * 0.10, [3, 1])

        strength_button = Button(screen, str(player.strength), BLACK, 30, 200, 140, [1, 2])
        intelligence_button = Button(screen, str(player.intelligence), BLACK, 30, 300, 140, [2, 2])
        constitution_button = Button(screen, str(player.constitution), BLACK, 30, 400, 140, [3, 2])
        player.convert_stats()

        weapon_button = Button(screen, player.equipped_weapon.name, BLACK, 32, WIDTH * 0.20, HEIGHT * 0.52, [1, 3])
        armour_button = Button(screen, player.equipped_armour.name, BLACK, 32, WIDTH * 0.50, HEIGHT * 0.52, [2, 3])
        token_button = Button(screen, player.equipped_token.name, BLACK, 32, WIDTH * 0.80, HEIGHT * 0.52, [3, 3])

        back_button = Button(screen, "BACK", BLACK, 32, WIDTH * 0.13, HEIGHT * 0.95, [1, 4])
        reset_button = Button(screen, "RESET", BLACK, 32, WIDTH * 0.50, HEIGHT * 0.95, [2, 4])
        start_button = Button(screen, "START", BLACK, 32, WIDTH * 0.87, HEIGHT * 0.95, [3, 4])

        # EVENTS
        menu_control([1, 1, 3, 4])  # min_x, min_y, max_x, max_y of button locations.
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if user.menu_location == [1, 1] or user.menu_location == [2, 1] or user.menu_location == [3, 1]:
                        print("NAME CHANGE")

                    if user.menu_location[1] == 2 and player.skill_points > 0:
                        if user.menu_location == [1, 2]:
                            player.strength += 1
                            player.strength_reset -= 1
                        if user.menu_location == [2, 2]:
                            player.intelligence += 1
                            player.intelligence_reset -= 1
                        if user.menu_location == [3, 2]:
                            player.constitution += 1
                            player.constitution_reset -= 1
                        player.skill_points -= 1
                        player.skill_points_reset += 1
                        sleep(0.1)

                    if user.menu_location == [1, 3]:
                        weapon_inventory_submenu = Submenu("Weapons", player.inventory_weapon)
                        weapon_inventory_submenu.running()

                    if user.menu_location == [2, 3]:
                        armour_inventory_submenu = Submenu("Armours", player.inventory_armour)
                        armour_inventory_submenu.running()

                    if user.menu_location == [3, 3]:
                        token_inventory_submenu = Submenu("Tokens", player.inventory_token)
                        token_inventory_submenu.running()

                    if user.menu_location == [1, 4]:
                        user.menu_location = [1, 1]
                        running = False

                    if user.menu_location == [2, 4]:
                        player.strength += player.strength_reset
                        player.intelligence += player.intelligence_reset
                        player.constitution += player.constitution_reset
                        player.skill_points += player.skill_points_reset
                        player.strength_reset = 0
                        player.intelligence_reset = 0
                        player.constitution_reset = 0
                        player.skill_points_reset = 0

                        player.equipped_weapon = none
                        player.equipped_armour = none
                        player.equipped_token = none
                        sleep(0.1)

                    if user.menu_location == [3, 4]:
                        player.health = player.max_health
                        running = False
                        game()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # UPDATE

        # DRAW
        draw_edge(BLACK)

        character_name_button.draw()
        back_button.draw()
        reset_button.draw()
        start_button.draw()

        pygame.draw.rect(screen, BLACK, [0, 175, 500, 10])
        pygame.draw.rect(screen, BLACK, [0, 350, 500, 10])

        ##DRAW 	# Display ITEM SLOTS
        # WEAPON SLOT
        draw_text("Weapon", 26, BLACK, screen, WIDTH * 0.20, HEIGHT * 0.41)
        draw_rect_center(screen, BLACK, WIDTH * 0.20, HEIGHT * 0.52, 75, 75, 5)
        weapon_button.draw()
        if weapon_button.button_location == user.menu_location:
            weapon_button.actived()

        # ARMOUR SLOT
        draw_text("Armour", 26, BLACK, screen, WIDTH * 0.50, HEIGHT * 0.41)
        draw_rect_center(screen, BLACK, WIDTH * 0.50, HEIGHT * 0.52, 75, 75, 5)
        armour_button.draw()
        if armour_button.button_location == user.menu_location:
            armour_button.actived()

        # TOKEN SLOT
        draw_text("Token", 26, BLACK, screen, WIDTH * 0.80, HEIGHT * 0.41)
        draw_rect_center(screen, BLACK, WIDTH * 0.80, HEIGHT * 0.52, 75, 75, 5)
        token_button.draw()
        if token_button.button_location == user.menu_location:
            token_button.actived()

        # DRAW 	# Display LEVEL
        pygame.draw.rect(screen, BLACK, [25, 25, 50, 50])
        draw_text("Lv " + str(player.level), 26, WHITE, screen, 50, 50)

        # DRAW 	#Display SKILL POINTS
        pygame.draw.rect(screen, BLACK, [25, 115, 50, 50])
        draw_text("Sp " + str(player.skill_points), 26, WHITE, screen, 50, 140)
        pygame.draw.rect(screen, BLACK, [90, 127.5, 50, 25])
        pygame.draw.polygon(screen, BLACK, [[140, 115], [160, 140], [140, 160]])

        # DRAW 	# Display Strength
        pygame.draw.rect(screen, BLACK, [175, 115, 50, 50], 5)
        draw_text("STR", 22, BLACK, screen, 200, 100)
        strength_button.draw()
        if strength_button.button_location == user.menu_location:
            strength_button.actived()

        draw_text("P. Damage", 26, BLACK, screen, WIDTH * 0.13, 400)
        draw_text(str(player.min_physical_damage) + "-" + str(player.max_physical_damage) + " + " + str(
            player.physical_damage), 22, BLACK, screen, WIDTH * 0.13, 425)

        # DRAW 	# Display Intelligence
        pygame.draw.rect(screen, BLACK, [275, 115, 50, 50], 5)
        draw_text("INT", 22, BLACK, screen, 300, 100)
        intelligence_button.draw()
        if intelligence_button.button_location == user.menu_location:
            intelligence_button.actived()

        draw_text("M. Damage", 26, BLACK, screen, 250, 400)
        draw_text(str(player.min_magic_damage) + "-" + str(player.max_magic_damage) + " + " + str(player.magic_damage),
                  22, BLACK, screen, 250, 425)

        # DRAW 	# Display Constitution
        pygame.draw.rect(screen, BLACK, [375, 115, 50, 50], 5)
        draw_text("CON", 22, BLACK, screen, 400, 100)
        constitution_button.draw()
        if constitution_button.button_location == user.menu_location:
            constitution_button.actived()

        draw_text("Health", 26, BLACK, screen, WIDTH * 0.87, 400)
        draw_text(str(player.max_health), 22, BLACK, screen, WIDTH * 0.87, 425)

        # DRAW # Draw active button arrows
        if character_name_button.button_location == user.menu_location or character_name_button1.button_location == user.menu_location or character_name_button2.button_location == user.menu_location:
            character_name_button.actived()
        if back_button.button_location == user.menu_location:
            back_button.actived()
        if reset_button.button_location == user.menu_location:
            reset_button.actived()
        if start_button.button_location == user.menu_location:
            start_button.actived()

        pygame.display.update()
        # pygame.display.flip()
        clock.tick(FPS)

def game():
    running = True

    user.menu_location = [1, 1]
    battle_phase = 1
    target = npc_dustin_echos

    target.convert_stats()
    target.health = target.max_health

    # INITIALIZATION
    player_nameplate = Nameplate(237, 267, player)
    target_nameplate = Nameplate(12, 12, target)

    attack_button = Button(screen, "ATTACK", BLACK, 32, WIDTH * 0.07, HEIGHT * 0.77, [1, 1])
    magic_button = Button(screen, "MAGIC", BLACK, 32, WIDTH * 0.07, HEIGHT * 0.85, [1, 2])
    inventory_button = Button(screen, "ITEM", BLACK, 32, WIDTH * 0.07, HEIGHT * 0.93, [1, 3])

    battletext = Battletext()



    while running:

        if battle_phase == 1:
            print("BATTLE PHASE 1")

            # EVENTS
            menu_control([1, 1, 1, 3])  # min_x, min_y, max_x, max_y of button locations.
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        if user.menu_location == [1, 1]:
                            damage_done = player.attack(target)
                            reduce_health(damage_done, player_nameplate, target_nameplate)
                            draw_battle_text(battletext.physical_damage(player.name, damage_done), player_nameplate, target_nameplate)
                            battle_phase = 2

                        if user.menu_location == [1, 2]:
                            print("MAGIC")
                            # magic_abilities = Submenu("Magic", player.magic_abilities)
                            # magic_abilities.running()




                        if user.menu_location == [1, 3]:
                            print("ITEM")

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # UPDATE

            # DRAW
            draw_edge(BLACK)
            pygame.draw.rect(screen, BLACK, [0, 350, 500, 10])

            player_nameplate.draw()
            target_nameplate.draw()

            attack_button.draw_left()
            if attack_button.button_location == user.menu_location:
                attack_button.actived()

            magic_button.draw_left()
            if magic_button.button_location == user.menu_location:
                magic_button.actived()

            inventory_button.draw_left()
            if inventory_button.button_location == user.menu_location:
                inventory_button.actived()

            pygame.display.update()
            clock.tick(FPS)

            if target.health <= 0:
                draw_battle_text(str(target.name) + " has been defeated!", player_nameplate, target_nameplate)
                running = False
                break

        if battle_phase == 2:
            print("BATTLE PHASE: 2")

            # INITIALIZATION

            # EVENTS
            damage_done = target.attack(player)
            reduce_health(damage_done, target_nameplate, player_nameplate)
            draw_battle_text(battletext.physical_damage(target.name, damage_done), player_nameplate, target_nameplate)

            # UPDATE

            # DRAW

            draw_edge(BLACK)
            pygame.draw.rect(screen, BLACK, [0, 350, 500, 10])

            player_nameplate.draw()
            target_nameplate.draw()

            pygame.display.update()
            clock.tick(FPS)

            battle_phase = 1

            if player.health <= 0:
                draw_battle_text(str(player.name) + " has been defeated!", player_nameplate, target_nameplate)
                draw_battle_text("GAME OVER!", player_nameplate, target_nameplate)
                running = False
                break



def compendium():
    running = True
    while running:

        # INITIALIZATION
        back_button = Button(screen, "BACK", BLACK, 32, WIDTH * 0.13, HEIGHT * 0.95, [1, 1])

        # EVENTS
        menu_control([1, 1, 1, 1])  # min_x, min_y, max_x, max_y of button locations.
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:

                    if user.menu_location == [1, 1]:
                        running = False

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # UPDATE
        # DRAW
        draw_edge(BLACK)
        draw_text("COMPENDIUM", 64, BLACK, screen, WIDTH * 0.5, HEIGHT * 0.10)

        back_button.draw()

        if back_button.button_location == user.menu_location:
            back_button.actived()

        pygame.display.update()
        pygame.display.flip()
        clock.tick(FPS)


main_menu()