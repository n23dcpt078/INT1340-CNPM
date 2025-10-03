# Lab06 – Thiết kế chi tiết lớp & kiến trúc ATM

## Nội dung nộp
- class-atm.puml / class-atm.png
- package-diagram.puml / package-diagram.png
- notes.md

## Cách tạo diagram
- Viết code UML vào file `.puml`.
- Dùng PlantUML Online (https://www.plantuml.com/plantuml/) để render → export PNG → lưu cùng thư mục.


## Mapping tới rubric
- Đủ lớp & quan hệ: ATM, Card, Account, Transaction và các association.
- Thuộc tính/phương thức: các thuộc tính và phương thức chính như đề.
- Tài liệu & repo: notes.md + commit trong thư mục labs/lab06-atm-class.

## Ghi chú thiết kế
- Controller điều khiển Hardware và kết nối tới BankService.
- Transaction có trạng thái (SUCCESS/FAILED/PENDING).
- Account có phương thức debit/credit để thay đổi balance.
