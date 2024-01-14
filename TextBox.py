import pygame

LETTER_MAPPING = {
    pygame.K_a: 'A',
    pygame.K_b: 'B',
    pygame.K_c: 'C',
    pygame.K_d: 'D',
    pygame.K_e: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'H',
    pygame.K_i: 'I',
    pygame.K_j: 'J',
    pygame.K_k: 'K',
    pygame.K_l: 'L',
    pygame.K_m: 'M',
    pygame.K_n: 'O',
    pygame.K_p: 'P',
    pygame.K_q: 'Q',
    pygame.K_r: 'Q',
    pygame.K_s: 'S',
    pygame.K_t: 'T',
    pygame.K_u: 'U',
    pygame.K_v: 'V',
    pygame.K_w: 'W',
    pygame.K_x: 'X',
    pygame.K_y: 'Y',
    pygame.K_z: 'Z',
}

SYMBOL_MAPPING = {
    pygame.K_1: '!',
    pygame.K_2: '@',
    pygame.K_3: '#',
    pygame.K_4: '$',
    pygame.K_5: '%',
    pygame.K_6: '^',
    pygame.K_7: '&',
    pygame.K_8: '*',
    pygame.K_9: '(',
    pygame.K_0: ')',
    # Add more key mappings for symbols
}


class TextBox:
    def __init__(self, screen, rect):
        self.screen = screen
        self.rect = pygame.Rect(rect)
        self.font = pygame.font.Font("Relington.ttf", 40)
        self.text_color = (0, 0, 0)
        self.border_color = (0, 0, 0)
        self.max_length = 200
        self.text = ""
        self.actual_text = ""
        self.is_active = False

    def handle_event(self, event, secret):
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(pygame.mouse.get_pos()):
            self.is_active = True
            return 1
        elif event.type == pygame.KEYDOWN and self.is_active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.actual_text = self.actual_text[:-1]
            else:
                # Check for Shift key state
                shift_pressed = event.mod & pygame.KMOD_SHIFT

                # Handle uppercase letters and symbols
                if event.key in SYMBOL_MAPPING and shift_pressed:
                    char = SYMBOL_MAPPING[event.key]
                elif event.key in LETTER_MAPPING and shift_pressed:
                    char = LETTER_MAPPING[event.key]
                else:
                    char = event.unicode

                # Limit the length of the entered text
                if len(self.text) < self.max_length and char != "":
                    self.actual_text += char
                    if not secret:
                        self.text += char
                    else:
                        self.text += "*"
            return 0

    def draw(self):
        pygame.draw.rect(self.screen, self.border_color, self.rect, 2)
        text_surface = self.font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect()
        text_rect.center = self.rect.center
        self.screen.blit(text_surface, text_rect)

    def return_actual_text(self):
        return self.actual_text

    def clean(self):
        self.actual_text = ""
        self.text = ""
