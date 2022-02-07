'''
Modul koji sadrzi funkcije za upisivanje objekata tipa
Sekcija, Polica, Artikal, Stavka i Racun u njihove fajlove.

'''

from cuvanje_citanje.putanje import sekcijaFajl,policeFajl,artikalFajl,stavkaFajl,racunFajl

def cuvanje_sekcija(sekcije,sekcijaFajl):
    '''
    Metoda koja upisuje sve sekcije u fajl u unpared
       predvidjenom formatu
    
    :param sekcije: lista sekcija za upis u fajl
    :param sekcijaFajl: putanja do fajla u koji se upisuju sekcije
    '''
    with open(sekcijaFajl,"w") as f:
        for s in sekcije:
            f.write("{}|".format(s.oznaka))
            f.write("{}|".format(s.naziv))
            f.write("{}|".format(s.opis))
            f.write("{}|\n".format(s.pozicija))
            
def cuvanje_polica(police,policeFajl):
    '''
    Metoda koja upisuje sve police u fajl u unpared
       predvidjenom formatu
    
    :param police: lista polica za upis u fajl
    :param policeFajl: putanja do fajla u koji se upisuju police
    '''
    with open(policeFajl,"w") as f:
        for p in police:
            f.write("{}|".format(p.oznaka))
            f.write("{}|".format(p.red))
            f.write("{}|".format(p.kolona))
            f.write("{}|".format(p.pozicija))
            f.write("{}|".format(p.duzina))
            f.write("{}|".format(p.sirina))
            f.write("{}|".format(p.visina))
            f.write("{}|\n".format("None" if p.sekcija is None else p.sekcija.oznaka))
            
def cuvanje_artikala(artikli,artikalFajl):
    
    '''
    Metoda koja dodaje artikal u datoteku u definisanom formatu
    :param artikli: predstavljaju listu za upis u datoteku
    :param artikalFajl: to predstavjla fajl u koji se upisuju podaci o artiklu  
    '''
    with open(artikalFajl,"w") as f:
        for a in artikli:
            f.write("{}|".format(a.oznaka))
            f.write("{}|".format(a.naziv))
            f.write("{}|".format(a.opis))
            f.write("{}|".format(a.cena))
            f.write("{}|".format(a.rok_trajanja))
            f.write("{}|\n".format("None" if a.polica is None else a.polica.oznaka))

def cuvanje_stavki(stavke ,stavkaFajl):
    
    '''
    Metoda koja dodaje stavku u datoteku u definisanom formatu
    :param stavke: predstavljaju listu za upis u datoteku
    :param stavkaFajl: to predstavjla fajl u koji se upisuju podaci o stavci
    '''
    with open(stavkaFajl,"w") as f:
        for st in stavke:
            f.write("{}|".format(st.oznaka))
            f.write("{}|".format(st.kolicina))
            f.write("{}|".format(st.ukupna_cena))
            f.write("{}|".format("None" if st.racun is None else st.racun.oznaka))
            f.write("{}|\n".format("None" if st.artikal is None else st.artikal.oznaka))
 
def cuvanje_racuna(racuni ,racunFajl):
    with open(racunFajl,"w") as f:
        for r in racuni:
            f.write("{}|".format(r.oznaka))
            f.write("{}|".format(r.prodavac))
            f.write("{}|".format(r.ukupna_cena))
            f.write("{}|\n".format(r.datum))
            
            
if __name__ == '__main__':
    pass