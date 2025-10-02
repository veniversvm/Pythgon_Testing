import unittest

"""
    Solo es un ejemplo de los tipos de asserts existentes
"""

SERVER = "server_b"
class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )
    # ---- clase 7 ---- #
    """
        Se usa para omitir prueba por cualqueir razon
    """
    @unittest.skip("Trabajo en progreso, sera habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    """
        Se usa para omitir prueba en base a condiciones especificas de
        manera automatizada.
    """
    @unittest.skipIf(SERVER != "server_a", "omitida por no estar en server de pruebas")
    def test_skip_is(self):
        self.assertGreater(1, 2)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertFalse(True)
