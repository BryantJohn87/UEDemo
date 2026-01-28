import unittest

import uedemo


class TestUEDemo(unittest.TestCase):
    def test_greet_trims_and_formats(self) -> None:
        self.assertEqual(uedemo.greet("  Ada "), "Hello, Ada!")

    def test_greet_rejects_blank(self) -> None:
        with self.assertRaises(ValueError):
            uedemo.greet("   ")

    def test_add(self) -> None:
        self.assertEqual(uedemo.add(2, 3), 5)

    def test_is_even(self) -> None:
        self.assertTrue(uedemo.is_even(10))
        self.assertFalse(uedemo.is_even(7))


if __name__ == "__main__":
    unittest.main()
