import csv
import os
import sys
import re



def pobrisi_dolar(sez):
    novisez = []
    for i in sez:
        if i == '$':
            pass
        elif i[0] == '$':
            novisez += [i[1:]]
        else:
            novisez += [i]
    return novisez


def naredi_seznam(ime_dat, leto, st):
    seznam = []
    with open(ime_dat) as dat:
        for vrstica in dat:
            if leto > 2008:
                sez = pobrisi_dolar(vrstica.split()[1:])
            else:
                sez = pobrisi_dolar(vrstica.split()[1:(-st)])
            if len(sez) >= 2:
                sez = [' '.join(sez[:(-1)]), sez[-1]]
                sez[1] = ''.join(sez[1].split(','))
                seznam += [sez]
    return seznam


GDP_na_prebivalca, GDP_rast, populacija, rast_populacije = {}, {}, {}, {}

def slovar_gdp_preb():
    for leto in range(2006, 2016):
        ime_dat = 'GDP_naprebivalca' + str(leto) + '.txt'
        for podsez in naredi_seznam(ime_dat, leto, 2):
            if podsez[0] in GDP_na_prebivalca.keys():
                GDP_na_prebivalca[podsez[0]][leto] = float(podsez[1])
            else:
                GDP_na_prebivalca[podsez[0]]= {'drzava': podsez[0]}
                GDP_na_prebivalca[podsez[0]][leto] = float(podsez[1])

def slovar_gdp_rast():
    for leto in range(2006, 2016):
        ime_dat = 'GDP_rast' + str(leto) + '.txt'
        for podsez in naredi_seznam(ime_dat, leto, 2):
            if podsez[0] in GDP_rast.keys():
                GDP_rast[podsez[0]][leto] = float(podsez[1])
            else:
                GDP_rast[podsez[0]]= {'drzava': podsez[0]}
                GDP_rast[podsez[0]][leto] = float(podsez[1])


def slovar_rast_populacije():
    for leto in range(2008, 2016):
        ime_dat = 'RastPopulacije' + str(leto) + '.txt'
        for podsez in naredi_seznam(ime_dat, leto, 2):
            if podsez[0] in rast_populacije.keys():
                rast_populacije[podsez[0]][leto] = float(podsez[1])
            else:
                rast_populacije[podsez[0]]= {'drzava': podsez[0]}
                rast_populacije[podsez[0]][leto] = float(podsez[1])

def zapisi_csv(ime, slovar):
    with open(ime, 'w') as csv_dat:
        polja = ['drzava'] + list(range(2006, 2016))
        writer = csv.DictWriter(csv_dat, fieldnames=polja, extrasaction='ignore')
        writer.writeheader()
        for item in slovar.values():
            writer.writerow(item)
    
slovar_gdp_preb()
slovar_gdp_rast()
slovar_rast_populacije()


zapisi_csv('GDP_na_prebivalca.csv', GDP_na_prebivalca)
zapisi_csv('GDP_rast.csv', GDP_rast)
zapisi_csv('rast_populacije.csv', rast_populacije)


            
                        
                    
