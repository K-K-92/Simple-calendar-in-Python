from menu import Menu, MenuCommand, ExitCommand, AddEventCommand, ListAllCommands, ExportCommand
from calendar import ListingStrategy, list_calendar

def main():
  
    calendar = []

    menu = Menu()

    menu = Menu()

    add_cmd = AddEventCommand(calendar)
    menu.add_command(add_cmd)

    list_all_cmd = ListAllCommands(calendar)
    menu.add_command(list_all_cmd)

    export = ExportCommand(calendar)
    menu.add_command(export)

    exit_cmd = ExitCommand(menu)
    menu.add_command(exit_cmd)


    menu.run()


main()
