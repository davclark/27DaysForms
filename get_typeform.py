#!/usr/bin/env python3

from configparser import ConfigParser

from requests import get

# Set up and performa the request

config = ConfigParser()
config.read('secrets.ini')

base_url = 'https://api.typeform.com/v1/form/' + config['TypeForm']['UID']
args = {'completed': 'true',
        'key': config['TypeForm']['key'],
        }

result = get(base_url, args)

with open('responses/0.json', 'w') as outfile:
    outfile.write(result.text)

# data = result.json()

# submit_dates = [d['metadata']['date_submit'] for d in data['responses']]
