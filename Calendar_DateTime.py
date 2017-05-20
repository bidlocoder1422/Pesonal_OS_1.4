import calendar


class Date_Work:

    def show_calendar(self, year):
        year = int(year)
        obj = calendar.TextCalendar(0)
        print(obj.formatyear(year))
