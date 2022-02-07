'''
Created on 27.06.2019.

@author: Nemanja
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_stavki
from globalne_promenljive import stavkaFajl,stavkePrazanFajl
from model import Stavka
import vrednosti
from izgled.stavka import pretraga_po_oznaci


class Test_pretraga_sekcije_po_oznaci(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_stavki(stavkaFajl)


    def tearDown(self):
        pass


    def test_pretraga_stavke_po_oznaci(self):
        stavka=pretraga_po_oznaci("3")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavke mora biti lista")
        self.assertEqual(len(stavka), 0, "Lista mora biti prazna jer nije pronadjen nijedna stavka")

    
    def test_pretraga_vise_vrednosti(self):
        stavka=pretraga_po_oznaci("2")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavke mora biti lista")
        self.assertEqual(len(stavka), 2, "Lista mora imati 2 elementa")
        self.assertIsInstance(stavka[0], Stavka, "Pronadjeni objekti moraju biti tipa Stavka")
        self.assertEqual(stavka[0].oznaka, "ST2", "Prvi pronadjen element mora imati u oznaci tekst 2")
    
    def test_pretraga_jedna_vrednost(self):
        stavka=pretraga_po_oznaci("ST2")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavke mora biti lista")
        self.assertEqual(len(stavka), 1, "Lista mora imati 1 element")
        self.assertIsInstance(stavka[0], Stavka, "Pronadjeni objekat mora biti tipa Stavka")
        self.assertEqual(stavka[0].oznaka, "ST2", "Pronadjen element mora imati oznaku ST2")
    
    def test_pretraga_pogresna_oznaka(self):
        stavka=pretraga_po_oznaci("ST0")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavke mora biti lista")
        self.assertEqual(len(stavka), 0, "Lista treba da bude prazna, jer nema stavke sa oznakom ST0")

    def test_pretraga_obrnut_case(self):
        stavka=pretraga_po_oznaci("st2")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavk mora biti lista")
        self.assertEqual(len(stavka), 1, "Lista mora imati 1 element")
        self.assertIsInstance(stavka[0], Stavka, "Pronadjeni objekat mora biti tipa Stavka")
        self.assertEqual(stavka[0].oznaka, "ST2", "Pronadjen element mora imati oznaka ST2")

    
    def test_pretraga_po_oznaci_none(self):
        with self.assertRaises(ValueError):
            pretraga_po_oznaci(None)
    
    def test_pretraga_po_oznaci_int(self):
        with self.assertRaises(TypeError):
            pretraga_po_oznaci(1)
            
class Test_pretraga_po_oznaci_PrazanFajl(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_stavki(stavkePrazanFajl)


    def tearDown(self):
        pass
    
    def test_pretraga_po_oznaci_prazan_fajl(self):
        stavka=pretraga_po_oznaci("ST2")
        self.assertIsNotNone(stavka, "Vrednost stavke mora biti objekat koji je lista")
        self.assertIsInstance(stavka, list, "Vrednosti stavke mora biti lista")
        self.assertEqual(len(stavka), 0, "Nema ucitanih stavki i ne moze biti pronadjen nijedna Stavka")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()