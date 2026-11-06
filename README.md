# AIMS-mini

Ứng dụng quản lý giỏ hàng đĩa số mẫu cho học phần **Quản lý cấu hình phần mềm (IT3180)**.

- **Sinh viên:** Dương Đức Anh
- **MSSV:** 202416126

## Chạy và kiểm thử

Yêu cầu Python >= 3.10 (chỉ dùng thư viện chuẩn). Từ thư mục gốc repo:
```bash
python main.py
python -m unittest discover -s tests -v
```
`main.py` in phiên bản và tổng tiền mẫu `63.89 $`. CI chạy bộ test tự động cho Pull Request vào `master` hoặc `release/*`.

## Báo cáo trả lời câu hỏi thảo luận

Tài liệu chi tiết tại [docs/](docs/) (kèm đặc tả [use-case.md](docs/use-case.md)):

| Lab | Nội dung | Báo cáo |
| :---: | --- | --- |
| 01 | Git cơ bản, refactor, baseline | [answers-lab01.md](docs/answers-lab01.md) |
| 02 | Feature/topic, PR và ba kiểu merge | [answers-lab02.md](docs/answers-lab02.md) |
| 03 | Bugfix, xung đột, revert | [answers-lab03.md](docs/answers-lab03.md) |
| 04 | Release, SemVer, tag và kiểm toán | [answers-lab04.md](docs/answers-lab04.md) |
| 05 | Hotfix, cherry-pick và bảo trì nhiều phiên bản | [answers-lab05.md](docs/answers-lab05.md) |

## Các mốc bài nộp

| Lab | Nhánh bài nộp | Tag |
| :---: | --- | --- |
| 01 | `release/lab01` | `v0.1.0` |
| 02 | `release/lab02` | `v0.2.0` |
| 03 | `release/lab03` | `v0.3.0` |
| 04 | `release/lab04` | `v1.0.0`, `v1.0.1` (hotfix) |
| 05 | `release/lab05` | `v1.1.0` |

`master` là dòng phát triển chính. Lịch sử Git ghi lại các nhánh refactor, feature, bugfix, release và hotfix; test lỗi giỏ hàng và giảm giá được ghi trước commit sửa. Bản sửa tìm kiếm không phân biệt hoa thường được cherry-pick với `-x` vào `master` và `release/lab05`.
