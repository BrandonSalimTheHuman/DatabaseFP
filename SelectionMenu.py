import pygame
from DropDown import DropDown
import sys


class SelectionMenu:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)

        self.font = pygame.font.Font("Relington.ttf", 40)
        self.font2 = pygame.font.Font("Relington.ttf", 30)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Choose the location you want to check", True, self.text_color)
        self.text2_image = self.font2.render("Then press enter to confirm", True, self.text_color)
        self.text3_image = self.font2.render("Back", True, self.text_color)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.border_rect = pygame.Rect(self.text3_rect.left + 27, self.text3_rect.top + 25, self.text3_rect.width + 20,
                                       self.text3_rect.height + 20)

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.screen_rect.center
        self.text1_rect.centery -= 400
        self.text2_rect.centery -= 340
        self.text3_rect.centerx -= 350
        self.text3_rect.centery -= 400

        self.dropdown = DropDown("Choose a location", ["Nanggroe Aceh Darussalam", "Sumatera Utara", "Sumatera Selatan",
                                                       "Sumatera Barat", "Bengkulu", "Riau", "Kepulauan Riau", "Jambi",
                                                       "Lampung", "Bangka Belitung", "Kalimantan Barat",
                                                       "Kalimantan Timur", "Kalimantan Selatan", "Kalimantan Tengah",
                                                       "Kalimantan Utara", "Banten", "DKI Jakarta", "Jawa Barat",
                                                       "Jawa Tengah", "Daerah Istimewa Yogyakarta", "Jawa Timur",
                                                       "Bali",
                                                       "Nusa Tenggara Timur", "Nusa Tenggara Barat", "Gorontalo",
                                                       "Sulawesi Barat", "Sulawesi Tengah", "Sulawesi Utara",
                                                       "Sulawesi Tenggara", "Sulawesi Selatan", "Maluku Utara",
                                                       "Maluku", "Papua Barat", "Papua", "Papua Tengah",
                                                       "Papua Pegunungan", "Papua Selatan", "Papua Barat Daya"],
                                 self.screen_rect)

    def draw_start(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 2)
        self.dropdown.draw(self.screen, True)

    def change_text(self, usage):
        if usage == "check":
            self.text1_image = self.font.render("Choose the location you want to check", True, self.text_color)
        elif usage == "add_reading":
            self.text1_image = self.font.render("Choose the location to add the data reading", True, self.text_color)
        elif usage == "add_event":
            self.text1_image = self.font.render("Choose the location to add the event", True, self.text_color)

    def handle_events(self, current_screen, result_screen, previous_screen, add_reading, add_event):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect.collidepoint(pygame.mouse.get_pos()):
                self.dropdown.main = "Choose a location"
                if previous_screen[0] == "admin":
                    return "admin_select", result_screen, previous_screen, add_reading, add_event
                elif previous_screen[0] == "user":
                    return "welcome", result_screen, previous_screen, add_reading, add_event
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                name = self.dropdown.result()
                if name != "Choose a location":
                    if previous_screen[1] == "add_reading":
                        add_reading.update_main(name)
                        return "add_reading", result_screen, previous_screen, add_reading, add_event
                    elif previous_screen[1] == "add_event":
                        add_event.update_main(name)
                        return "add_event", result_screen, previous_screen, add_reading, add_event
                    result_screen.update_main(name)
                    return "result", result_screen, previous_screen, add_reading, add_event

        selected_option = self.dropdown.update(event_list, True)
        if selected_option >= 0:
            self.dropdown.main = self.dropdown.options[selected_option]

        self.dropdown.draw(self.screen, True)

        return current_screen, result_screen, previous_screen, add_reading, add_event
