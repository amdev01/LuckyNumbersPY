import unittest
import sys
import importlib
from _io import StringIO

stdout = sys.stdout
stdin = sys.stdin
student_code = ""

class LuckyNumberPYUnitTests(unittest.TestCase):

    def setUp(self):
        global stdout
        global stdin
        stdout = sys.stdout
        stdin = sys.stdin

    def tearDown(self):
        global stdout
        global stdin
        stdout = sys.stdout
        stdin = sys.stdin

    def test_alphabet_string(self):
        import LuckyNumbers
        self.assertTrue(LuckyNumbers.alphabet == "abcdefghijklmnopqrstuvwxyz")
        self.assertTrue(LuckyNumbers.CAPalphabet == "ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def test_cenversion(self):
        import LuckyNumbers
        self.assertEqual(34, LuckyNumbers.convert("eleanor"))
        self.assertEqual(30, LuckyNumbers.convert("wiseman"))

    def test_splitting(self):
        import LuckyNumbers
        self.assertEqual(1, LuckyNumbers.split_number(1))
        self.assertEqual(2, LuckyNumbers.split_number(11))
        self.assertEqual(8, LuckyNumbers.split_number(35))
        self.assertEqual(7, LuckyNumbers.split_number(34))
        self.assertEqual(3, LuckyNumbers.split_number(30))

    def test_output(self):
        global student_code
        sys.stdout = StringIO()
        sys.stdin = StringIO("eleanor\nwiseman")
        student_code = importlib.import_module('LuckyNumbers')
        output = sys.stdout.getvalue().strip("\n")
        self.assertTrue("Your lucky number is 1!! This means that you are a natural leader".casefold().replace(" ", "").startswith(output.casefold().replace(" ", "")))
if __name__ == '__main__':
    unittest.main()