"""
start with command line:
python -m unittest -v bit_test.py
"""
import bit_count
import unittest


class BitTest(unittest.TestCase):
    """Tests bit function"""

    def setUp(self):
        print("preparing for test '{}'".format(self.shortDescription()))

    def tearDown(self):
        print("test has been completed")

    def test_count_bits(self):
        """count bits test"""
        self.assertEqual(bit_count.count_bits(255), 8)
        self.assertEqual(bit_count.count_bits(0), 0)
        self.assertEqual(bit_count.count_bits(1), 1)
        self.assertEqual(bit_count.count_bits(3), 2)
        self.assertEqual(bit_count.count_bits(-129), 2)


if __name__ == "__main__":
    unittest.main()
