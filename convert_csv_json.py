import csv
import json

csvfile = open('exported.csv', 'r')
jsonfile = open('exported.json', 'w')

fieldnames = ("","Name","","Email")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')