import unittest
from GameOfLife import get_next_generation, get_living_neighbors

class TestGameOfLifeMethods(unittest.TestCase):

    def test_get_living_neighbors(self):
        self.assertEqual(2, get_living_neighbors(1, 1, [[0,1,0],[0,1,0],[0,1,0]]))
        self.assertEqual(1, get_living_neighbors(0, 1, [[0,1,0],[0,1,0],[0,1,0]]))
        self.assertEqual(1, get_living_neighbors(2, 1, [[0,1,0],[0,1,0],[0,1,0]]))

    def test_get_next_generation(self):
        self.assertEqual([[0,0,0],[1,1,1],[0,0,0]], get_next_generation([[0,1,0],[0,1,0],[0,1,0]]))

if __name__ == '__main__':
    unittest.main()