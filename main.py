import datetime
import random

now = datetime.datetime.now()
current_time = now.strftime("%H:%M:%S")


y = ["Python", "YouTube", "Read"]
x = ["Assetto Corsa", "Kingdom Deliverance", "CitiXXl"] + y

after_work = random.choice(x)
before_bed = random.choice(y)

while after_work == before_bed:
    after_work = random.choice(x)

print(
    "Current Time = " + current_time + " " + "\nAfter Work Activity = " + after_work + "\nBefore Bed Activity = " + before_bed)
