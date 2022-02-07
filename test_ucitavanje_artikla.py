'''
Created on 27.06.2019.

@author: Nemanja
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_artikala
from globalne_promenljive import artikalFajl,ArtikliPrazanFajl
from model import Artikal


class Testiranje_ucitavanja_artikla(unittest.TestCase):
    
    def test_ucitati_vise_vrednosti(self):
        artikli=ucitavanje_artikala(artikalFajl)
        self.assertIsNotNone(artikli, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikli, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikli), 6, "Lista mora imati 6 elementa")
        self.assertIsInstance(artikli[0], Artikal, "Ucitani objekti moraju biti tipa Artikal")
        self.assertEqual(artikli[0].oznaka, "A3", "Prvi ucitani element mora imati indeks A3")


    def test_ucitati_prazan(self):
        artikli=ucitavanje_artikala(ArtikliPrazanFajl)
        self.assertIsNotNone(artikli, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikli, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikli), 0, "Lista mora biti prazna, jer ucitavamo prazan fajl")
    
    def test_ucitati_none(self):
        with self.assertRaises(ValueError):
            ucitavanje_artikala(None)
            
    def test_ucitati_int(self):
        with self.assertRaises(TypeError):
            ucitavanje_artikala(1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
