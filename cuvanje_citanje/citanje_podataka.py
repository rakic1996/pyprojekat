'''
Modul koji sadrzi funkcije za ucitavanje 
sekcija, polica, artikala, stavki i racuna iz njihovih fajlova.

'''

from model import Sekcija,Polica,Artikal,Stavka,Racun
from vrednosti import sekcija_po_oznaci, police_po_oznaci,artikal_po_oznaci,racun_po_oznaci
import vrednosti
from cuvanje_citanje.putanje import sekcijaFajl, policeFajl, artikalFajl, stavkaFajl, racunFajl
from izgled.sekcija import prikaz_sekcija
import izgled
from os.path import exists

def ucitavanje_sekcija(sekcijaFajl):
    '''
    U ovoj metodi ucitavamo sve sekcije koristeci parametar sekcijeFajl, koji cuva
    putanju do fajla u kome se nalaze sekcije.
    
    :param sekcijaFajl: putanja do fajla iz kog se citaju sekcije
    
    :return: lista objekata tipa Sekcija ucitanih iz fajla
    
    :raise ValueError: ako sekcijaFajl nije prosledjen
    :raise TypeError: ako sekcijaFajl nije tipa string
    '''
    if sekcijaFajl is None:
        raise ValueError("Putanja mora biti string")
    if type(sekcijaFajl) is not str:
        raise TypeError("Putanja mora biti vrednost tipa string")
    checkFile(sekcijaFajl)
    sekcije=[]
    with open(sekcijaFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            naziv = fields[1]
            opis = fields[2]
            pozicija = fields[3]
            sekcije.append(Sekcija(oznaka,naziv,opis,pozicija))
    return sekcije

def ucitavanje_police(policeFajl):
    '''
    U ovoj metodi ucitavamo sve police koristeci parametar policeFajl, koji cuva
    putanju do fajla u kome se nalaze police.
    
    :param policeFajl: putanja do fajla iz kog se citaju police
    
    :return: lista objekata tipa Polica ucitanih iz fajla
    '''
    police=[]
    with open(policeFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            red= int(fields[1])
            kolona= int(fields[2])
            pozicija= int(fields[3])
            duzina = float(fields[4])
            sirina = float(fields[5])
            visina = float(fields[6])
            sekcija_oznaka=fields[7]
            sekcija=sekcija_po_oznaci(sekcija_oznaka)
            police.append(Polica(oznaka,red,kolona,pozicija,duzina,sirina,visina,sekcija))
    return police

def ucitavanje_artikala(artikalFajl):
    '''
    U ovoj metodi ucitavamo sve artikle koristeci parametar artikalFajl
    
    :param artikalFajl: putanja do fajla iz kog se citaju artikli
    
    :return: lista objekata tipa Artikal ucitanih iz fajla
    
    :raise ValueError: ako artikalFajl nije prosledjen
    :raise TypeError: ako artikalFajl nije tipa string
    '''
    
    artikli=[]
    with open(artikalFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            naziv = fields[1]
            opis = fields[2]
            cena = float(fields[3])
            rok_trajanja = fields[4]
            polica_oznaka = fields[5]
            polica = police_po_oznaci(polica_oznaka)
            artikli.append(Artikal(oznaka,naziv,opis,cena,rok_trajanja,polica))
    return artikli

def ucitavanje_stavki(stavkaFajl):
    '''
    U ovoj metodi ucitavamo sve stavke koristeci parametar stavkaFajl
    
    :param stavkaFajl: putanja do fajla iz kog se citaju stavke
    
    :return: lista objekata tipa Stavka ucitanih iz fajla
    
    :raise ValueError: ako stavkaFajl nije prosledjen
    :raise TypeError: ako stavkaFajl nije tipa string
    '''
    
    stavke=[]
    with open(stavkaFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            kolicina= int(fields[1])
            ukupna_cena= float(fields[2])
            racun_oznaka=fields[3]
            racun=racun_po_oznaci(racun_oznaka)
            artikal_oznaka=fields[4]
            artikal=artikal_po_oznaci(artikal_oznaka)
            stavke.append(Stavka(oznaka,kolicina,ukupna_cena,racun,artikal))
    return stavke


def ucitavanje_racuna(racunFajl):
    racuni=[]
    with open(racunFajl) as f:
        for line in f:
            fields = line.split("|")
            oznaka = fields[0]
            prodavac=(fields[1])
            ukupna_cena= float(fields[2])
            datum=fields[3]
            racuni.append(Racun(oznaka,prodavac,ukupna_cena, datum))
    return racuni



def prikaz_vrednosti(lista):
    for i,el in enumerate(lista):
        print("{} {}".format(i,el))
        
def checkFile(file):
    '''
    Proverava da li postoji fajl u fajl sistemu i ako ne postoji kreira novi.
    
    :param file: putanja do fajla koji se proverava da li postoji
    '''
    if not exists(file):
        open(file, 'w').close()
        
if __name__ == '__main__':
    pass
    