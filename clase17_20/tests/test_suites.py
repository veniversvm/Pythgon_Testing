import unittest

from tests.test_bank_account import BankAccountTests2


def bank_account_suite():
    suite = unittest.TestSuite()
    suite.addTest(BankAccountTests2("test_deposit"))
    suite.addTest(BankAccountTests2("test_withdraw"))
    return suite

if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(bank_account_suite())