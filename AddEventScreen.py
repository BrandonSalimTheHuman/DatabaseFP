import pygame
import mysql.connector
import sys
from DropDown import DropDown
from TextBox import TextBox


def status_weight(status):
    if status == "none":
        return 0
    elif status == "safe":
        return 1
    elif status == "moderate":
        return 2
    elif status == "dangerous":
        return 3


class AddEventScreen:
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.text_color = (48, 25, 52)
        self.color = (200, 90, 255)

        self.rect = pygame.Rect(0, 150, 400, 37)
        self.rect.centerx = self.screen_rect.centerx

        self.switch = False
        self.switch2 = False
        self.event_status_switch = False
        self.location_status_switch = False
        self.delete_switch = False
        self.delete_confirm = False

        self.font = pygame.font.Font("Relington.ttf", 40)
        self.font2 = pygame.font.Font("Relington.ttf", 30)
        self.font3 = pygame.font.Font("Relington.ttf", 22)
        self.font4 = pygame.font.Font("Relington.ttf", 55)

    def initialize_start_text(self):
        self.text1_image = self.font.render("Enter the event type:", True, self.text_color)
        self.text2_image = self.font2.render("Chosen location:", True, self.text_color)
        self.text3_image = self.font2.render("Back", True, self.text_color)
        self.text4_image = self.font2.render("Then press enter to confirm", True, self.text_color)

        self.continue_msg = self.font3.render("Press enter to return to selection screen.", True, self.text_color)
        self.continue_rect = self.continue_msg.get_rect()

        self.delete_image = self.font2.render("Or click here to delete the event on this location", True,
                                              self.text_color)
        self.delete_rect = self.delete_image.get_rect()

        self.delete_msg = self.font4.render("Event successfully deleted", True, self.text_color)
        self.delete_msg_rect = self.delete_msg.get_rect()

        self.border_rect_delete = pygame.Rect(115, 525, 600, 50)

        self.text1_rect = self.text1_image.get_rect()
        self.text2_rect = self.text2_image.get_rect()
        self.text3_rect = self.text3_image.get_rect()
        self.text4_rect = self.text4_image.get_rect()
        self.border_rect = pygame.Rect(self.text3_rect.left + 27, self.text3_rect.top + 25, self.text3_rect.width + 20,
                                       self.text3_rect.height + 20)

        self.textbox = TextBox(self.screen, (120, 280, 600, 60))

        self.dropdown = DropDown("Choose event status", ["safe", "moderate", "dangerous"], self.screen_rect)
        self.dropdown.move_down(300)

        self.main = ""

        self.value = ""

        self.text1_rect.center = self.text2_rect.center = self.text3_rect.center = self.text4_rect.center = \
            self.continue_rect.center = self.delete_rect.center = self.delete_msg_rect.center = self.screen_rect.center
        self.text1_rect.centery -= 400
        self.text2_rect.centery -= 340
        self.text3_rect.centerx -= 350
        self.text3_rect.centery -= 400
        self.text4_rect.centery -= 215
        self.continue_rect.centery += 400
        self.delete_rect.centery += 100
        self.delete_msg_rect.centery += 100

    def update_main(self, main):
        self.main = main
        self.msg = self.font2.render(self.main, 1, (0, 0, 0))
        self.msg_rect = self.msg.get_rect()
        self.msg_rect.center = self.rect.center

    def draw_start(self):
        if not self.delete_switch and not self.delete_confirm:
            self.screen.blit(self.text1_image, self.text1_rect)
        self.screen.blit(self.text2_image, self.text2_rect)
        self.screen.blit(self.text3_image, self.text3_rect)
        pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect, 2)
        pygame.draw.rect(self.screen, self.color, self.rect, 0)
        pygame.draw.rect(self.screen, (0, 0, 0), self.rect, 1)
        self.screen.blit(self.msg, self.msg_rect)

        if not self.delete_switch:
            self.screen.blit(self.text4_image, self.text4_rect)
            self.textbox.draw()
            if not self.switch:
                self.screen.blit(self.delete_image, self.delete_rect)
                pygame.draw.rect(self.screen, (0, 0, 0), self.border_rect_delete, 3)
            if self.switch:
                self.dropdown.draw(self.screen, False)
                self.screen.blit(self.text5_image, self.text5_rect)

            if self.switch2:
                self.screen.blit(self.continue_msg, self.continue_rect)

            if self.event_status_switch:
                self.screen.blit(self.text6_image, self.text6_rect)

            if self.location_status_switch:
                self.screen.blit(self.text7_image, self.text7_rect)
        elif self.delete_confirm:
            self.screen.blit(self.delete_msg, self.delete_msg_rect)
            self.screen.blit(self.continue_msg, self.continue_rect)
        elif self.event_search_result is not None:
            self.screen.blit(self.confirm1_image, self.confirm1_rect)
            self.screen.blit(self.confirm2_image, self.confirm2_rect)
            self.screen.blit(self.confirm3_image, self.confirm3_rect)
        else:
            self.screen.blit(self.no_event_msg, self.no_event_rect)

    def handle_events(self, current_screen):
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect.collidepoint(pygame.mouse.get_pos()):
                if self.delete_switch:
                    self.delete_switch = False
                    self.delete_confirm = False
                elif self.switch and not self.switch2:
                    self.switch = False
                    self.text1_image = self.font.render("Enter the event type:", True, self.text_color)
                    self.text1_rect = self.text1_image.get_rect()
                    self.text4_image = self.font2.render("Then press enter to confirm", True, self.text_color)
                    self.text4_rect = self.text4_image.get_rect()
                    self.text1_rect.center = self.text4_rect.center = self.screen_rect.center
                    self.text1_rect.centery -= 400
                    self.text4_rect.centery -= 215
                elif self.switch2:
                    self.value = ""
                    self.switch2 = False
                    self.switch = True
                    self.event_status_switch = False
                    self.location_status_switch = False
                else:
                    self.dropdown.main = "Choose event status"
                    return "selection"
            elif event.type == pygame.MOUSEBUTTONDOWN and self.border_rect_delete.collidepoint(pygame.mouse.get_pos()):
                self.delete_switch = True

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
                            fr"""SELECT events.event_type, locations.location_id FROM events JOIN locations ON 
                            events.location_id = locations.location_id WHERE locations.location_name = %s""",
                            (self.main, )
                        )

                    self.event_search_result = cursor.fetchone()
                    if self.event_search_result is not None:
                        event_type, self.delete_location = self.event_search_result
                        self.confirm1_image = self.font4.render("Deleting event:", True, (255, 0, 0))
                        self.confirm2_image = self.font4.render(event_type, True, (255, 0, 0))
                        self.confirm3_image = self.font.render("Press enter to confirm", True, self.text_color)

                        self.confirm1_rect = self.confirm1_image.get_rect()
                        self.confirm2_rect = self.confirm2_image.get_rect()
                        self.confirm3_rect = self.confirm3_image.get_rect()

                        self.confirm1_rect.center = self.confirm2_rect.center = self.confirm3_rect.center = \
                            self.screen_rect.center

                        self.confirm1_rect.centery -= 100
                        self.confirm2_rect.centery += 50
                        self.confirm3_rect.centery += 250
                    else:
                        self.no_event_msg = self.font4.render("No event in this location", True, self.text_color)
                        self.no_event_rect = self.no_event_msg.get_rect()
                        self.no_event_rect.center = self.screen_rect.center
                        self.no_event_rect.centery += 100

                except mysql.connector.Error as e:
                    print(f"Error connecting to MySQL: {e}")

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN and self.delete_switch \
                    and not self.delete_confirm and self.event_search_result is not None:
                self.delete_confirm = True

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
                            fr"""DELETE FROM events WHERE location_id = %s""",
                            (self.delete_location,)
                        )

                        connection.commit()

                except mysql.connector.Error as e:
                    print(f"Error connecting to MySQL: {e}")

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if self.switch2 or self.delete_confirm:
                    self.switch = False
                    self.switch2 = False
                    self.event_status_switch = False
                    self.location_status_switch = False
                    self.delete_switch = False
                    self.delete_confirm = False
                    self.textbox.clean()
                    self.dropdown.clean()
                    self.dropdown.main = "Choose event status"
                    return "admin_select"

                elif not self.switch and self.textbox.return_actual_text() != "":
                    self.event_type = self.textbox.return_actual_text()
                    self.text1_image = self.font.render("Choose the status for the event:", True, self.text_color)
                    self.text4_image = self.font2.render("Entered location type:", True, self.text_color)
                    self.text5_image = self.font2.render("Then press enter to confirm", True, self.text_color)
                    self.text1_rect = self.text1_image.get_rect()
                    self.text4_rect = self.text4_image.get_rect()
                    self.text5_rect = self.text5_image.get_rect()
                    self.text1_rect.center = self.text4_rect.center = self.text5_rect.center = self.screen_rect.center
                    self.text1_rect.centery -= 400
                    self.text4_rect.centery -= 215
                    self.text5_rect.centery -= 50
                    self.switch = True
                elif self.switch and self.dropdown.result() != "Choose event status":
                    self.switch2 = True
                    self.status = self.dropdown.result()

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
                                fr"""SELECT events.event_status, locations.location_id, locations.overall_status FROM 
                                events JOIN locations ON events.location_id = locations.location_id WHERE 
                                locations.location_name = %s""",
                                (self.main,)
                            )

                            results = cursor.fetchone()
                            if results is not None:
                                event_status, location_id, overall_status = results
                            else:
                                cursor.execute(
                                    fr"""SELECT location_id, overall_status FROM locations WHERE location_name = %s""",
                                    (self.main,)
                                )

                                event_status = "none"

                                results2 = cursor.fetchone()
                                location_id, overall_status = results2

                            if results is None:
                                cursor.execute(
                                    fr"""INSERT INTO `events`(`location_id`, `event_type`, `event_status`) VALUES (
                                    %s, %s, %s)""", (location_id, self.event_type, self.status)
                                )

                                self.text6_image = self.font2.render("Event successfully entered.", True,
                                                                     self.text_color)
                                self.text6_rect = self.text6_image.get_rect()
                                self.text6_rect.center = self.screen_rect.center
                                self.text6_rect.centery += 250

                                self.event_status_switch = True

                                connection.commit()

                            else:
                                if status_weight(self.status) >= status_weight(event_status):
                                    if status_weight(self.status) == status_weight(event_status):
                                        text = "Event updated, no status change."
                                    else:
                                        text = "Event updated, " + event_status + " to " + self.status

                                    self.text6_image = self.font2.render(text, True, self.text_color)
                                    self.text6_rect = self.text6_image.get_rect()
                                    self.text6_rect.center = self.screen_rect.center
                                    self.text6_rect.centery += 250

                                    self.event_status_switch = True

                                    cursor.execute(
                                        fr"""UPDATE `events` set `event_type` = %s, `event_status` = %s 
                                        WHERE location_id = %s""", (self.event_type, self.status, location_id)
                                    )

                                    connection.commit()

                                else:
                                    text = "Event not updated, less dangerous"
                                    self.text6_image = self.font2.render(text, True, self.text_color)
                                    self.text6_rect = self.text6_image.get_rect()
                                    self.text6_rect.center = self.screen_rect.center
                                    self.text6_rect.centery += 250

                                    self.event_status_switch = True

                            cursor.execute(
                                fr"""SELECT event_status FROM events WHERE location_id = %s""", (location_id,)
                            )

                            results = cursor.fetchone()
                            event_status = results[0]

                            if status_weight(event_status) > status_weight(overall_status):
                                text = "Location status changed to " + event_status
                                self.text7_image = self.font2.render(text, True, self.text_color)
                                self.text7_rect = self.text7_image.get_rect()
                                self.text7_rect.center = self.screen_rect.center
                                self.text7_rect.centery += 300

                                self.location_status_switch = True

                    except mysql.connector.Error as e:
                        print(f"Error connecting to MySQL: {e}")
            else:
                if not self.switch:
                    self.textbox.handle_event(event, False)

        selected_option = self.dropdown.update(event_list, False)
        if selected_option >= 0:
            self.dropdown.main = self.dropdown.options[selected_option]

        return current_screen
