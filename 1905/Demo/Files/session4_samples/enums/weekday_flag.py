from enum import Flag
class Weekday(Flag):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 4
    THURSDAY = 8
    FRIDAY = 16
    SATURDAY = 32
    SUNDAY = 64

if __name__ == "__main__":
    weekend = Weekday.SATURDAY | Weekday.SUNDAY

    for day in weekend:
        print(day)
