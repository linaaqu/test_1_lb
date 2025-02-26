import unittest
import string_utils

class TestStringUtils(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(string_utils.t_polindrome("sas"), True)
    def test_back_string(self):
        self.assertEqual(string_utils.r_string("asd"), "dsa")
    def test_vowels(self):
        self.assertEqual(string_utils.e_vowels("aeiou"), "aeiou")
    def test_remove_duplicates(self):
        self.assertEqual(string_utils.r_duplicates("Hello world"), "Helo wrd")

if __name__ == '__main__':
    unittest.main()
