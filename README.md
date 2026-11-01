# AIMS-mini

Ứng dụng quản lý giỏ hàng đĩa số mẫu cho học phần **Quản lý cấu hình phần mềm (IT3180)**.

- **Sinh viên:** Dương Đức Anh
- **MSSV:** 202416126

---

## 1. Yêu cầu môi trường
- **Python:** Phiên bản `>= 3.10` (khuyến nghị Python 3.12).
- Không yêu cầu cài đặt thư viện bên thứ ba (chỉ sử dụng thư viện chuẩn của Python: `unittest`, `sys`...).

---

## 2. Hướng dẫn sử dụng

### Chạy chương trình mô phỏng chính:
```bash
python main.py
```
Chương trình sẽ khởi tạo danh sách DVD mẫu, thêm đĩa vào giỏ hàng, in thông tin giỏ hàng và tổng tiền.

### Chạy kiểm thử tự động (Unit Tests):
```bash
python -m unittest discover -s tests -v
```
Toàn bộ 11 test cases kiểm tra nghiệp vụ của Cart và Search sẽ được thực thi tự động.

---

## 3. Cấu trúc thư mục dự án
- `aims/`: Gói mã nguồn nghiệp vụ chính (`dvd.py`, `cart.py`, `search.py`).
- `tests/`: Bộ kiểm thử đơn vị tự động (`test_cart.py`, `test_search.py`).
- `docs/`: Tài liệu đặc tả ca sử dụng (`use-case.md`) và câu hỏi thảo luận các bài lab (`answers-lab01.md` -> `answers-lab05.md`).
- `.github/`: Mẫu Pull Request template và cấu hình luồng CI tự động (`workflows/ci.yml`).
