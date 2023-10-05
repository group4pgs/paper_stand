#!/usr/bin/env python
import json
import sys
import os
import getopt


def search_by_tags(tags):
    dbf = open('db.json','r+')
    db = json.loads(dbf.read())

    search_tag = tags
    for i in db:
        if set(search_tag).issubset(i['tags']):

            print('Name \t\t-> ',i['name'])
            print('Path \t\t-> ',i['loc'])
            print('Other tags\t -> ',i['tags'])
            print()

    dbf.close()

def change_tags():
    tag_doi = input("Paste the DOI -> ")
    new_tags = []
    dbf = open('db.json','r')
    db = json.load(dbf)
    dbf.close()
    updated_db = []
    for i in db:
        tags = i['tags']
        if i["doi"] == tag_doi:
            print("Paper found!")
            print("Current tags are -> ",i['tags'])
            tags = input("Enter new tags -> ").split(',')
        updated_db.append({"name":i['name'],"doi":i['doi'],"loc":i['loc'],"tags":tags})

    with open('db.json','w') as db_file:
        json.dump(updated_db,db_file)

    return True



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
    print('This tool allows you to manage your collection of papers or documents in the PC\n*****************\n')
    print('The following are the arguments that are needed for the tool to be used')
    print('\n--search or -s: is compulsory if we want to search of the papers')
    print('--add or -a: is used to add a document to the collection. It will prompt you the inputs where in you need to enter the details, after which the paper will be stored successfully')
    print('--change or -c: is used to change the tags of an existing paper in the database. It will prompt you the inputs but keep the DOI handy')
    


if __name__=='__main__':

    try:
        opts, args = getopt.getopt(sys.argv[1:], "h:s:u:t:a:c", ["help","search","doi","tags","add","change"])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    #print(opts)

    #print("Using option %s"%args[0][0])
    tags=[]
    for o,a in opts:
        if o in ('-t','--tags'):
            tags = a.split(',')


    for o,a in opts:
        if o in ('--search','-s'):
            search_by_tags(tags)
        if o in ('--help','-h'):
            usage()
        if o in ('--change','-c'):
            if change_tags():
                print("Tags changed!")
        if o in ('--add','-a'):
            if add_paper():
                print("Paper successfully added!")
            else:
                print("ERROR: Problem adding the paper, Please try again or check the 'db.json' file!")
    print("\n")




