from weekday_flag import Weekday

chores_for_ethan = {
    'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
    'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
    'answer SO questions': Weekday.SATURDAY,
    }

def show_chores(chores, day):
    for chore, days in chores.items():
        if day in days:
            print(chore)

show_chores(chores_for_ethan, Weekday.SATURDAY)