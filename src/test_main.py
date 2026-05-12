import unittest
from gencontent import extract_title

class Testtitle(unittest.TestCase):

    def test_title(self):
        title = '# Que grande tolkien'
        result = extract_title(title)
        self.assertEqual(result, 'Que grande tolkien')

    def test_generate(self):
        pass

if __name__ == "__main__":
    unittest.main()