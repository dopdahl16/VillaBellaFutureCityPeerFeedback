# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# import pandas lib as pd
import pandas as pd
 
# read by default 1st sheet of an excel file
dataframe1 = pd.read_excel('Peer Feedback Form - 5th Hour (Week 7).xlsx', sheet_name=1)
 
print(dataframe1)

for index, row in dataframe1.iterrows():
    dataframe1.at[index, 'Name'] = row[0].lower().strip()

student_scores = dict()

for index, row in dataframe1.iterrows():
    print(row[0], row[1], row[2], row[3], row[4], row[5])
    if row[0] in student_scores:
        new_average = []
        for category_idx in range(len(student_scores[row[0]])):
            avg = (student_scores[row[0]][category_idx] + row[category_idx + 1]) / 2.0
            new_average.append(avg)
        student_scores[row[0]] = new_average
    else:
        student_scores[row[0]] = [row[1], row[2], row[3], row[4], row[5]]

print(student_scores)

df = pd.DataFrame(student_scores)
df = df.transpose()
df.columns = ["Contributes to group discussions and group decisions", "Works hard and makes valuable contributions to the team", "Is kind, respectful, and cooperative", "Helps to keep the group on task", "Fulfills responsibilities "]
print(df)
df.to_csv('Anonymous Peer Feedback - 5th hour (Week 7).csv')