from datetime import datetime

now = datetime.now()

current_time = now.strftime("%Y-%m-%d %H:%M %p")

print("Current time is : ", current_time)
