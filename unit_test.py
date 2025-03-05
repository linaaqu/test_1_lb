import unittest
import homework

class TestStringUtils(unittest.TestCase):
    def test_palindrome(self):
        self.assertEqual(homework.t_polindrome("sas"), True)
    def test_back_string(self):
        self.assertEqual(homework.r_string("asd"), "dsa")
    def test_vowels(self):
        self.assertEqual(homework.e_vowels("aeiou"), "aeiou")
    def test_remove_duplicates(self):
        self.assertEqual(homework.r_duplicates("Hello world"), "Helo wrd")

if __name__ == '__main__':
    unittest.main()
