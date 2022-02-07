'''
Created on 27.06.2019.

@author: Aleksandar Jankovic
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_racuna
from globalne_promenljive import racuniFajl,racuniPrazanFajl
from model import Racun


class Testiranje_ucitavanja_sekcije(unittest.TestCase):
    
    def test_ucitati_vise_vrednosti(self):
        racuni = ucitavanje_racuna(racuniFajl)
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 5, "Lista mora imati 6 elementa")
        self.assertIsInstance(racuni[0], Racun, "Ucitani objekti moraju biti tipa Sekcija")
        self.assertEqual(racuni[0].oznaka, "R1", "Prvi ucitani element mora imati indeks R1")


    def test_ucitati_prazan(self):
        racuni = ucitavanje_racuna(racuniPrazanFajl)
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 0, "Lista mora biti prazna, jer ucitavamo prazan fajl")
    
    def test_ucitati_none(self):
        with self.assertRaises(TypeError):
            ucitavanje_racuna(None)
            
            
    def test_ucitati_int(self):
        with self.assertRaises(BaseException):
            ucitavanje_racuna(666)


if __name__ == "__main__":
    unittest.main()