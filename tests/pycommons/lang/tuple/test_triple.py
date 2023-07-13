from unittest import TestCase

from pycommons.lang.tuple import Triple, MutableTriple


class TestImmutableTriple(TestCase):

    def test_triple_methods(self):
        pair: Triple[int, int] = Triple.of(1, 5, 6)
        self.assertEqual(1, pair.left)
        self.assertEqual(1, pair.get_left())

        self.assertEqual(5, pair.middle)
        self.assertEqual(5, pair.get_middle())

        self.assertEqual(6, pair.right)
        self.assertEqual(6, pair.get_right())

        self.assertEqual("(1, 5, 6)", str(pair))
        self.assertEqual("[1, 5, 6]", pair.to_string("[{0}, {1}, {2}]"))


class TestMutableTriple(TestCase):

    def test_triple_methods(self):
        pair: MutableTriple[int, int] = MutableTriple(1, 5, 6)
        self.assertEqual(1, pair.left)
        self.assertEqual(1, pair.get_left())

        self.assertEqual(5, pair.middle)
        self.assertEqual(5, pair.get_middle())

        self.assertEqual(6, pair.right)
        self.assertEqual(6, pair.get_right())

        self.assertEqual("(1, 5, 6)", str(pair))
        self.assertEqual("[1, 5, 6]", pair.to_string("[{0}, {1}, {2}]"))

        pair.left = 2
        self.assertEqual(2, pair.left)

        pair.middle = 3
        self.assertEqual(3, pair.middle)

        pair.right = 7
        self.assertEqual(7, pair.right)

        pair.set_left(3)
        self.assertEqual(3, pair.left)

        pair.set_middle(0)
        self.assertEqual(0, pair.middle)

        pair.set_right(8)
        self.assertEqual(8, pair.right)
