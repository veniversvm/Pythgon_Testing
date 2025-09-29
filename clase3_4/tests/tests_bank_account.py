import unittest
from src.bank_account import BankAccount

class BankAccountTests(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount(balance=1000)
        expected = 1500
        new_balance = account.deposit(amount=500)
        assert new_balance == expected

    def test_withdraw(self):
        account = BankAccount(balance=1000)
        expected = 500
        new_balance = account.withdraw(amount=500)
        assert new_balance == expected

    def test_get_balance(self):
        account = BankAccount(balance=1000)
        expected = 1000
        new_balance = account.get_balance()
        assert new_balance == expected

class BankAccountTests2(unittest.TestCase):
    """
        setUp permite setear los parametros de prueba con una sola linea.
        DRY
    """
    def setUp(self) -> None:
        self.account = BankAccount(balance=1000)

    def test_deposit(self):

        expected = 1500
        new_balance = self.account.deposit(amount=500)
        assert new_balance == expected

    def test_withdraw(self):
        expected = 500
        new_balance = self.account.withdraw(amount=500)
        assert new_balance == expected

    def test_get_balance(self):
        expected = 1000
        new_balance = self.account.get_balance()
        assert new_balance == expected



    pass