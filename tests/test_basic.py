# coding=utf-8
import unittest
from companycase import CompanyCase

class TestEnglishCCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.ccase = CompanyCase()

    def test_simple(self):
        self.assertEqual(self.ccase.apply("foobar ltd"), "Foobar LTD")
        self.assertEqual(self.ccase.apply("hsbc bank (uk) ltd"), "HSBC Bank (UK) LTD")
        self.assertEqual(self.ccase.apply("AXA INSURANCE"), "AXA Insurance")

    def test_abbreviations(self):
        s = 'ltd plc llc and of'
        expected = 'LTD PLC LLC and of'
        self.assertEqual(self.ccase.apply(s, 0.0), expected)
        self.assertEqual(self.ccase.apply(s, 1.0), expected)

    def test_threshold(self):
        s = 'hello there nk'
        self.assertEqual(self.ccase.apply(s), "Hello There NK")
        self.assertEqual(self.ccase.apply(s, 0.0), "Hello There Nk")
        self.assertEqual(self.ccase.apply(s, 1.0), "HELLO THERE NK")

    def test_force_case(self):
        self.ccase.force_case_for_words(['fOO', 'bAr'])
        s = 'foo bar limited plc ltd'
        self.assertEqual(self.ccase.apply(s), "fOO bAr Limited PLC LTD")
        self.assertEqual(self.ccase.apply(s, 0.0), "fOO bAr Limited PLC LTD")
        self.assertEqual(self.ccase.apply(s, 1.0), "fOO bAr LIMITED PLC LTD")

    def test_unicode(self):
        self.assertEqual(self.ccase.apply(u"foobar ltd"), "Foobar LTD")
        self.assertEqual(self.ccase.apply(u"hsbc bank (uk) ltd"), "HSBC Bank (UK) LTD")
        self.assertEqual(self.ccase.apply(u"AXA INSURANCE"), "AXA Insurance")

        self.assertEqual(self.ccase.apply(u"tromsø, arctic explorers plc"), u'Tromsø, Arctic Explorers PLC')
        self.assertEqual(self.ccase.apply(u"tromsø, arctic explorers plc", 1.0), u'TROMSØ, ARCTIC EXPLORERS PLC')


if __name__ == '__main__':
    unittest.main()

