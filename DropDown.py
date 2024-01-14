import pygame


class DropDown:
    def __init__(self, main, options, screen_rect):
        self.screen_rect = screen_rect
        self.color_menu = [(200, 90, 255), [230, 120, 255]]
        self.color_option = [(100, 140, 255), [130, 160, 255]]
        self.rect = pygame.Rect(0, 150, 400, 37)
        self.rect.centerx = self.screen_rect.centerx
        self.font = pygame.font.Font("Relington.ttf", 30)
        self.main = self.main_original = main
        self.options = options
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf, shift):
        pygame.draw.rect(surf, self.color_menu[self.menu_active], self.rect, 0)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 1)
        msg = self.font.render(self.main, 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center=self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.options):
                rect = self.rect.copy()
                rect.y += ((i % 19) + 1) * self.rect.height
                if shift:
                    rect.x -= 200
                if i >= 19:
                    rect.x += 400
                pygame.draw.rect(surf, self.color_option[1 if i == self.active_option else 0], rect, 0)
                pygame.draw.rect(surf, (0, 0, 0), rect, 1)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center=rect.center))

    def update(self, event_list, shift):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)

        self.active_option = -1
        for i in range(len(self.options)):
            rect = self.rect.copy()
            rect.y += ((i % 19) + 1) * self.rect.height
            if shift:
                rect.x -= 200
            if i >= 19:
                rect.x += 400
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.draw_menu = False
                    return self.active_option
        return -1

    def move_down(self, distance):
        self.rect.centery += distance

    def result(self):
        return self.main

    def clean(self):
        self.active_option = self.main_original
