import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import NoSuchElementException

# --- PHẦN CẤU HÌNH ---
LOGIN_URL = "https://colorlib.com/etc/lf/Login_v4/index.html"

# Tạo thư mục để lưu ảnh chụp màn hình nếu chưa có
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

# --- KHỞI TẠO WEBDRIVER ---
print(">>> Đang khởi tạo WebDriver...")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get(LOGIN_URL)
driver.maximize_window()
print(f">>> Đã mở trang: {driver.title}")
time.sleep(2)

def run_test(test_name, test_function, screenshot_name):
    """Hàm tiện ích được cập nhật để chạy test và chụp ảnh."""
    print(f"\n--- Bắt đầu Test Case: {test_name} ---")
    try:
        result, message = test_function()
        # Chụp ảnh sau khi hành động test case hoàn tất
        screenshot_path = f"screenshots/{screenshot_name}.png"
        driver.save_screenshot(screenshot_path)
        print(f"📷 Đã chụp ảnh màn hình và lưu tại: {screenshot_path}")
        
        if result:
            print(f"✅ PASSED: {message}")
        else:
            print(f"❌ FAILED: {message}")
    except Exception as e:
        print(f"❌ FAILED: Đã xảy ra lỗi không mong muốn - {e}")
        driver.save_screenshot(f"screenshots/ERROR_{screenshot_name}.png")

# --- CÁC HÀM TEST CASE ---

def test_case_1_login_success():
    driver.find_element(By.NAME, "username").send_keys("my_valid_username")
    driver.find_element(By.NAME, "pass").send_keys("my_valid_password")
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
    # Vì trang không chuyển hướng, ta chỉ cần đợi 1 chút để thấy hành động
    time.sleep(1)
    return True, "Đã điền thông tin và nhấn LOGIN thành công (mô phỏng)."

def test_case_2_login_incorrect():
    driver.find_element(By.NAME, "username").send_keys("correct_username")
    driver.find_element(By.NAME, "pass").send_keys("wrong_password")
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
    time.sleep(1)
    return True, "Đã điền username đúng, password sai và nhấn LOGIN (mô phỏng)."

def test_case_3_empty_fields():
    driver.find_element(By.CLASS_NAME, "login100-form-btn").click()
    time.sleep(1)
    username_wrapper = driver.find_element(By.XPATH, "//div[contains(@class, 'wrap-input100')][.//input[@name='username']]")
    if "alert-validate" in username_wrapper.get_attribute("class"):
        return True, "Cảnh báo yêu cầu nhập liệu đã hiển thị chính xác."
    else:
        return False, "Không tìm thấy cảnh báo yêu cầu nhập liệu."

# Các hàm còn lại không cần thay đổi
def test_case_4_forgot_password_link():
    forgot_link = driver.find_element(By.LINK_TEXT, "Forgot password?")
    return forgot_link.is_displayed(), "Link 'Forgot password?' hiển thị và có thể click."

def test_case_5_sign_up_link():
    signup_link = driver.find_element(By.XPATH, "//a[normalize-space()='Sign Up']")
    return signup_link.is_displayed(), "Link 'Sign Up' hiển thị đúng và có thể click."

def test_case_6_social_login_buttons():
    fb_btn = driver.find_element(By.CLASS_NAME, "fa-facebook")
    tw_btn = driver.find_element(By.CLASS_NAME, "fa-twitter")
    gg_btn = driver.find_element(By.CLASS_NAME, "fa-google")
    return fb_btn.is_displayed() and tw_btn.is_displayed() and gg_btn.is_displayed(), "Cả 3 nút social (Facebook, Twitter, Google) đều hiển thị."

# --- LUỒNG CHẠY CHÍNH ---
try:
    run_test("Đăng nhập thành công", test_case_1_login_success, "TC1_login_success")
    driver.get(LOGIN_URL)
    run_test("Sai thông tin đăng nhập", test_case_2_login_incorrect, "TC2_login_incorrect")
    driver.get(LOGIN_URL)
    run_test("Bỏ trống trường", test_case_3_empty_fields, "TC3_empty_fields_validation")
    driver.get(LOGIN_URL)
    run_test("Link Forgot password?", test_case_4_forgot_password_link, "TC4_forgot_password_link")
    run_test("Link SIGN UP", test_case_5_sign_up_link, "TC5_signup_link")
    run_test("Nút social login", test_case_6_social_login_buttons, "TC6_social_buttons")
finally:
    print("\n--- Tất cả test case đã hoàn thành. Đóng trình duyệt sau 5 giây. ---")
    time.sleep(5)
    driver.quit()