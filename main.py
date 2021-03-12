import datetime
from datetime import datetime
import random
from _csv import writer
from os import path
import csv

if not path.exists("file.csv"):
    with open('file.csv', 'wb') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        filewriter.writerow(['After Work', 'Before Bed', 'Date'])

current_time = datetime.now().date()
current_time = str(current_time)

import csv
from datetime import datetime

current_time = datetime.now().date()
current_time = str(current_time)

with open('file.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
        if current_time == row[2]:  # if the username shall be on column 3 (-> index 2)
            print(row)

y = ["Python", "YouTube", "Read"]
x = ["Assetto Corsa", "Kingdom Deliverance", "CitiXXl"] + y

after_work = random.choice(x)
before_bed = random.choice(y)

while after_work == before_bed:
    after_work = random.choice(x)

csv_new_row = [after_work, before_bed, current_time]


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


print(
    "Current Time = " + current_time + " " + "\nAfter Work Activity = " + after_work + "\nBefore Bed Activity = " + before_bed)
append_list_as_row('file.csv', csv_new_row)