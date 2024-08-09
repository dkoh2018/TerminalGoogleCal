from add_new_event import add_new_event
from delete_an_event import delete_an_event
from view_events import view_events
from settings import calendar_settings
from see_ya import see_ya


def main_menu():
    while True:
        print("\nWhat would you like to do today?")
        print("1. Add new event(s)")
        print("2. Delete event")
        print("3. View events")
        print("4. User Settings")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_new_event()
        elif choice == "2":
            delete_an_event()
        elif choice == "3":
            view_events()
        elif choice == "4":
            calendar_settings()
        elif choice == "5":
            see_ya()
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    print(
        """
           #######            #######      ###      ##                 
         ##     ##           ##    ##     ## ##     ##                  
         ##                  ##          ##   ##    ##                  
         ##   ####   ####    ##         ## # # ##   ##                 
         ##      #           ##    ##   ##     ##   ##                  
          #######             ######    ##     ##   ########               
        """
    )
    main_menu()
