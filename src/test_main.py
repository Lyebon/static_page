import unittest
from gencontent import extract_title

class Testtitle(unittest.TestCase):

    def test_title(self):
        title = '''
# Que grande tolkien
>quoting the grate  tolkien

sauron did nothing rong
'''
        result = extract_title(title)
        self.assertEqual(result, 'Que grande tolkien')


if __name__ == "__main__":
    unittest.main()