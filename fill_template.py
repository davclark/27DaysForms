#!/usr/bin/env python

'''Run with the name of the data file as the first (and only) argument
get filled templates'''

from string import Template
from sys import argv
from csv import reader

with open('template.html') as template_file:
    t = Template(template_file.read())

with open(argv[1]) as response_file:
    # Throw away the header
    next(response_file)

    for line in reader(response_file):
        filled = t.substitute(time=line[2], service=line[1],
                              harm_reduction=line[4], footprint=line[5],
                              equanimity=line[7],
                              fearlessness=line[9],
                              stillness=line[11], practice=line[12],
                              personal=line[14])

        with open(line[16].strip() + '.html', 'w') as outfile:
            outfile.write(filled)
