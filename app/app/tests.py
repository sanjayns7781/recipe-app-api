"""
Sample tests
"""
from django.test import SimpleTestCase

from . import calc


class CalcTests(SimpleTestCase):
    """Test the ccalc module"""

    def test_add_numbers(self):
        """Test adding numbers together"""
        res = calc.add(5,2)

        self.assertEqual(res,7)
    
    def test_sub_numbers(self):
        """Test substracting numbers"""
        res = calc.substract(15,5)

        self.assertEqual(res,10)