#!/usr/bin/env python

'''Run with the name of the data file as the first (and only) argument
get filled templates'''

from string import Template, whitespace
from sys import argv
from csv import reader
from datetime import date

with open('template.html') as template_file:
    t = Template(template_file.read())

with open(argv[1]) as response_file:
    # Throw away the header
    next(response_file)

    for line in reader(response_file):
        line = [item.strip(',-./:' + whitespace) for item in line]

        # Date is a little complex
        curr_date, _ = line[22].split()
        parsed_date = date(*(int(x) for x in curr_date.split('-')))
        string_date = parsed_date.strftime('%B %-d, %Y')

        filled = t.substitute(time=line[2], service=line[1],
                              harm_reduction=line[4], footprint=line[5],
                              equanimity=line[7],
                              fearlessness=line[9],
                              stillness=line[11], practice=line[12],
                              personal=line[14],
                              name=line[16],
                              date=string_date)

        with open('{} {}.html'.format(line[16].strip(), line[22]), 'w') as outfile:
            outfile.write(filled)
