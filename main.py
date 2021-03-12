import csv
import os
import random
import sys
from _csv import writer
from datetime import datetime

global after_work
global before_bed
global csv_new_row


# Check if CSV files exist
def check_csv():
    if not os.path.exists('log.csv'):
        with open('log.csv', 'wb') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['Afternoon', 'Evening', 'Date'])
    if not os.path.exists('activities.csv'):
        with open('activities.csv', 'wb') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow(['Afternoon', 'Evening'])


current_time = datetime.now().date()
current_time = str(current_time)


def already_run():
    with open('log.csv', 'rt') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row[1] == current_time:
                final_line = f.readlines()[-1]
                sys.exit(final_line)
            else:
                break


def random_select():
    # y = ["Python", "YouTube", "Read"]
    # x = ["Assetto Corsa", "Kingdom Deliverance", "CitiXXl"] + y
    import pandas

    import pandas as pd

    dict_from_csv = pd.read_csv('activities.csv', header=0, squeeze=True, index=False).to_dict()
    print(dict_from_csv)

    global after_work
    global before_bed
    after_work = random.choice(list(dict_from_csv.items()))
    before_bed = random.choice(list(dict_from_csv.values()))

    while after_work == before_bed:
        after_work = random.choice(list(dict_from_csv.values()))
    global csv_new_row
    csv_new_row = [after_work, before_bed, current_time]
    after_work = str(after_work)
    before_bed = str(before_bed)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


check_csv()
already_run()
random_select()
print("Current Time = " + current_time + " " + "\nAfter Work Activity = " + after_work)
print("Before Bed Activity = " + before_bed)
append_list_as_row('log.csv', csv_new_row)
sys.exit()
