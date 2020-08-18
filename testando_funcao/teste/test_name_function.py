import unittest
from name_function import get_formatted_name

class AaaNome(unittest.TestCase):
    def test(self):
        nome_formatado = get_formatted_name("Ramon", "Maran")
        self.assertEqual(nome_formatado, "Ramon Maran")

unittest.main()