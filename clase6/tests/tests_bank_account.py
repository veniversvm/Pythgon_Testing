import unittest, os
from src.bank_account import BankAccount

# class BankAccountTests(unittest.TestCase):
#     def test_deposit(self):
#         account = BankAccount(balance=1000)
#         expected = 1500
#         new_balance = account.deposit(amount=500)
#         assert new_balance == expected

#     def test_withdraw(self):
#         account = BankAccount(balance=1000)
#         expected = 500
#         new_balance = account.withdraw(amount=500)
#         assert new_balance == expected

#     def test_get_balance(self):
#         account = BankAccount(balance=1000)
#         expected = 1000
#         new_balance = account.get_balance()
#         assert new_balance == expected

class BankAccountTests2(unittest.TestCase):
    """
        setUp permite setear los parametros de prueba con una sola linea.
        DRY
        ---
        LOG_NAME: constante para el nombrar el log
        """
    LOG_NAME = "transaction_test_log.log"

    def setUp(self) -> None:
        self.account = BankAccount(balance=1000, log_file=self.LOG_NAME)

    def tearDown(self):
        # Se usa para limpiar los datos de la pruebas y evitar que
        # los datos de distintas pruebas interfieran unos con otros
        if os.path.exists(self.LOG_NAME):
            os.remove(self.LOG_NAME)

    def test_deposit(self):
        expected = 1500
        new_balance = self.account.deposit(amount=500)
        # assert new_balance == expected
        self.assertEqual(new_balance, expected, "Balance it's not equal")

    def test_withdraw(self):
        expected = 500
        new_balance = self.account.withdraw(amount=500)
        # assert new_balance == expected
        self.assertEqual(new_balance, expected, "Balance it's not equal")


    def test_get_balance(self):
        expected = 1000
        new_balance = self.account.get_balance()
        # assert new_balance == expected
        self.assertEqual(new_balance, expected, "Balance it's not equal")

    # --- CLASE 5 --#

    def _count_lines(self, filename):
        with open(filename, "r") as f:
            return len(f.readlines())

    def _expect_in_line(self, filename, line_number, expected_msg):
        lines = None
        with open(filename, "r") as f:
            lines = f.readlines()
        return expected_msg.strip() == lines[line_number].strip()

    def test_transaction_log(self):
        self.account.deposit(amount=500)
        # assert os.path.exists(self.LOG_NAME)
        self.assertTrue(os.path.exists(self.LOG_NAME))

    def test_count_transactions(self):
        log_file = self.account.log_file
        # assert self._count_lines(log_file) == 1
        self.assertEqual(self._count_lines(log_file), 1, "Not the same lines in the log file")
        self.account.deposit(500)
        # assert self._count_lines(log_file) == 2
        self.assertEqual(self._count_lines(log_file), 2, "Not the same lines in the log file")
        self.account.withdraw(amount=500)
        # assert self._count_lines(log_file) == 3
        self.assertEqual(self._count_lines(log_file), 3, "Not the same lines in the log file")

    def test_multiple_operations(self):
        log_file = self.account.log_file
        assert self._count_lines(log_file) == 1
        self._expect_in_line(log_file, 0, '--- Account Created ---')
        ### ---- Deposit ---- ###
        balance = self.account.balance
        deposit = 500
        self.account.deposit(deposit)
        assert self._count_lines(log_file) == 2
        assert self._expect_in_line(log_file, 1, f"Deposit of {deposit} --- Balance: {balance + deposit}") == True
        ### ---- Withdrawl ---- ###
        balance = self.account.balance
        withdraw = 900
        self.account.withdraw(withdraw)
        assert self._count_lines(log_file) == 3
        assert self._expect_in_line(log_file, 2, f"Withdraw of {withdraw} --- Balance: {balance - withdraw}") == True

    def test_amount_exceds_balance(self):
        log_file = self.account.log_file
        withdraw = 5000
        balance = balance = self.account.balance
        assert self._count_lines(log_file) == 1
        with self.assertRaises(ValueError):
            self.account.withdraw(amount=withdraw)
        assert self._count_lines(log_file) == 2
        assert self._expect_in_line(
            filename=log_file,
            line_number=1,
            expected_msg=f"Error of withdraw attemp: Intendent ammount:{withdraw} || Current balance: {balance}.") == True
