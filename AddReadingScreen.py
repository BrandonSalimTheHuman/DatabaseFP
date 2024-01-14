import pygame
import mysql.connector
import sys
from DropDown import DropDown
from Numpad import NumPad


class AddReadingScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)
        self.color = (200, 90, 255)

        self.rect = pygame.Rect(0, 150, 400, 37)
        self.rect.centerx = self.screen_rect.centerx

        self.switch = False
        self.switch2 = False

        self.font = pygame.font.Font("Relington.ttf", 40)
        self.font2 = pygame.font.Font("Relington.ttf", 30)
        self.font3 = pygame.font.Font("Relington.ttf", 22)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Choose the suitable parameter", True, self.text_color)
        self.text2_image = self.font2.render("Chosen location:", True, self.text_color)
        self.text3_image = self.font2.render("Back", True, self.text_color)
        self.text4_image = self.font2.render("Then press enter to confirm", True, self.text_color)

        self.continue_msg = self.font3.render("Press enter to return to selection screen.", True, self.text_color)
        self.continue_rect = self.continue_msg.get_rect()

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.border_rect = pygame.Rect(self.text3_rect.left + 27, self.text3_rect.top + 25, self.text3_rect.width + 20,
                                       self.text3_rect.height + 20)

        self.dropdown = DropDown("Choose a parameter", ["Temperature", "Humidity", "Wind speed", "Air pressure",
                                                        "Precipitation", "UV index", "Air quality index"],
                                 self.screen_rect)
        self.dropdown.move_down(100)

        self.numpad = NumPad(self.screen)

        self.main = ""

        self.value = ""

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.continue_rect.center = self.screen_rect.center

        self.text1_rect.centery -= 400
        self.text2_rect.centery -= 340
        self.text3_rect.centerx -= 350
        self.text3_rect.centery -= 400
        self.text4_rect.centery -= 230
        self.continue_rect.centery += 400

    def update_main(self, main):
        self.main = main
        self.msg = self.font2.render(self.main, 1, (0, 0, 0))
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_start(self):
        self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        self.screen.blit(self.text4_image, self.text4_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 2)
        pygame.draw.rect(self.screen, self.color, self.rect, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
        self.screen.blit(self.msg, self.msg_rect)
        if not self.switch:
            self.dropdown.draw(self.screen, False)

        if self.switch:
            pygame.draw.rect(self.screen, self.color, self.rect2, 0)
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect2, 1)
            self.screen.blit(self.msg2, self.msg2_rect)

            self.numpad.draw_start()

            self.screen.blit(self.text6_image, self.text6_rect)
            pygame.draw.rect(self.screen, self.color, self.rect3, 0)
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect3, 1)

            self.value_img = self.font2.render(self.value, True, self.text_color)
            self.value_rect = self.value_img.get_rect()
            self.value_rect.center = self.rect3.center
            self.screen.blit(self.value_img, self.value_rect)

        if self.switch2:
            pygame.draw.rect(self.screen, self.color, self.rect3, 0)
            pygame.draw.rect(self.screen, (0, 0, 0), self.rect3, 1)
            self.screen.blit(self.text6_image, self.text6_rect)
            self.screen.blit(self.value_img, self.value_rect)
            self.screen.blit(self.status_msg, self.status_msg_rect)
            self.screen.blit(self.overall_status, self.overall_status_rect)
            self.screen.blit(self.continue_msg, self.continue_rect)

    def handle_events(self, current_screen):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect.collidepoint(pygame.mouse.get_pos()):
                if self.switch:
                    self.switch = False
                    self.text1_image = self.font.render("Choose the suitable parameter", True, self.text_color)
                    self.text1_rect = self.text1_image.get_rect()
                    self.text4_image = self.font2.render("Then press enter to confirm", True, self.text_color)
                    self.text4_rect = self.text4_image.get_rect()
                    self.text1_rect.center = self.text4_rect.center = self.screen_rect.center
                    self.text1_rect.centery -= 400
                    self.text4_rect.centery -= 230
                elif self.switch2:
                    self.value = ""
                    self.switch2 = False
                    self.switch = True
                else:
                    self.dropdown.main = "Choose a parameter"
                    return "selection"
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.switch2:
                    self.switch = False
                    self.switch2 = False
                    self.event_status_switch = False
                    self.location_status_switch = False
                    self.dropdown.main = "Choose a parameter"
                    return "admin_select"

                elif not self.switch and self.dropdown.result() != "Choose a parameter":
                    self.name = self.dropdown.result()
                    self.msg2 = self.font2.render(self.name, 1, (0, 0, 0))
                    self.msg2_rect = self.msg2.get_rect()
                    self.rect2 = pygame.Rect(0, 250, 400, 37)
                    self.rect2.centerx = self.screen_rect.centerx
                    self.msg2_rect.center = self.rect2.center
                    self.text4_image = self.font2.render("Chosen parameter:", True, self.text_color)
                    self.text4_rect = self.text4_image.get_rect()
                    self.text4_rect.centerx = self.screen_rect.centerx
                    self.text4_rect.centery += 200
                    self.switch = True
                    self.value = ""
                    self.numpad.reset()

                    self.text1_image = self.font.render("Enter the value for the reading", True, self.text_color)
                    self.text6_image = self.font2.render("Then press enter to confirm", True, self.text_color)
                    self.rect3 = pygame.Rect(0, 100, 400, 37)
                    self.rect3.centerx = self.screen_rect.centerx
                    self.rect3.centery += 260
                    self.text1_rect = self.text1_image.get_rect()
                    self.text6_rect = self.text6_image.get_rect()
                    self.text1_rect.center = self.text6_rect.center = self.screen_rect.center
                    self.text1_rect.centery -= 400
                    self.text6_rect.centery -= 120

                elif self.switch and not self.switch2 and self.value != "" and self.value[-1] != ".":
                    self.text6_image = self.font2.render("Entered value:", True, self.text_color)
                    self.text6_rect = self.text6_image.get_rect()
                    self.text6_rect.center = self.screen_rect.center
                    self.text6_rect.centery -= 120
                    self.switch2 = True
                    self.switch = False

                    db_config = {
                        'host': 'localhost',
                        'user': 'root',
                        'password': '',
                        'database': 'database_fp',
                        'port': '4306'
                    }

                    try:
                        connection = mysql.connector.connect(**db_config)
                        if connection.is_connected():

                            cursor = connection.cursor()

                            cursor.execute(
                                fr"""SELECT safe_value_min, safe_value_max, moderate_value_min, moderate_value_max, 
                                 parameter_id FROM parameters WHERE parameter_name = %s""", (self.name,)
                            )

                            results = cursor.fetchone()

                            safe_value_min, safe_value_max, moderate_value_min, moderate_value_max, parameter_id = \
                                results

                            if parameter_id == 1 or parameter_id == 2 or parameter_id == 4:
                                if safe_value_min <= float(self.value) <= safe_value_max:
                                    status = "safe"
                                elif moderate_value_min <= float(self.value) <= moderate_value_max:
                                    status = "moderate"
                                else:
                                    status = "dangerous"
                            else:
                                if safe_value_min <= float(self.value) < safe_value_max:
                                    status = "safe"
                                elif moderate_value_min <= float(self.value) < moderate_value_max:
                                    status = "moderate"
                                else:
                                    status = "dangerous"

                            cursor.execute(
                                fr"""SELECT location_id, overall_status FROM locations WHERE location_name = %s""",
                                (self.main,)
                            )

                            results = cursor.fetchone()

                            location_id, original_status = results

                            cursor.execute(
                                fr"""UPDATE `data_readings` SET `value` = %s, `status` = %s, `timestamp` = 
                                CURRENT_TIMESTAMP WHERE location_id = %s AND parameter_id = %s""",
                                (float(self.value), status, location_id, parameter_id)
                            )

                            connection.commit()

                            self.status_msg = self.font2.render("Status for data reading: " + status, True,
                                                                self.text_color)
                            self.status_msg_rect = self.status_msg.get_rect()
                            self.status_msg_rect.center = self.screen_rect.center
                            self.status_msg_rect.centery += 150

                            cursor.execute(
                                fr"""SELECT parameter_id, status FROM data_readings WHERE location_id = %s""",
                                (location_id,)
                            )

                            results = cursor.fetchall()
                            sum_status = 0

                            parameter_weight = [0.2, 0.15, 0.1, 0.05, 0.15, 0.2, 0.15]

                            for i in range(len(results)):
                                tmp_parameter_id = int(results[i][0]) - 1
                                tmp_weight = parameter_weight[tmp_parameter_id]
                                tmp_status = results[i][1]
                                if tmp_status == "safe":
                                    sum_status += tmp_weight
                                elif tmp_status == "moderate":
                                    sum_status += (2 * tmp_weight)
                                else:
                                    sum_status += (3 * tmp_weight)

                            if sum_status < 1.6:
                                overall_status = "safe"
                            elif sum_status < 2.2:
                                overall_status = "moderate"
                            else:
                                overall_status = "dangerous"

                            if original_status != overall_status:
                                text = "Old location status: " + original_status + ", new location status: " + \
                                       overall_status

                            else:
                                text = "Location status: " + overall_status + ", overall status didn't change"

                            self.overall_status = self.font2.render(text, True, self.text_color)
                            self.overall_status_rect = self.overall_status.get_rect()
                            self.overall_status_rect.center = self.screen_rect.center
                            self.overall_status_rect.centery += 250

                            cursor.execute(
                                fr"""UPDATE `locations` SET `overall_status` = %s WHERE location_id = %s """,
                                (overall_status, location_id,)
                            )
                            connection.commit()

                    except mysql.connector.Error as e:
                        print(f"Error connecting to MySQL: {e}")

            elif self.switch and event.type == pygame.MOUSEBUTTONDOWN:
                self.value = self.numpad.handle_events(self.value)

        selected_option = self.dropdown.update(event_list, False)
        if selected_option >= 0:
            self.dropdown.main = self.dropdown.options[selected_option]

        if not self.switch:
            self.dropdown.draw(self.screen, False)
        return current_screen
