import pygame
import sys


class WelcomeScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)

        self.font = pygame.font.Font("Relington.ttf", 90)
        self.font2 = pygame.font.Font("font.ttf", 20)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Welcome to", True, self.text_color)
        self.text2_image = self.font.render("NimbusNav", True, self.text_color)
        self.text3_image = self.font2.render("Click anywhere to continue", True, self.text_color)
        self.text4_image = self.font2.render("Or click here to login as admin", True, self.text_color)
        self.background = pygame.Rect(0, 0, 300, 175)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()

        self.border_rect = pygame.Rect(165, 575, 500, 50)

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.background.center = self.screen_rect.center

        self.text1_rect.centery -= 150
        self.text2_rect.centery -= 50
        self.text3_rect.centery += 50
        self.text4_rect.centery += 150
        self.background.centery += 50

    def handle_events(self, current_screen, previous_screen, selection_screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if self.border_rect.collidepoint(mouse_pos):
                    return "admin", previous_screen, selection_screen
                else:
                    previous_screen[0] = "user"
                    previous_screen[1] = "check"
                    selection_screen.change_text(previous_screen[1])
                    return "selection", previous_screen, selection_screen
        return current_screen, previous_screen, selection_screen

    def draw_start(self):
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 3)
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        self.screen.blit(self.text4_image, self.text4_rect)
