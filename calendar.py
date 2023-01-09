
class ListingStrategy:
    def begin(self):
        pass

    def event(self, title, date, time):
        pass

    def end(self):
        pass

class ConsoleView(ListingStrategy):
    def event(self, title, date, time):
        print("Title: "+ title)
        print("Date: " + date + ", " + time)

class iCalendar(ListingStrategy):
    def begin(self):
        print("BEGIN:VCALENDAR\nVERSION:2.0\nBEGIN:VTIMEZONE\nTZID:Europe/Warsaw\nX-LIC-LOCATION:Europe/Warsaw\nEND:VTIMEZONE")

    def event(self, title, date, time):
        date = date[6:10]+date[3:5]+date[0:2]
        time = "T"+time[0:2]+time[3:5]+"00"
        fulltime = date+time

        print("BEGIN:VEVENT\n"
              "DTSTART:"+fulltime+"\n"
              "DTEND:"+fulltime+"\n"
              "SUMMARY:"+title+"\n"
              "END:VEVENT")

    def end(self):
        print("END:VCALENDAR")


def list_calendar(calendar, listing_strategy):
    listing_strategy.begin()

    for event in calendar:
        title = event['title']
        date = event['date']
        time = event['time']
        listing_strategy.event(title, date, time)

    listing_strategy.end()
