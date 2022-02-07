'''
Created on 24.06.2019.

@author: Dejan
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_sekcija
from globalne_promenljive import sekcijaFajl,sekcijePrazanFajl
from model import Sekcija
import vrednosti
from izgled.sekcija import pretraga_po_oznaci


class Test_pretraga_sekcije_po_oznaci(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_sekcija(sekcijaFajl)


    def tearDown(self):
        pass


    def test_pretraga_sekcije_po_oznaci(self):
        sekcije=pretraga_po_oznaci("Odeca")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 0, "Lista mora biti prazna jer nije pronadjen nijedna sekcija")

    
    def test_pretraga_vise_vrednosti(self):
        sekcije=pretraga_po_oznaci("1")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 2, "Lista mora imati 2 elementa")
        self.assertIsInstance(sekcije[0], Sekcija, "Pronadjeni objekti moraju biti tipa Sekcija")
        self.assertEqual(sekcije[0].oznaka, "S13", "Prvi pronadjen element mora imati u oznaci tekst 1")
    
    def test_pretraga_jedna_vrednost(self):
        sekcije=pretraga_po_oznaci("S13")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 1, "Lista mora imati 1 element")
        self.assertIsInstance(sekcije[0], Sekcija, "Pronadjeni objekat mora biti tipa Sekcija")
        self.assertEqual(sekcije[0].oznaka, "S13", "Pronadjen element mora imati oznaku S13")
    
    def test_pretraga_pogresna_oznaka(self):
        sekcije=pretraga_po_oznaci("S0")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 0, "Lista treba da bude prazna, jer nema sekcije sa oznakom S0")

    def test_pretraga_obrnut_case(self):
        sekcije=pretraga_po_oznaci("s13")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 1, "Lista mora imati 1 element")
        self.assertIsInstance(sekcije[0], Sekcija, "Pronadjeni objekat mora biti tipa Sekcija")
        self.assertEqual(sekcije[0].oznaka, "S13", "Pronadjen element mora imati oznaka S13")

    
    def test_pretraga_po_oznaci_none(self):
        with self.assertRaises(ValueError):
            pretraga_po_oznaci(None)
    
    def test_pretraga_po_oznaci_int(self):
        with self.assertRaises(TypeError):
            pretraga_po_oznaci(1)
            
class Test_pretraga_po_oznaci_PrazanFajl(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_sekcija(sekcijePrazanFajl)


    def tearDown(self):
        pass
    
    def test_pretraga_po_oznaci_prazan_fajl(self):
        sekcije=pretraga_po_oznaci("S4")
        self.assertIsNotNone(sekcije, "Vrednost sekcije mora biti objekat koji je lista")
        self.assertIsInstance(sekcije, list, "Vrednosti sekcije mora biti lista")
        self.assertEqual(len(sekcije), 0, "Nema ucitanih sekcija i ne moze biti pronadjen nijedna Sekcija")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()