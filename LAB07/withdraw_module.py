import hashlib
from db_config import get_connection

def verify_pin(card_no, pin):
    """Xác thực mã PIN của thẻ"""
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT pin_hash FROM cards WHERE card_no=%s", (card_no,))
    row = cur.fetchone()
    conn.close()
    
    if not row:
        print("❌ Thẻ không tồn tại.")
        return False

    input_hash = hashlib.sha256(pin.encode()).hexdigest()
    return row[0] == input_hash


def withdraw(card_no, amount):
    """Thực hiện giao dịch rút tiền"""
    conn = get_connection()
    cur = conn.cursor()
    try:
        conn.start_transaction()
        # Khóa hàng để tránh xung đột khi rút cùng lúc
        cur.execute("""
            SELECT a.account_id, a.balance 
            FROM accounts a 
            JOIN cards c USING(account_id) 
            WHERE c.card_no=%s FOR UPDATE
        """, (card_no,))
        
        result = cur.fetchone()
        if not result:
            raise Exception("Thẻ không hợp lệ.")
        
        account_id, balance = result
        
        if balance < amount:
            raise Exception("Không đủ số dư.")
        
        # Cập nhật số dư
        cur.execute("UPDATE accounts SET balance = balance - %s WHERE account_id = %s", (amount, account_id))
        
        # Ghi lại giao dịch
        cur.execute("""
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after)
            VALUES (%s, %s, 1, 'WITHDRAW', %s, %s)
        """, (account_id, card_no, amount, balance - amount))
        
        conn.commit()
        print(f"✅ Rút thành công {amount} VND. Số dư còn lại: {balance - amount} VND")
    
    except Exception as e:
        conn.rollback()
        print("⚠️ Lỗi:", e)
    
    finally:
        conn.close()
