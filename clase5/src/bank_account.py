class BankAccount:
    def __init__(self, balance=0, log_file=None):
        self.balance = balance
        self.log_file = log_file
        self._log_transaction('--- Account Created ---')

    def _log_transaction(self, message):
        if self.log_file:
            with open(self.log_file, "a") as f:
                f.write(f"{message}\n")

    def deposit(self, amount):
        if amount <= 0:
            msg = f"Error of deposit attemp: Intendent ammount:{amount} || Non zero(0) or negative value allowed."
            self._log_transaction(msg)
            raise ValueError(msg)

        self.balance += amount
        self._log_transaction(f"Deposit of {amount} --- Balance: {self.balance}")
        return self.balance

    def withdraw(self, amount):
        print("### withdraw ",amount, self.balance, amount > self.balance)
        if amount > self.balance:
            msg = f"Error of withdraw attemp: Intendent ammount:{amount} || Current balance: {self.balance}."
            self._log_transaction(msg)
            raise ValueError(msg)
        self.balance -= amount
        self._log_transaction(f"Withdraw of {amount} --- Balance: {self.balance}")
        return self.balance

    def get_balance(self):
        self._log_transaction(f"Get Balance: {self.balance}")
        return self.balance