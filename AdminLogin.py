import pygame
import sys
from TextBox import TextBox
import mysql.connector
import hashlib


def hash_password(password, salt):
    # Combine password and salt, then hash using a secure hashing algorithm (e.g., SHA-256)
    hashed_password = hashlib.sha256(password.encode('utf-8') + salt).hexdigest()
    return hashed_password


class AdminLogin:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)

        self.font = pygame.font.Font("Relington.ttf", 90)
        self.font2 = pygame.font.Font("font.ttf", 20)
        self.font3 = pygame.font.Font("Relington.ttf", 30)
        self.font4 = pygame.font.Font("font.ttf", 30)
        self.font4_color = (255, 0, 0)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Enter username:", True, self.text_color)
        self.text2_image = self.font.render("Enter password:", True, self.text_color)
        self.background = pygame.Rect(0, 0, 300, 175)

        self.textbox1 = TextBox(self.screen, (120, 230, 600, 60))
        self.textbox2 = TextBox(self.screen, (120, 530, 600, 60))

        self.text3_image = self.font2.render("Press enter to confirm", True, self.text_color)
        self.text4_image = self.font3.render("Back", True, self.text_color)
        self.text5 = ""
        self.text5_image = self.font4.render(self.text5, True, self.font4_color)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.text5_rect = self.text5_image.get_rect()
        self.border_rect = pygame.Rect(self.text4_rect.left + 27, self.text4_rect.top + 25, self.text4_rect.width + 20,
                                       self.text4_rect.height + 20)

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.text5_rect.center = self.background.center = self.screen_rect.center

        self.text1_rect.centery -= 300
        self.text2_rect.centery += 0
        self.text3_rect.centery += 200
        self.text4_rect.centerx -= 350
        self.text4_rect.centery -= 400
        self.text5_rect.centery += 325
        self.background.centery += 50

    def handle_events(self, current_screen, previous_screen):
        switch = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect.collidepoint(pygame.mouse.get_pos()):
                self.textbox1.clean()
                self.textbox2.clean()
                return "welcome", previous_screen
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                username_input = self.textbox1.return_actual_text()
                password_input = self.textbox2.return_actual_text()

                db_config = {
                    'host': 'localhost',
                    'user': 'root',
                    'password': '',
                    'database': 'database_fp',
                    'port': '4306'
                }

                try:
                    connection = mysql.connector.connect(**db_config)
                    cursor = connection.cursor()
                    if connection.is_connected():
                        cursor.execute(
                            fr"""SELECT password, salt FROM admins WHERE username = %s""", (username_input,)
                        )

                    results = cursor.fetchone()
                    if results is None:
                        self.text5 = "No username exists"
                        self.text5_image = self.font4.render(self.text5, True, self.font4_color)
                        self.text5_rect = self.text5_image.get_rect()
                        self.text5_rect.center = self.screen_rect.center
                        self.text5_rect.centery += 325
                    else:
                        actual_pass = results[0]
                        salt = results[1]
                        hashed_password = hash_password(password_input, salt)
                        if hashed_password == actual_pass:
                            previous_screen[0] = "admin"
                            return "admin_select", previous_screen
                        else:
                            self.text5 = "Incorrect password"
                            self.text5_image = self.font4.render(self.text5, True, self.font4_color)
                            self.text5_rect = self.text5_image.get_rect()
                            self.text5_rect.center = self.screen_rect.center
                            self.text5_rect.centery += 325

                except mysql.connector.Error as e:
                    print(f"Error connecting to MySQL: {e}")
            else:
                self.textbox1.handle_event(event, False)

                if self.textbox1.is_active and switch == 0:
                    self.textbox2.is_active = False

                switch = self.textbox2.handle_event(event, True)

                if self.textbox1.is_active and switch == 1:
                    self.textbox1.is_active = False
        return current_screen, previous_screen

    def draw_start(self):
        self.textbox1.draw()
        self.textbox2.draw()
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        self.screen.blit(self.text4_image, self.text4_rect)
        self.screen.blit(self.text5_image, self.text5_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 2)
