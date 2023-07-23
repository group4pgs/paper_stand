import json
import sys
import os
import getopt


def search_by_tags(tags):
    dbf = open('db.json')
    db = json.loads(dbf.read())

    search_tag = tags
    for i in db:
        if search_tag in i['tags']:
            print('Name \t\t-> ',i['name'])
            print('Path \t\t-> ',i['loc'])
            print('Other tags\t -> ',i['tags'])

    dbf.close()




if __name__=='__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:s:n:u:t:a", ["help","search","name","doi","tags","add"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    #print(opts)

    #print("Using option %s"%args[0][0])
    tags=[]
    for o,a in opts:
        if o in ('-t','--tags'):
            tags = a

    for o,a in opts:
        if o in ('--search','-s'):
            search_by_tags(tags)
        if o in ('--help','-h'):
            usage()


def usage():
    print('Instruction to use')
