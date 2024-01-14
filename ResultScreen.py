import pygame
import mysql.connector
import sys


def status_weight(status):
    if status == "none":
        return 0
    elif status == "safe":
        return 1
    elif status == "moderate":
        return 2
    elif status == "dangerous":
        return 3


class ResultScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)
        self.color = (200, 90, 255)
        self.color_safe = (20, 155, 150)
        self.color_moderate = (245, 255, 20)
        self.color_dangerous = (255, 0, 0)

        self.rect = pygame.Rect(0, 150, 400, 37)
        self.rect.centerx = self.screen_rect.centerx

        self.font = pygame.font.Font("Relington.ttf", 40)
        self.font2 = pygame.font.Font("Relington.ttf", 30)
        self.font3 = pygame.font.Font("Relington.ttf", 60)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Results", True, self.text_color)
        self.text2_image = self.font2.render("Chosen location:", True, self.text_color)
        self.text3_image = self.font2.render("Back", True, self.text_color)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.border_rect = pygame.Rect(self.text3_rect.left + 27, self.text3_rect.top + 25, self.text3_rect.width + 20,
                                       self.text3_rect.height + 20)

        self.main = ""
        self.shift_switch = False

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.screen_rect.center
        self.text1_rect.centery -= 400
        self.text2_rect.centery -= 340
        self.text3_rect.centerx -= 350
        self.text3_rect.centery -= 400

    def update_main(self, main):
        self.main = main
        self.msg = self.font2.render(self.main, 1, (0, 0, 0))
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.center = self.rect.center

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
                    fr"""SELECT parameters.parameter_name, data_readings.status, locations.overall_status, 
                    parameters.unit_of_measurement, data_readings.value FROM locations JOIN data_readings ON 
                    locations.location_id = data_readings.location_id JOIN parameters ON parameters.parameter_id = 
                    data_readings.parameter_id WHERE locations.location_name = %s""",
                    (self.main,)
                )

                results = cursor.fetchall()
                self.result_images = []
                self.result_rects = []

                cursor.execute(
                    fr"""SELECT events.event_type, events.event_status FROM events JOIN locations ON events.location_id = 
                                    locations.location_id WHERE locations.location_name = %s""",
                    (self.main,)
                )

                results2 = cursor.fetchone()
                if results2 is not None:
                    self.shift_switch = True
                    event_type, self.event_status = results2
                    text = "Event: " + event_type + ", " + self.event_status

                    if self.event_status == "safe":
                        color_to_use = self.color_safe
                    elif self.event_status == "moderate":
                        color_to_use = self.color_moderate
                    else:
                        color_to_use = self.color_dangerous

                    self.event_image = self.font.render(text, True, color_to_use)
                    self.event_rect = self.event_image.get_rect()
                    self.event_rect.center = self.screen_rect.center
                    self.event_rect.centery += 260
                else:
                    self.shift_switch = False

                for i in range(len(results)):
                    parameter_name = results[i][0]
                    status = results[i][1]
                    measurement = results[i][3]
                    value = results[i][4]
                    text = parameter_name + ": " + str(value)
                    if measurement is not None:
                        text += measurement + " "
                    else:
                        text += " "
                    if status == "safe":
                        color_to_use = self.color_safe
                    elif status == "moderate":
                        color_to_use = self.color_moderate
                    else:
                        color_to_use = self.color_dangerous

                    tmp_image = self.font.render(text, True, self.text_color)
                    tmp_image2 = self.font.render("(" + status + ")", True, color_to_use)

                    total_width = tmp_image.get_width() + tmp_image2.get_width()
                    combined_surface = pygame.Surface((total_width, tmp_image.get_height()))
                    combined_surface.fill((204, 204, 255))
                    combined_surface.blit(tmp_image, (0, 0))
                    combined_surface.blit(tmp_image2, (tmp_image.get_width(), 0))
                    combined_rect = combined_surface.get_rect()

                    combined_rect.center = self.screen_rect.center
                    combined_rect.centery -= 150
                    combined_rect.centery += (i * 60)
                    if self.shift_switch:
                        combined_rect.centery -= 30

                    self.result_images.append(combined_surface)
                    self.result_rects.append(combined_rect)

                overall_status = results[0][2]

                if self.shift_switch:
                    if status_weight(self.event_status) > status_weight(overall_status):
                        overall_status = self.event_status

                if overall_status == "safe":
                    color_to_use = self.color_safe
                elif overall_status == "moderate":
                    color_to_use = self.color_moderate
                else:
                    color_to_use = self.color_dangerous

                overall_image = self.font3.render("Overall: ", True, self.text_color)
                overall_image2 = self.font3.render(overall_status, True, color_to_use)

                overall_width = overall_image.get_width() + overall_image2.get_width()

                combined_overall_surface = pygame.Surface((overall_width, overall_image.get_height()))
                combined_overall_surface.fill((204, 204, 255))
                combined_overall_surface.blit(overall_image, (0, 0))
                combined_overall_surface.blit(overall_image2, (overall_image.get_width(), 0))

                combined_overall_rect = combined_overall_surface.get_rect()
                combined_overall_rect.center = self.screen_rect.center
                combined_overall_rect.centery += 330
                if self.shift_switch:
                    combined_overall_rect.centery += 15

                self.result_images.append(combined_overall_surface)
                self.result_rects.append(combined_overall_rect)

        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")

    def draw_start(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 2)
        pygame.draw.rect(self.screen, self.color, self.rect, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
        self.screen.blit(self.msg, self.msg_rect)

        for i in range(len(self.result_images)):
            self.screen.blit(self.result_images[i], self.result_rects[i])

        if self.shift_switch:
            self.screen.blit(self.event_image, self.event_rect)

    def handle_events(self, current_screen):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect.collidepoint(pygame.mouse.get_pos()):
                return "selection"

        return current_screen
