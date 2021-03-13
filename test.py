from datetime import datetime

import pandas as pd

string = "STRING"
current_date = datetime.now()
string_current_date = current_date.strftime("%Y-%m-%d")
print(string_current_date)

df2 = pd.read_csv('log.csv', header=None, squeeze=True)

if [df2[2] == string_current_date]:
    print("Present")
    out = df2[2].isin([string_current_date])
    filtered_df2 = df2[out]
    print(filtered_df2)

    # print([df2[1] == string_current_date])

else:
    print("Not Present")

# boolean_findings = df2[0].str.contains(string)

# print(boolean_findings)
