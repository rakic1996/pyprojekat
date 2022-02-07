'''
Created on 24.06.2019.

@author: Dejan
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_sekcija
from globalne_promenljive import sekcijaFajl,sekcijePrazanFajl
from model import Sekcija


class Testiranje_ucitavanja_sekcije(unittest.TestCase):
    
    def test_ucitati_vise_vrednosti(self):
        sekcije=ucitavanje_sekcija(sekcijaFajl)
        self.assertIsNotNone(sekcije, "Vrednost sekcija mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcija mora biti lista")
        self.assertEqual(len(sekcije), 6, "Lista mora imati 6 elementa")
        self.assertIsInstance(sekcije[0], Sekcija, "Ucitani objekti moraju biti tipa Sekcija")
        self.assertEqual(sekcije[0].oznaka, "S4", "Prvi ucitani element mora imati indeks S4")


    def test_ucitati_prazan(self):
        sekcije=ucitavanje_sekcija(sekcijePrazanFajl)
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 0, "Lista mora biti prazna, jer ucitavamo prazan fajl")
    
    def test_ucitati_none(self):
        with self.assertRaises(ValueError):
            ucitavanje_sekcija(None)
            
    def test_ucitati_int(self):
        with self.assertRaises(TypeError):
            ucitavanje_sekcija(1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()