import unittest
from lab_1 import reverse_string

class TestReverseString(unittest.TestCase):

    def test_check(self):
        with self.assertRaises(SystemExit) as cm: 
            reverse_string("hello") 
            self.assertEqual(cm.exception.code, 0)

        with self.assertRaises(SystemExit) as cm: 
            reverse_string("123") 
            self.assertEqual(cm.exception.code, 0)
            
if __name__ == "__main__":
    unittest.main()