# test_withdraw.py
import pytest
from atm import ATM

@pytest.fixture
def atm():
    """Khởi tạo máy ATM với PIN mặc định và số dư 1000"""
    return ATM(pin="1234", balance=1000)

# --- Test verify_pin ---
def test_verify_pin_correct(atm):
    assert atm.verify_pin("1234") == True

def test_verify_pin_incorrect(atm):
    assert atm.verify_pin("0000") == False

# --- Test withdraw ---
def test_withdraw_enough_balance(atm):
    result = atm.withdraw(500)
    assert result == 500  # Sau khi rút 500, còn 500

def test_withdraw_not_enough_balance(atm):
    result = atm.withdraw(2000)
    assert result == "Insufficient funds"

def test_withdraw_invalid_amount(atm):
    result = atm.withdraw(-100)
    assert result == "Invalid amount"
