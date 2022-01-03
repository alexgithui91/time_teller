from datetime import datetime

"""
Tell us the current datetime as : 09:00 AM Monday 3 August 2022
Tell us the number of month, weeks, days to end of year
Tell us the number of hours, minutes and seconds to end year
See if it is possible to get Kenyan Holiday Calendar
"""

time_now = datetime.now()


def breakdown_1(time_now):
    current_date = time_now.strftime("%A, %d %B %Y")
    current_time = time_now.strftime("%H:%M %p")

    print("Current Date : ", current_date)
    print("Current Time : ", current_time)


def breakdown_2():
    pass


def breakdown_3():
    pass


def main():
    breakdown_1(time_now)
    # breakdown_2()
    # breakdown_3()


if __name__ == "__main__":
    main()
