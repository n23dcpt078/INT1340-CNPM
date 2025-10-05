# selenium_test_login.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import pytest

# ⚙️ Đường dẫn tới file index.html của bạn
HTML_PATH = "file:///C:/Users/n23dc/INT1340-CNPM/LAB08/index.html"

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get(HTML_PATH)
    yield driver
    driver.quit()

def test_login_success(driver):
    """Test case 1: Đăng nhập hợp lệ"""
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Đăng nhập thành công!"
    alert.accept()

def test_login_empty(driver):
    """Test case 2: Bỏ trống username/password"""
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Vui lòng nhập đầy đủ Username và Password!"
    alert.accept()

def test_login_short_password(driver):
    """Test case 3: Password < 6 ký tự"""
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("123")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    time.sleep(1)
    alert = Alert(driver)
    assert alert.text == "Password phải có ít nhất 6 ký tự!"
    alert.accept()
