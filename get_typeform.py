#!/usr/bin/env python3

from configparser import ConfigParser

from requests import get

config = ConfigParser()
config.read('secrets.ini')

base_url = 'https://api.typeform.com/v0/form/' + config['TypeForm']['UID']
args = {'completed': 'true',
        'key': config['TypeForm']['key'],
        }

result = get(base_url, args)

data = result.json()

submit_dates = [d['metadata']['date_submit'] for d in data['responses']]
