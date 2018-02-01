import csv

with open('rep.csv', mode='r') as infile:
    reader = csv.DictReader(infile)
    with open('coors_new.csv', mode='w') as outfile:
        writer = csv.writer(outfile)
        dict_list = []
        for line in reader:
            dict_list.append(line)

def getKey(key):
    for element in dict_list:
        element.get(key)
populaire = []
moyen = []
privilege = []

def separate_in_class():

    for element in dict_list:
        classe = int(element.get("classe"))
        if(classe==-1):
            populaire.append(element)
        if(classe==0):
            moyen.append(element)
        if(classe==1):
            privilege.append(element)

separate_in_class()

def taux_sport(dic):
    total = len(dic)
    for elemnt in dic:



print()
