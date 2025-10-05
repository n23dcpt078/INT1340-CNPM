from withdraw_module import verify_pin, withdraw

card_no = input("Nhập số thẻ: ")
pin = input("Nhập PIN: ")

if verify_pin(card_no, pin):
    amount = int(input("Nhập số tiền muốn rút: "))
    withdraw(card_no, amount)
else:
    print("❌ PIN không đúng.")
