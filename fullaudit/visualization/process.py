# trim any csv headers 
import csv
import json
import pdb

results = {}

def clean_string(orig):
    return orig.lower().lstrip().rstrip()

with open('1505Export.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        for item in [1, 3]:
            if not bool(clean_string(row[item])):
                row[item] = 'unknown'
            else:
                row[item] = clean_string(row[item])
        if row[3] in results:
            if not bool(clean_string(row[2])):
                continue
            if row[2] in results[row[3]]:
                results[row[3]][row[2]] += float(row[1])
            else:
                results[row[3]][row[2]] = float(row[1])
        else:
            results[row[3]] = {}
            results[row[3]][row[2]] = float(row[1])

formatted_results = []
for key, value in results.iteritems():
    formatted_children = []
    for name, amount in value.iteritems():
        formatted_children.append({ 'name': name, 'size': amount })
    formatted_results.append({'name': key, 'children': formatted_children})

with open('output.json', 'w') as output:
    output.write(json.dumps({'name': 'cpd', 'children': formatted_results}, sort_keys=True, indent=4) + '\n')
