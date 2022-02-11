from datetime import datetime
from datetime import date

"""
Tell us the current datetime as : 09:00 AM Monday 3 August 2022
Tell us the number of days, hours, minutes and seconds to end of year
"""

pg_break = "*" * 50


def breakdown_1():
    print(pg_break)
    current_date = datetime.now().strftime("%A, %d %B %Y")
    current_time = datetime.now().strftime("%H:%M %p")

    print("Current Date : ", current_date)
    print("Current Time : ", current_time)


def breakdown_2():
    t1 = datetime(
        year=date.today().year,
        month=date.today().month,
        day=date.today().day,
        hour=int(datetime.now().strftime("%H")),
        minute=int(datetime.now().strftime("%M")),
        second=int(datetime.now().strftime("%S")),
    )
    t2 = datetime(
        year=date.today().year, month=12, day=31, hour=23, minute=59, second=59
    )
    print("End year (days/hours/minutes/seconds) : " + str(t2 - t1))


def main():
    breakdown_1()
    breakdown_2()


if __name__ == "__main__":
    main()
