#!/usr/bin/env python

'''Run with the name of the data file as the first (and only) argument
get filled templates'''

from string import Template, whitespace
from sys import argv
# from csv import reader
from datetime import date
import json

# Set up things that are standard across responses
with open('template.html') as template_file:
    t = Template(template_file.read())

field_map = {'textfield_18665036': 'name',
             'textfield_18665039': 'service',
             'textarea_18665044': 'time',
             'list_18665042_choice': 'harm_reduction',
             'textarea_18665045': 'footprint',
             'textarea_18665046': 'equanimity',
             'textarea_18665047': 'fearlessness',
             'textfield_18665040': 'stillness',
             'textarea_18665048': 'practice',
             'textarea_18665049': 'personal',
             }

# To keep track of types
old_field_map = {'textfield_14892155': 'service',
                 'textarea_14892160': 'time',
                 'list_14892158_choice': 'harm_reduction',
                 'textarea_14892161': 'footprint',
                 'textarea_14892162': 'equanimity',
                 'textarea_14892163': 'fearlessness',
                 'textfield_14892156': 'stillness',
                 'textarea_14892164': 'practice',
                 'textarea_14892165': 'personal',
                 'textfield_14892152': 'name',
                 }


# Process our responses

with open(argv[1]) as response_file:
    data = json.load(response_file)

for i, d in enumerate(data['responses']):
    # Date is a little complex
    curr_date, _ = d['metadata']['date_submit'].split()
    parsed_date = date(*(int(x) for x in curr_date.split('-')))
    string_date = parsed_date.strftime('%B %-d, %Y')

    answers = d['answers']
    try:
        mapped_fields = {v: answers[k].strip(',-./:' + whitespace)
                         for k, v in field_map.items()}
    except KeyError:
        print('***Problem with record {}:\n{}'.format(i, answers))

    filled = t.substitute(date=string_date, **mapped_fields)

    ofname = 'html_forms/{} {}.html'.format(mapped_fields['name'], curr_date)
    with open(ofname, 'w') as outfile:
        outfile.write(filled)
