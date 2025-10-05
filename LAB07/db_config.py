import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="127.0.0.1",  # Đừng để localhost
        user="root",
        password="",       # Để trống nếu Workbench không cần mật khẩu
        database="atm_demo"
    )
