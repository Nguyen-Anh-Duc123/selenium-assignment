import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# 1. Khởi tạo trình duyệt Chrome tự động
print("--- KHỞI TẠO TRÌNH DUYỆT CHROME ---")
options = webdriver.ChromeOptions()
# options.add_argument('--headless') # Bỏ dấu thăng nếu muốn chạy ngầm không bật cửa sổ
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

try:
    # ========================================================
    # TEST CASE 01: ĐĂNG NHẬP THÀNH CÔNG (LOGIN SUCCESS)
    # ========================================================
    print("\n[Chạy TC-01]: Đăng nhập vào hệ thống...")
    driver.get("https://www.saucedemo.com/")
    time.sleep(2) # Đợi trang tải
    
    # Tìm phần tử và điền thông tin tài khoản mẫu
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    time.sleep(2)
    
    # Xác thực xem đã chuyển hướng vào trang mua sắm chưa
    assert "inventory.html" in driver.current_url
    print("=> TC-01: PASSED (Đăng nhập thành công)")
    driver.save_screenshot("01_login_success.png") # Tự động chụp ảnh 1

    # ========================================================
    # TEST CASE 02: THÊM SẢN PHẨM VÀO GIỎ HÀNG (ADD TO CART)
    # ========================================================
    print("\n[Chạy TC-02]: Thêm sản phẩm đầu tiên vào giỏ hàng...")
    
    # Click nút Add to cart của sản phẩm Balo
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    time.sleep(1)
    
    # Kiểm tra số hiển thị trên biểu tượng giỏ hàng xem có tăng lên 1 không
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert cart_badge == "1"
    print("=> TC-02: PASSED (Thêm giỏ hàng thành công)")
    driver.save_screenshot("02_add_to_cart.png") # Tự động chụp ảnh 2

    # ========================================================
    # TEST CASE 03: ĐĂNG XUẤT HỆ THỐNG (LOGOUT SUCCESS)
    # ========================================================
    print("\n[Chạy TC-03]: Tiến hành đăng xuất tài khoản...")
    
    # Mở Menu thanh bên trái
    driver.find_element(By.ID, "react-burger-menu-btn").click()
    time.sleep(1)
    
    # Bấm nút Logout
    driver.find_element(By.ID, "logout_sidebar_link").click()
    time.sleep(2)
    
    # Xác thực xem có quay lại trang login gốc không
    assert "https://www.saucedemo.com/" in driver.current_url
    print("=> TC-03: PASSED (Đăng xuất hệ thống thành công)")
    driver.save_screenshot("03_logout_success.png") # Tự động chụp ảnh 3

except Exception as e:
    print(f"\n❌ Phát sinh lỗi trong quá trình test: {e}")

finally:
    # Đóng trình duyệt, giải phóng tài nguyên
    print("\n--- HOÀN THÀNH QUY TRÌNH KIỂM THỬ - ĐÓNG TRÌNH DUYỆT ---")
    driver.quit()