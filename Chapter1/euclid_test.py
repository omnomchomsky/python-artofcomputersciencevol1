import unittest
import euclid


class MyTestCase(unittest.TestCase):
    def test_algorithm_e(self):
        self.assertEqual(euclid.algorithm_e(12, 6), 6)
        self.assertEqual(euclid.algorithm_e(6, 12), 6)
        self.assertEqual(euclid.algorithm_e(1, 1), 1)
        #s1e4
        self.assertEqual(euclid.algorithm_e(2166, 6099), 57)
        self.assertEqual(euclid.algorithm_e(6099, 2166), 57)

    def test_algorithm_f(self):
        self.assertEqual(euclid.algorithm_f(12, 6), 6)
        self.assertEqual(euclid.algorithm_f(6, 12), 6)
        self.assertEqual(euclid.algorithm_f(1, 1), 1)
        #s1e4
        self.assertEqual(euclid.algorithm_f(2166, 6099), 57)
        self.assertEqual(euclid.algorithm_f(6099, 2166), 57)

if __name__ == '__main__':
    unittest.main()
