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


field_map = {'textfield_11217477': 'service',
             'textarea_11217482': 'time',
             'list_11217480_choice': 'harm_reduction',
             'textarea_11217483': 'footprint',
             'textarea_11217484': 'equanimity',
             'textarea_11217485': 'fearlessness',
             'textfield_11217478': 'stillness',
             'textarea_11217486': 'practice',
             'textarea_11217487': 'personal',
             'textfield_11217474': 'name',
             }

# Process our responses

with open(argv[1]) as response_file:
    data = json.load(response_file)

for d in data['responses']:
    # Date is a little complex
    curr_date, _ = d['metadata']['date_submit'].split()
    parsed_date = date(*(int(x) for x in curr_date.split('-')))
    string_date = parsed_date.strftime('%B %-d, %Y')

    answers = d['answers']
    mapped_fields = {v: answers[k].strip(',-./:' + whitespace)
                     for k, v in field_map.items()}

    filled = t.substitute(date=string_date, **mapped_fields)

    ofname = 'html_forms/{} {}.html'.format(mapped_fields['name'], curr_date)
    with open(ofname, 'w') as outfile:
        outfile.write(filled)
