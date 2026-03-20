import unittest

from model.DoubleList import DoubleList

class TestDoubleList(unittest.TestCase):
    def setUp(self):
    # lista base para la mayoría de tests
        self.lista = DoubleList[int]()
        self.lista.add(10)
        self.lista.add(20)
        self.lista.add(30)

    # 🔹 ADD
    def test_add(self):
        self.assertEqual(self.lista.size, 3)

    # 🔹 REMOVE
    def test_remove_existing(self):
        result = self.lista.remove(20)
        self.assertTrue(result)
        self.assertEqual(self.lista.size, 2)
        self.assertFalse(self.lista.contains(20))

    def test_remove_not_found(self):
        result = self.lista.remove(99)
        self.assertFalse(result)
        self.assertEqual(self.lista.size, 3)

    def test_remove_head(self):
        self.lista.remove(10)
        self.assertEqual(self.lista.head.value, 20)

    def test_remove_tail(self):
        self.lista.remove(30)
        self.assertEqual(self.lista.tail.value, 20)

    # 🔹 CONTAINS
    def test_contains_true(self):
        self.assertTrue(self.lista.contains(10))
        self.assertTrue(self.lista.contains(20))
        self.assertTrue(self.lista.contains(30))

    def test_contains_false(self):
        self.assertFalse(self.lista.contains(99))

    def test_contains_after_remove(self):
        self.lista.remove(20)
        self.assertFalse(self.lista.contains(20))

    def test_contains_none(self):
        with self.assertRaises(ValueError):
            self.lista.contains(None)

    # 🔹 ISEMPTY (IMPORTANTE: lista nueva)
    def test_is_empty_initial(self):
        lista = DoubleList[int]()   # 👈 lista vacía
        self.assertTrue(lista.isEmpty())

    def test_is_empty_after_add(self):
        self.assertFalse(self.lista.isEmpty())

    def test_is_empty_after_remove_all(self):
        self.lista.remove(10)
        self.lista.remove(20)
        self.lista.remove(30)
        self.assertTrue(self.lista.isEmpty())


if __name__ == "__main__":
    unittest.main()