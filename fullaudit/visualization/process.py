# trim any csv headers 
import csv
import json

results = {}

def clean_string(orig):
    return orig.lower().lstrip().rstrip()

with open('August28.csv', 'rb') as csvfile:
    data = csv.reader(csvfile)
    for row in data:
        for item in [3, 4]:
            if not bool(clean_string(row[item])):
                row[item] = 'unknown'
            else:
                row[item] = clean_string(row[item])
        if row[4] in results:
            if not bool(clean_string(row[2])):
                continue
            if row[3] in results[row[4]]:
                results[row[4]][row[3]] += float(row[2])
            else:
                results[row[4]][row[3]] = float(row[2])
        else:
            results[row[4]] = {}
            results[row[4]][row[3]] = float(row[2])

formatted_results = []
for key, value in results.iteritems():
    formatted_children = []
    for name, amount in value.iteritems():
        formatted_children.append({ 'name': name, 'size': amount })
    formatted_results.append({'name': key, 'children': formatted_children})

with open('output.json', 'w') as output:
    output.write(json.dumps({'name': 'cpd', 'children': formatted_results}, sort_keys=True, indent=4) + '\n')
