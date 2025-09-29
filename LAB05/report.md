# LAB05 - Tích hợp, quản lý & báo cáo

## 1. Mục tiêu
- Hoàn thiện quy trình phần mềm từ thiết kế đến triển khai.
- Tích hợp các artifacts đã làm ở các LAB trước (Use Case, Sequence Diagram, Form Login).
- Quản lý dự án bằng Git/GitHub và tạo báo cáo tổng hợp.

---

## 2. Artifacts
Các tài liệu và code được gom trong thư mục [`LAB05/artifacts`](./artifacts):

- **Use Case Diagram**: [usecase.png](./artifacts/lab03UC.png)  
- **Sequence Diagram**: [sequence.png](./artifacts/lab03SQ.png)  
- **Form Login Code**: [form_login_code/](./artifacts/login_code)

---

## 3. Quy trình làm việc
1. **Phân tích yêu cầu**  
   - Xác định các chức năng chính của hệ thống qua Use Case Diagram.  

2. **Thiết kế**  
   - Dùng Sequence Diagram để mô tả chi tiết các bước xử lý giữa User và hệ thống.  

3. **Lập trình**  
   - Cài đặt chức năng Form Login bằng HTML, CSS, JavaScript.  
   - Có input Username/Password, nút Login, và kiểm tra dữ liệu cơ bản.  

4. **Tích hợp & Quản lý**  
   - Gom toàn bộ artifacts vào một thư mục (`LAB05/artifacts`).  
   - Dùng Git để quản lý phiên bản.  
   - Cập nhật README.md ở repo chính.   
   - Tạo tag phiên bản `v1.0`.

---

## 4. Kết quả
- Bộ tài liệu thiết kế (Use Case, Sequence).  
- Giao diện Form Login chạy được bằng **Live Server** hoặc GitHub Pages.  
- Repo GitHub có quản lý version, tag, và báo cáo.

---

## 5. Hướng dẫn chạy demo
1. Clone repo:
   ```bash
   git clone https://github.com/n23dcpt078/INT1340-CNPM.git
   cd INT1340-CNPM/LAB05/artifacts/login_code
