from unittest import TestCase

from pycommons.lang.tuple import Pair, MutablePair


class TestImmutablePair(TestCase):
    def test_pair_methods(self):
        pair: Pair[int, int] = Pair.of(1, 6)
        self.assertEqual(1, pair.left)
        self.assertEqual(1, pair.get_left())
        self.assertEqual(1, pair.get_key())

        self.assertEqual(6, pair.right)
        self.assertEqual(6, pair.get_right())
        self.assertEqual(6, pair.get_value())

        self.assertEqual("(1, 6)", str(pair))
        self.assertEqual("[1, 6]", pair.to_string("[{0}, {1}]"))


class TestMutablePair(TestCase):
    def test_pair_methods(self):
        pair: MutablePair[int, int] = MutablePair(1, 6)
        self.assertEqual(1, pair.left)
        self.assertEqual(1, pair.get_left())
        self.assertEqual(1, pair.key)
        self.assertEqual(1, pair.get_key())

        self.assertEqual(6, pair.right)
        self.assertEqual(6, pair.get_right())
        self.assertEqual(6, pair.value)
        self.assertEqual(6, pair.get_value())

        self.assertEqual("(1, 6)", str(pair))
        self.assertEqual("[1, 6]", pair.to_string("[{0}, {1}]"))

        pair.left = 2
        self.assertEqual(2, pair.left)

        pair.right = 7
        self.assertEqual(7, pair.right)

        pair.set_left(3)
        self.assertEqual(3, pair.left)

        pair.set_right(8)
        self.assertEqual(8, pair.right)
