import csv
import os
import sys
from _csv import writer
from datetime import datetime

import PySimpleGUI as sg
import numpy as np
import pandas as pd

global after_work
global before_bed
global csv_new_row
global df
global window
global layout


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


def already_run():
    global df
    df = pd.read_csv('log.csv', header=None, squeeze=True)
    df.columns = ["Afternoon", "Evening", "Date"]
    if string_current_date in df.values:
        out = df['Date'].isin([string_current_date])
        df = df[out]
        interface()
    else:
        random_select()


def today():
    global df
    global df
    df = pd.read_csv('log.csv', header=None, squeeze=True)
    df.columns = ["Afternoon", "Evening", "Date"]
    out = df['Date'].isin([string_current_date])
    df = df[out]
    window.close()
    interface()


def random_select():
    global after_work
    global before_bed
    global df

    # Needs to be fixed
    df = pd.read_csv('activities.csv', header=0, squeeze=True)
    after_work = df['Afternoon'].iloc[np.random.randint(len(df))]
    before_bed = df['Afternoon'].iloc[np.random.randint(len(df))]

    while after_work == before_bed:
        after_work = df['Afternoon'].iloc[np.random.randint(len(df))]
    global csv_new_row
    csv_new_row = [after_work, before_bed, current_date]
    after_work = str(after_work)
    before_bed = str(before_bed)
    append_list_as_row('log.csv', csv_new_row)
    df = {'Afternoon': [after_work], 'Evening': [before_bed], 'Date': [string_current_date]}
    interface()


def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


def pivot_table():
    global df
    global layout
    df = pd.read_csv('log.csv')
    df['Count'] = 1
    df.columns = ['Afternoon', 'Evening', 'Date', 'Count']
    pivot_table1 = pd.pivot_table(df, index=['Afternoon'], values=['Count'], aggfunc=[np.sum], margins=True)
    pivot_table2 = pd.pivot_table(df, index=['Evening'], values=['Count'], aggfunc=[np.sum], margins=True)
    window.Element('_TEXT_').Update(pivot_table1)
    window.close()
    interface()


def interface():
    global layout
    sg.theme('DarkAmber')  # Add a touch of color
    # All the stuff inside your window.
    layout = [[sg.Text(string_current_date)],
              [sg.Text(df, key='_TEXT_')],
              [sg.Button('Close'), sg.Button('Log'), sg.Button('Pivot'), sg.Button('Today')]
              ]
    global window
    window = sg.Window('What Can I Do Today?', layout)

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Close':  # if user closes window or clicks cancel
            window.close()
            sys.exit()
        elif event == 'Log':
            log()
        elif event == 'Pivot':
            pivot_table()
        elif event == 'Today':
            today()


def log():
    global df
    df = pd.read_csv('log.csv')
    df = df.head()
    window.Element('_TEXT_').Update(df)
    window.close()
    interface()


current_date = datetime.now().date()
string_current_date = current_date.strftime("%Y-%m-%d")

check_csv()
already_run()
interface()
random_select()

sys.exit()
