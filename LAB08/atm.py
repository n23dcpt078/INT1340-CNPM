# atm.py

class ATM:
    def __init__(self, pin, balance):
        self.pin = pin
        self.balance = balance

    def verify_pin(self, input_pin):
        """Trả về True nếu PIN đúng, ngược lại False"""
        return self.pin == input_pin

    def withdraw(self, amount):
        """Trả về số tiền còn lại nếu rút thành công, nếu không đủ tiền trả về 'Insufficient funds'"""
        if amount <= 0:
            return "Invalid amount"
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance
