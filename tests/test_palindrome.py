import unittest
from src.palindrome import is_palindrome

class TestPalindrome(unittest.TestCase):
    def test_simple_palindromes(self):
        self.assertTrue(is_palindrome("reconocer"))
        self.assertTrue(is_palindrome("anilina"))
        self.assertTrue(is_palindrome("salas"))

    
def test_phrase_palindromes(self):
    self.assertTrue(is_palindrome("Anita lava la tina"))
    self.assertTrue(is_palindrome("La ruta natural"))
    self.assertTrue(is_palindrome("A mamá Roma le aviva el amor a mamá"))


def test_non_palindromes(self):
    self.assertFalse(is_palindrome("hola"))
    self.assertFalse(is_palindrome("computadora"))
    self.assertFalse(is_palindrome("Esto no es un palíndromo"))


def test_edge_cases(self):
    self.assertTrue(is_palindrome(""))
    self.assertTrue(is_palindrome("a"))
    self.assertTrue(is_palindrome("A"))
