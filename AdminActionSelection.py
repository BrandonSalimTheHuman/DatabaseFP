import pygame
import sys


class AdminActionSelection:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)

        self.font = pygame.font.Font("Relington.ttf", 90)
        self.font2 = pygame.font.Font("Relington.ttf", 70)
        self.font3 = pygame.font.Font("Relington.ttf", 30)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Check location status", True, self.text_color)
        self.text2_image = self.font.render("Add data reading", True, self.text_color)
        self.text3_image = self.font.render("to location", True, self.text_color)
        self.text4_image = self.font.render("Edit event in location", True, self.text_color)
        self.text5_image = self.font2.render("Choose an action:", True, self.text_color)
        self.text6_image = self.font3.render("Back", True, self.text_color)
        self.background = pygame.Rect(0, 0, 300, 175)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.text5_rect = self.text5_image.get_rect()
        self.text6_rect = self.text6_image.get_rect()

        self.border_rect = pygame.Rect(40, 140, 750, 200)
        self.border2_rect = pygame.Rect(40, 390, 750, 200)
        self.border3_rect = pygame.Rect(40, 640, 750, 200)
        self.back_rect = pygame.Rect(self.text6_rect.left + 27, self.text6_rect.top + 25, self.text6_rect.width + 20,
                                     self.text6_rect.height + 20)

        self.combined_height = self.text2_image.get_height() + self.text3_image.get_height()
        self.combined_surface = pygame.Surface((self.text2_image.get_width(), self.combined_height))
        self.combined_surface.fill((204, 204, 255))
        self.combined_surface.blit(self.text2_image, (0, 0))
        self.combined_surface.blit(self.text3_image, (125, self.text2_image.get_height()))
        self.combined_rect = self.combined_surface.get_rect()

        self.text1_rect.center = self.combined_rect.center = self.text4_rect.center = self.text5_rect.center = \
            self.text6_rect.center = self.background.center = self.screen_rect.center

        self.text1_rect.centery -= 210
        self.combined_rect.centery += 40
        self.text4_rect.centery += 290
        self.text5_rect.centery -= 380
        self.text6_rect.centerx -= 350
        self.text6_rect.centery -= 400
        self.background.centery += 50

    def handle_events(self, current_screen, previous_screen, selection_screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.back_rect.collidepoint(mouse_pos):
                    return "admin", previous_screen, selection_screen
                elif self.border_rect.collidepoint(mouse_pos):
                    previous_screen[1] = "check"
                    selection_screen.change_text(previous_screen[1])
                elif self.border2_rect.collidepoint(mouse_pos):
                    previous_screen[1] = "add_reading"
                    selection_screen.change_text(previous_screen[1])
                elif self.border3_rect.collidepoint(mouse_pos):
                    previous_screen[1] = "add_event"
                    selection_screen.change_text(previous_screen[1])
                return "selection", previous_screen, selection_screen

        return current_screen, previous_screen, selection_screen

    def draw_start(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border2_rect, 3)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border3_rect, 3)
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.combined_surface, self.combined_rect)
        self.screen.blit(self.text4_image, self.text4_rect)
        self.screen.blit(self.text5_image, self.text5_rect)
        self.screen.blit(self.text6_image, self.text6_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.back_rect, 2)
