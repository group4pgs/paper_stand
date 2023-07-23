import json
import sys

dbf = open('db.json')
db = json.loads(dbf.read())

search_tag = sys.argv[1]
for i in db:
    if search_tag in i['tags']:
        print('Name -> ',i['name'])
        print('Path -> ',i['loc'])

dbf.close()
