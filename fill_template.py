#!/usr/bin/env python

'''Run with the name of the data file as the first (and only) argument
get filled templates'''

from string import Template, whitespace
from sys import argv, exit

import pandas as pd

# Set up things that are standard across responses
with open('template.html') as template_file:
    t = Template(template_file.read())

# Process our responses

try:
    data = pd.read_excel(argv[1])
except:
    print('Please specify the excel filename as the first (and only) argument')
    exit(1)

# We treat name separately, as there is no way to make that work with
# case-insensitive matching
field_keywords = ['service', 'specify', 'harm', # reduction!
        'footprint', 'equanimity', 'fearlessness', 'stillness',
        'extra', 'own', 'submit']

def match_col(df, keyword):
    '''Extract exactly one column matching the keyword (case-insensitive) or sys.exit(1)'''
    pattern = '(?i){}'.format(keyword)
    cols = data.columns.str.contains(pattern)
    # These will be True/False ~ 1/0
    num_cols = cols.sum()
    if num_cols != 1:
        print('Found {} cols for keyword {}!'.format(num_cols, keyword))
        # exit(1)

    # Now we can do this slightly ugly unpacking
    return data.columns[cols][0]

matched_fields = ['Name']
matched_fields.extend(match_col(data, field) for field in field_keywords)

# Copy is less efficient, but I don't care and then we don't get warnings about
# modifying a copy
clean_data = data[matched_fields].copy()
# NB! Pandas also has a 'name' attribute on it's Series. So don't use dot-notation
clean_data.columns = ['name'] + field_keywords
# Sometimes people use punctuation. If they add some other mark, I'll leave it
clean_data.replace('\s*\.\s*$', '', regex=True, inplace=True)

# Since we're already using pandas, we use their date parsing functionality
clean_data.submit = pd.to_datetime(clean_data.submit).dt.date

for _, row in clean_data.iterrows():
    filled = t.substitute(**row)

    ofname = 'html_forms/{} {}.html'.format(row['name'], row['submit'])
    with open(ofname, 'w') as outfile:
        outfile.write(filled)
