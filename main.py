import pygame
import sys
from WelcomeScreen import WelcomeScreen
from AdminLogin import AdminLogin
from SelectionMenu import SelectionMenu
from ResultScreen import ResultScreen
from AdminActionSelection import AdminActionSelection
from AddReadingScreen import AddReadingScreen
from AddEventScreen import AddEventScreen


def run():
    pygame.init()

    screen = pygame.display.set_mode((830, 900))
    pygame.display.set_caption("NimbusNav")

    welcome_screen = WelcomeScreen(screen)
    welcome_screen.initialize_start_text()

    admin_login = AdminLogin(screen)
    admin_login.initialize_start_text()

    selection_screen = SelectionMenu(screen)
    selection_screen.initialize_start_text()

    result_screen = ResultScreen(screen)
    result_screen.initialize_start_text()

    admin_selection = AdminActionSelection(screen)
    admin_selection.initialize_start_text()

    add_reading = AddReadingScreen(screen)
    add_reading.initialize_start_text()

    add_event = AddEventScreen(screen)
    add_event.initialize_start_text()

    current_screen = "welcome"
    previous_screen = ["", ""]

    while True:
        screen.fill((204, 204, 255))

        if current_screen == "welcome":
            welcome_screen.draw_start()
            current_screen, previous_screen, selection_screen = welcome_screen.handle_events(current_screen,
                                                                                             previous_screen,
                                                                                             selection_screen)
        if current_screen == "admin":
            admin_login.draw_start()
            current_screen, previous_screen = admin_login.handle_events(current_screen, previous_screen)
        if current_screen == "selection":
            selection_screen.draw_start()
            current_screen, result_screen, previous_screen, add_reading, add_event = selection_screen.handle_events(
                current_screen,
                result_screen,
                previous_screen,
                add_reading,
                add_event)
        if current_screen == "result":
            result_screen.draw_start()
            current_screen = result_screen.handle_events(current_screen)
        if current_screen == "admin_select":
            admin_selection.draw_start()
            current_screen, previous_screen, selection_screen = admin_selection.handle_events(current_screen,
                                                                                              previous_screen,
                                                                                              selection_screen)
        if current_screen == "add_reading":
            add_reading.draw_start()
            current_screen = add_reading.handle_events(current_screen)

        if current_screen == "add_event":
            add_event.draw_start()
            current_screen = add_event.handle_events(current_screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()


run()
