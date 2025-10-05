-- ================================
--  DATABASE: atm_demo
--  Author: Mai Hang - Lab 07
-- ================================

DROP DATABASE IF EXISTS atm_demo;
CREATE DATABASE atm_demo;
USE atm_demo;

-- ---------------------
-- BẢNG accounts
-- ---------------------
CREATE TABLE accounts (
    account_id INT AUTO_INCREMENT PRIMARY KEY,
    balance DECIMAL(15,2) NOT NULL DEFAULT 0
);

-- ---------------------
-- BẢNG cards
-- ---------------------
CREATE TABLE cards (
    card_no VARCHAR(20) PRIMARY KEY,
    account_id INT NOT NULL,
    pin_hash VARCHAR(64) NOT NULL,
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

-- ---------------------
-- BẢNG transactions
-- ---------------------
CREATE TABLE transactions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    account_id INT,
    card_no VARCHAR(20),
    atm_id INT,
    tx_type VARCHAR(20),
    amount DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ---------------------
-- DỮ LIỆU MẪU
-- ---------------------
INSERT INTO accounts (balance) VALUES (500000.00);   -- account_id = 1
INSERT INTO cards (card_no, account_id, pin_hash)
VALUES ('123456789', 1, SHA2('1234', 256));          -- PIN mặc định: 1234

-- Test thêm 1 account khác
INSERT INTO accounts (balance) VALUES (1500000.00);   -- account_id = 2
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '';
FLUSH PRIVILEGES;

INSERT INTO cards (card_no, account_id, pin_hash)
VALUES ('987654321', 2, SHA2('5678', 256));          -- PIN mặc định: 5678
