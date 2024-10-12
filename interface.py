import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_start_screen():
    clear_console()
    print("""
  ____  _   _ ____  ____   ___  ____ _____           _   _ _____ _     ____  _____ ____  
 / ___|| | | |  _ \|  _ \ / _ \|  _ \_   _|         | | | | ____| |   |  _ \| ____|  _ \ 
 \___ \| | | | |_) | |_) | | | | |_) || |    _____  | |_| |  _| | |   | |_) |  _| | |_) |
  ___) | |_| |  __/|  __/| |_| |  _ < | |   |_____| |  _  | |___| |___|  __/| |___|  _ < 
 |____/ \___/|_|   |_|    \___/|_| \_\|_|           |_| |_|_____|_____|_|   |_____|_| \_\ 
                                                                                         """)
    print("version 0.0.1 by ferieninsel001")
    time.sleep(1)

def main_menu():
    while True:
        print("\n")
        print("1. Sort Desktop ")
        print("2. Sort Custom Location")
        print("3. Clear Cache and History")
        choice = input("opt (1-3): ")

        if choice == '1':
            import tools.file_organizer.desktop_sorter
        elif choice == '2':
            import tools.file_organizer.custom_sorter
        elif choice == '3':
            import tools.browser_cleaner.cleaner
        elif choice == '':
            print("Exiting...")
            time.sleep(1)
            break
        else:
            print("Invalid option to exit press enter")




if __name__ == '__main__':
    display_start_screen()
    main_menu()
