
import string
import calendar

class MenuCommand:
    def description(self):
        raise NotImplementedError

    def execute(self):
        raise NotImplementedError


class ExitCommand(MenuCommand):
    def __init__(self, menu):
        super().__init__()
        self._menu = menu

    def description(self):
        return "Exit"

    def execute(self):
        self._menu.stop()


class AddEventCommand(MenuCommand):
    def __init__(self, calendar):
        self._calendar = calendar

    def description(self):
        return "New event"

    def _time_check(self,time):
        if len(time) != 5 or time[2] != ":" or time[0] not in string.digits or time[1] not in string.digits or time[3] not in string.digits or time[4] not in string.digits:
            raise ValueError("Invalid input")

    def _date_check(self,date):
        if len(date) != 10 or date[2]!="." or date[5]!="." or date[0] not in string.digits or date[1] not in string.digits or date[3] not in string.digits or date[4] not in string.digits or date[6] not in string.digits or date[7] not in string.digits or date[8] not in string.digits or date[9] not in string.digits:
            raise ValueError("Invalid input")

    def _title_check(self,title):

        if len(title) == 0:
            raise ValueError("Invalid input")

        self.wrong_signs = "[@_!#$%^&*()<>?/\|}{~:];"

        for i in self.wrong_signs:
            for j in title:
                if i == j:
                    raise ValueError("Invalid input")

    def execute(self):
        event = {}
        try:
            title = input("Title: ")
            self._title_check(title)
            date = input("Date(DD.MM.YYYY): ")
            self._date_check(date)
            time = input("Time (HH:MM): ")
            self._time_check(time)
            event["title"] = title
            event["date"] = date
            event["time"] = time
            self._calendar.append(event)
        except ValueError:
            print("Invalid input")



class ListAllCommands(MenuCommand):
    def __init__(self, calendar):
        self._calendar = calendar

    def description(self):
        return "List calendar"

    def execute(self):
        calendar.list_calendar(self._calendar,calendar.ConsoleView())
        #for i in range(len(self._calendar)):
        #    print("Title: ", self._calendar[i]["title"])
        #    print("Date: ", self._calendar[i]["date"], ", ", self._calendar[i]["time"])


class ExportCommand(MenuCommand):
    def __init__(self, calendar):
        self._calendar = calendar

    def description(self):
        return "Export calendar to iCalendar"

    def execute(self):
        calendar.list_calendar(self._calendar,calendar.iCalendar())


class Menu:
    def __init__(self):
        self._commands = []
        self._should_running = True

    def add_command(self, cmd):
        self._commands.append(cmd)

    def run(self):
        while self._should_running:
            self._display_menu()
            self._execute_selected_command()

    def stop(self):
        self._should_running = False

    def _display_menu(self):
        for i, cmd in enumerate(self._commands):
            print("{}. {}".format(i + 1, cmd.description()))

    def _execute_selected_command(self):

        try:
            cmd_num = int(input("Select menu item (1-{}): ".format(len(self._commands))))
            cmd = self._commands[cmd_num - 1]
            cmd.execute()
        except ValueError:
            print("Invalid input")
        except IndexError:
            print("Invalid input")


