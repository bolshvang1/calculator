import unittest
from src.Randomgenerator.randomgenerator import genrandnumseed
from src.Randomgenerator.randomgenerator import genrandnum
from src.Randomgenerator.randomgenerator import genrandlist


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def testrandnum(self):
        number = genrandnum(0, 10)
        self.assertIsInstance(number, float)
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual(number, 10)

    def testrandnumseed(self):
        number = genrandnumseed(0, 10, 2)
        self.assertIsInstance(number, float)
        self.assertGreaterEqual(number, 0)
        self.assertLessEqual(number, 10)


    def testrandlist(self):
        listsize = 20
        randlist = genrandlist(0, 10, 2, listsize)
        self.assertEqual(listsize, len(randlist))
        for num in randlist:
            self.assertIsInstance(num, float)
            self.assertGreaterEqual(num, 0)
            self.assertLessEqual(num, 10)


if __name__ == '__main__':
    unittest.main()
