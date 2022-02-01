import datetime
from datetime import datetime

"""
Tell us the current datetime as : 09:00 AM Monday 3 August 2022
Tell us the number of days, hours, minutes and seconds to end of year
See if it is possible to get Kenyan Holiday Calendar
"""

time_now = datetime.now()
pg_break = "*" * 50


def breakdown_1(time_now):
    print(pg_break)
    current_date = time_now.strftime("%A, %d %B %Y")
    current_time = time_now.strftime("%H:%M %p")

    print("Current Date : ", current_date)
    print("Current Time : ", current_time)


def breakdown_2(time_now):
    print(pg_break)
    print(datetime.datetime("2022-12-31 23:59:59"))


def breakdown_3():
    pass


def main():
    breakdown_1(time_now)
    breakdown_2(time_now)
    # breakdown_3()


if __name__ == "__main__":
    main()
