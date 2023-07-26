import json
import sys
import os
import getopt


def search_by_tags(tags):
    dbf = open('db.json','r+')
    db = json.loads(dbf.read())

    search_tag = tags
    for i in db:
        if search_tag in i['tags']:
            print('Name \t\t-> ',i['name'])
            print('Path \t\t-> ',i['loc'])
            print('Other tags\t -> ',i['tags'])

    dbf.close()

def add_paper():
    paper_name = input("Name \t->")
    paper_doi = input("DOI \t->")
    paper_loc = input("Path \t->")
    paper_tags = input("Tags \t->").split(',')

    db = ""
    with open('db.json','r') as db_file:
        db = json.load(db_file)
        #print (db)

    new_entry = {"name":paper_name,"doi":paper_doi,"loc":paper_loc,"tags":paper_tags}

    db.append(new_entry)

    with open('db.json','w') as db_file:
        json.dump(db,db_file)


    return True


def usage():
    print('Instruction to use')
    


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
        if o in ('--add','-a'):
            if add_paper():
                print("Paper successfully added!")
            else:
                print("ERROR: Problem adding the paper, Please try again or check the 'db.json' file!")


