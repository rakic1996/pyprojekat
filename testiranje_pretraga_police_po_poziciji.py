'''
Created on 24.06.2019.

@author: Dejan
'''
import unittest
from cuvanje_citanje.citanje_podataka import ucitavanje_police
from globalne_promenljive import policeFajl,policePrazanFajl
import vrednosti
from izgled.police import pretraga_po_poziciji
from model import Polica 


class Test_pretraga_polica_po_poziciji(unittest.TestCase):


    def setUp(self):
        vrednosti.police=ucitavanje_police(policeFajl)


    def tearDown(self):
        pass


    def test_pretraga_sekcije_po_oznaci(self):
        police=pretraga_po_poziciji(7)
        self.assertIsNotNone(police, "Vrednost police mora biti objekat koji je lista")
        self.assertIsInstance(police, list, "Vrednosti police mora biti lista")
        self.assertEqual(len(police), 1, "Lista mora imati 1 element")
        self.assertIsInstance(police[0], Polica, "Pronadjeni objekat mora biti tipa Polica")
        self.assertEqual(police[0].pozicija, 7, "Pronadjen element mora imati poziciju 7")


    def test_pretraga_po_poziciji_none(self):
        with self.assertRaises(ValueError):
            pretraga_po_poziciji(None)
            
    def test_pretraga_po_poziciji_str(self):
        with self.assertRaises(TypeError):
            pretraga_po_poziciji("7")
            
    def test_pretraga_po_poziciji_nije_pronadjena(self):
        police=pretraga_po_poziciji(3)
        self.assertIsNotNone(police, "Vrednost police mora biti objekat koji je lista")
        self.assertIsInstance(police, list, "Vrednosti police mora biti lista")
        self.assertEqual(len(police), 0, "Lista mora biti prazna jer nije pronadjen nijedna polica sa zadatom pozocijom")

class Test_pretraga_po_poziciji_PrazanFajl(unittest.TestCase):


    def setUp(self):
        vrednosti.police=ucitavanje_police(policePrazanFajl)


    def tearDown(self):
        pass
    
    def test_pretraga_po_oznaci_prazan_fajl(self):
        police=pretraga_po_poziciji(7)
        self.assertIsNotNone(police, "Vrednost police mora biti objekat koji je lista")
        self.assertIsInstance(police, list, "Vrednosti police mora biti lista")
        self.assertEqual(len(police), 0, "Nema ucitanih polica i ne moze biti pronadjen nijedna polica")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()