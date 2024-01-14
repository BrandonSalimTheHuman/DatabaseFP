import pygame


class NumPad:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)
        self.default_color = (200, 90, 255)
        self.hover_color = (255, 150, 150)

        self.switch = False
        self.switch2 = False

        self.font = pygame.font.Font("Relington.ttf", 40)

        self.number_images = []
        self.number_rects = []

        self.switch = False

        button_width = 100  # Adjust the width of each button
        button_height = 100  # Adjust the height of each button

        self.nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, ".", 0, "<-"]
        for i in range(12):
            tmp_text = str(self.nums[i])
            tmp_image = self.font.render(tmp_text, True, self.text_color)
            tmp_rect = tmp_image.get_rect()

            row = i // 3
            col = i % 3
            tmp_rect.topleft = (col * button_width, row * button_height)
            tmp_rect.centerx += 270
            tmp_rect.centery += 450

            button_rect = pygame.Rect(tmp_rect.topleft, (button_width, button_height))

            self.number_images.append(tmp_image)
            self.number_rects.append(button_rect)

    def draw_start(self):
        for i in range(len(self.number_images)):
            rect = self.number_rects[i]
            if rect.collidepoint(pygame.mouse.get_pos()):
                pygame.draw.rect(self.screen, self.hover_color, rect)
            else:
                pygame.draw.rect(self.screen, self.default_color, rect)
            pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

            text_rect = self.number_images[i].get_rect(center=rect.center)
            self.screen.blit(self.number_images[i], text_rect.topleft)

    def reset(self):
        self.switch = False

    def handle_events(self, current_value):
        for i in range(len(self.number_rects)):
            if self.number_rects[i].collidepoint(pygame.mouse.get_pos()):
                if i == 9:
                    if not self.switch:
                        self.switch = True
                        current_value += str(self.nums[i])
                elif i == 11:
                    if current_value != "":
                        if current_value[-1] == ".":
                            self.switch = False
                        current_value = current_value[:-1]
                else:
                    current_value += str(self.nums[i])
                return current_value
        return current_value
