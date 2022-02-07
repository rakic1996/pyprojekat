'''
Created on 27.06.2019.

@author: Aleksandar Jankovic
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_racuna
from globalne_promenljive import racuniFajl,racuniPrazanFajl
from model import Racun
import vrednosti
from izgled.racun import pretraga_po_oznaci


class Test_pretraga_sekcije_po_oznaci(unittest.TestCase):


    def setUp(self):
        vrednosti.racuni=ucitavanje_racuna(racuniFajl)


    def tearDown(self):
        pass


    def test_pretraga_racuna_po_oznaci(self):
        racuni = pretraga_po_oznaci("Dejan Rakin")
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 0, "Lista mora biti prazna jer nije pronadjen nijedan racun")

    
    def test_pretraga_jedna_vrednost(self):
        racuni = pretraga_po_oznaci("R1")
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 1, "Lista mora imati 1 element")
        self.assertIsInstance(racuni[0], Racun, "Pronadjeni objekat mora biti tipa Racun")
        self.assertEqual(racuni[0].oznaka, "R1", "Pronadjen element mora imati oznaku R1")
    
    def test_pretraga_pogresna_oznaka(self):
        racuni =pretraga_po_oznaci("R666")
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 0, "Lista treba da bude prazna, jer nema racuna sa oznakom R666")

    
    def test_pretraga_po_oznaci_int(self):
        with self.assertRaises(TypeError):
            pretraga_po_oznaci(0)
            
class Test_pretraga_po_oznaci_PrazanFajl(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_racuna(racuniFajl)


    def tearDown(self):
        pass
    
    def test_pretraga_po_oznaci_prazan_fajl(self):
        racuni = pretraga_po_oznaci("R1")
        self.assertIsNotNone(racuni, "Vrednost racuna mora biti objekat koji je lista")
        self.assertIsInstance(racuni, list, "Vrednosti racuna mora biti lista")
        self.assertEqual(len(racuni), 0, "Nema ucitanih racuna i ne moze biti pronadjen nijedan objekat tipa Racun")


if __name__ == "__main__":
    unittest.main()