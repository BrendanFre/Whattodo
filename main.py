import csv
import os
import sys
from _csv import writer
from datetime import datetime

import numpy as np
import pandas as pd

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


current_date = datetime.now().date()
string_current_date = current_date.strftime("%Y-%m-%d")


def already_run():
    df2 = pd.read_csv('log.csv', header=None, squeeze=True)
    df2.columns = ["Afternoon", "Evening", "Date"]
    if string_current_date in df2.values:
        # [df2[2] == string_current_date]:
        print("Present")
        out = df2['Date'].isin([string_current_date])
        filtered_df2 = df2[out]
        print(filtered_df2)
        sys.exit()


def random_select():
    global after_work
    global before_bed
    # after_work = random.choice(list(dict_from_csv.items()))
    # before_bed = random.choice(list(dict_from_csv.values()))

    # Needs to be fixed
    df = pd.read_csv('activities.csv', header=0, squeeze=True)
    after_work = df['Afternoon'].iloc[np.random.randint(len(df))]
    before_bed = df['Afternoon'].iloc[np.random.randint(len(df))]

    print(after_work + before_bed)

    while after_work == before_bed:
        after_work = df[0].iloc[np.random.randint(len(df))]
    global csv_new_row
    csv_new_row = [after_work, before_bed, current_date]
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
print("Current Time = " + string_current_date + " " + "\nAfter Work Activity = " + after_work)
print("Before Bed Activity = " + before_bed)
append_list_as_row('log.csv', csv_new_row)
sys.exit()
