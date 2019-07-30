CSV_URL = 'https://raw.githubusercontent.com/turingschool/backend-curriculum-site/gh-pages/module4/projects/take_home_challenge/prompts/olympic_data_2016.csv'

import requests

res = requests.get(CSV_URL)

raw_data = res.text
from io import StringIO

import csv
import json
from os.path import dirname, abspath, join
from pprint import pprint as pp

CURR_DIR = dirname(abspath(__file__))

# Open the CSV
csvfile = StringIO(raw_data)
jsonfile = open(join(CURR_DIR, 'seed_db.json'), 'w')

fieldnames = ("name", "sex", "age", "height", "weight",
    "team", "games", "sport", "event", "medal"
)

reader = csv.DictReader(csvfile, fieldnames)
# breakpoint()

app_table = 'api.olympian'
pk = 1
data = []
for idx, row in enumerate(reader):
    if idx == 0:
        continue
    row = { k:(v if v != "NA" else None) for k,v in dict(row).items() }
    fixture = {
        "model": app_table,
        "pk": pk,
        "fields": row
    }
    data.append(fixture)
    pk += 1

json.dump(data, fp=jsonfile, indent=4)
