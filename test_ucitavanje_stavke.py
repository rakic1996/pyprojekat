'''
Created on 27.06.2019.

@author: Nemanja
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_stavki
from globalne_promenljive import stavkaFajl,stavkePrazanFajl
from model import Stavka


class Testiranje_ucitavanja_stavki(unittest.TestCase):
    
    def test_ucitati_vise_vrednosti(self):
        stavka=ucitavanje_stavki(stavkaFajl)
        self.assertIsNotNone(stavka, "Vrednost stavki mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavki mora biti lista")
        self.assertEqual(len(stavka), 2, "Lista mora imati 2 elementa")
        self.assertIsInstance(stavka[0], Stavka, "Ucitani objekti moraju biti tipa Stavka")
        self.assertEqual(stavka[0].oznaka, "ST1", "Prvi ucitani element mora imati indeks ST1")


    def test_ucitati_prazan(self):
        stavka=ucitavanje_stavki(stavkePrazanFajl)
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavki mora biti lista")
        self.assertEqual(len(stavka), 0, "Lista mora biti prazna, jer ucitavamo prazan fajl")
    
    def test_ucitati_none(self):
        with self.assertRaises(ValueError):
            ucitavanje_stavki(None)
            
    def test_ucitati_int(self):
        with self.assertRaises(TypeError):
            ucitavanje_stavki(1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
