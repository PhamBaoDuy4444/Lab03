# Lab 03: Kiểm thử Form Đăng nhập bằng Selenium

## Mục lục
- [Các chức năng được kiểm thử](#các-chức-năng-được-kiểm-thử)
- [Công nghệ sử dụng](#công-nghệ-sử-dụng)
- [Yêu cầu môi trường](#yêu-cầu-môi-trường)
- [Hướng dẫn cài đặt và chạy test](#hướng-dẫn-cài-đặt-và-chạy-test)
- [Kết quả mong đợi](#kết-quả-mong-đợi)

## Các chức năng được kiểm thử
Kịch bản test bao gồm 6 test case chính theo yêu cầu của đề bài:
1.  **Đăng nhập thành công:** Kiểm tra việc điền thông tin hợp lệ và nhấn nút Login.
2.  **Sai thông tin đăng nhập:** Kiểm tra việc điền sai thông tin và nhấn nút Login.
3.  **Bỏ trống trường:** Kiểm tra cảnh báo lỗi khi không nhập dữ liệu vào các trường bắt buộc.
4.  **Kiểm tra link "Forgot password?":** Xác thực sự tồn tại và khả năng tương tác của link quên mật khẩu.
5.  **Kiểm tra link "Sign Up":** Xác thực sự tồn tại và khả năng tương tác của link đăng ký.
6.  **Kiểm tra các nút Social Login:** Xác thực sự hiển thị của 3 nút đăng nhập bằng mạng xã hội (Facebook, Twitter, Google).

## Công nghệ sử dụng
*   **Ngôn ngữ:** Python 3.x
*   **Thư viện:**
    *   `selenium`: Thư viện chính để tự động hóa trình duyệt.
    *   `webdriver-manager`: Tự động quản lý và tải về WebDriver tương thích với trình duyệt.

## Yêu cầu môi trường
-   Python 3.7 trở lên.
-   Trình quản lý gói `pip`.
-   Trình duyệt web Google Chrome (khuyến khích phiên bản mới nhất).
-   Kết nối Internet để tải các thư viện và WebDriver.

## Hướng dẫn cài đặt và chạy test

Thực hiện các bước sau trong cửa sổ dòng lệnh (Terminal hoặc Command Prompt).

**Bước 1: Clone repository từ GitHub**
```bash
git clone [URL-repository-cua-ban]
cd [ten-thu-muc-project-cua-ban]
```

**Bước 2: Tạo và kích hoạt môi trường ảo (Recommended)**
Việc này giúp quản lý các gói thư viện của project một cách độc lập.
```bash
# Tạo môi trường ảo
python -m venv venv

# Kích hoạt môi trường ảo
# Trên Windows:
venv\Scripts\activate
# Trên macOS/Linux:
source venv/bin/activate
```

**Bước 3: Cài đặt các thư viện cần thiết**
Tất cả các thư viện yêu cầu đã được liệt kê trong file `requirements.txt`.
```bash
pip install -r requirements.txt
```
*(Để tạo file này, bạn chạy lệnh `pip freeze > requirements.txt` sau khi đã cài `selenium` và `webdriver-manager`)*

**Bước 4: Chạy kịch bản kiểm thử**
Thực thi file Python chính để bắt đầu quá trình kiểm thử.
```bash
python test_login_final.py
```
Trình duyệt Chrome sẽ tự động mở lên, thực hiện các thao tác và đóng lại sau khi hoàn thành. Kết quả sẽ được in ra trực tiếp trên cửa sổ dòng lệnh.

## Kết quả mong đợi
Sau khi chạy thành công, bạn sẽ thấy kết quả tương tự như sau trong terminal:
```
>>> Đang khởi tạo WebDriver...
>>> Đã mở trang: Login V4

--- Bắt đầu Test Case: Đăng nhập thành công ---
✅ PASSED: Đã điền thông tin và nhấn LOGIN thành công (mô phỏng).

--- Bắt đầu Test Case: Sai thông tin đăng nhập ---
✅ PASSED: Đã điền username đúng, password sai và nhấn LOGIN (mô phỏng).

--- Bắt đầu Test Case: Bỏ trống trường ---
✅ PASSED: Cảnh báo yêu cầu nhập liệu đã hiển thị chính xác.

--- Bắt đầu Test Case: Link Forgot password? ---
✅ PASSED: Link 'Forgot password?' hiển thị và có thể click.

--- Bắt đầu Test Case: Link SIGN UP ---
✅ PASSED: Link 'Sign Up' hiển thị đúng và có thể click.

--- Bắt đầu Test Case: Nút social login ---
✅ PASSED: Cả 3 nút social (Facebook, Twitter, Google) đều hiển thị.

--- Tất cả test case đã hoàn thành. Đóng trình duyệt sau 5 giây. ---
```
