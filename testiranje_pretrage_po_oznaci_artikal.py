'''
Created on 27.06.2019.

@author: Nemanja
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_artikala
from globalne_promenljive import artikalFajl,ArtikliPrazanFajl
from model import Artikal
import vrednosti
from izgled.artikal import pretraga_po_oznaci


class Test_pretraga_sekcije_po_oznaci(unittest.TestCase):


    def setUp(self):
        vrednosti.sekcije=ucitavanje_artikala(artikalFajl)


    def tearDown(self):
        pass


    def test_pretraga_artikla_po_oznaci(self):
        artikal=pretraga_po_oznaci("pavlaka")
        self.assertIsNotNone(artikal, "Vrednost artikla mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikla mora biti lista")
        self.assertEqual(len(artikal), 0, "Lista mora biti prazna jer nije pronadjen nijedan artikal")

    
    def test_pretraga_vise_vrednosti(self):
        artikal=pretraga_po_oznaci("Sir")
        self.assertIsNotNone(artikal, "Vrednost artikla mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikal), 2, "Lista mora imati 2 elementa")
        self.assertIsInstance(artikal[0], Artikal, "Pronadjeni objekti moraju biti tipa Artikal")
        self.assertEqual(artikal[0].oznaka, "A1", "Prvi pronadjen element mora imati u oznaci tekst Sir")
    
    def test_pretraga_jedna_vrednost(self):
        artikal=pretraga_po_oznaci("A1")
        self.assertIsNotNone(artikal, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikal), 1, "Lista mora imati 1 element")
        self.assertIsInstance(artikal[0], Artikal, "Pronadjeni objekat mora biti tipa Artikal")
        self.assertEqual(artikal[0].oznaka, "A1", "Pronadjen element mora imati oznaku A1")
    
    def test_pretraga_pogresna_oznaka(self):
        artikal=pretraga_po_oznaci("A22")
        self.assertIsNotNone(artikal, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikal), 0, "Lista treba da bude prazna, jer nema artikla sa oznakom A22")

    def test_pretraga_obrnut_case(self):
        artikal=pretraga_po_oznaci("a1")
        self.assertIsNotNone(artikal, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikal), 1, "Lista mora imati 1 element")
        self.assertIsInstance(artikal[0], Artikal, "Pronadjeni objekat mora biti tipa Artikal")
        self.assertEqual(artikal[0].oznaka, "A1", "Pronadjen element mora imati oznaka A1")

    
    def test_pretraga_po_oznaci_none(self):
        with self.assertRaises(ValueError):
            pretraga_po_oznaci(None)
    
    def test_pretraga_po_oznaci_int(self):
        with self.assertRaises(TypeError):
            pretraga_po_oznaci(1)
            
class Test_pretraga_po_oznaci_PrazanFajl(unittest.TestCase):


    def setUp(self):
        vrednosti.artikli=ucitavanje_artikala(ArtikliPrazanFajl)


    def tearDown(self):
        pass
    
    def test_pretraga_po_oznaci_prazan_fajl(self):
        artikal=pretraga_po_oznaci("A4")
        self.assertIsNotNone(artikal, "Vrednost artikala mora biti objekat koji je lista")
        self.assertIsInstance(artikal, list, "Vrednosti artikala mora biti lista")
        self.assertEqual(len(artikal), 0, "Nema ucitanih artikala i ne moze biti pronadjen nijedan Artikal")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()