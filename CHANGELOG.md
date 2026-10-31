# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.1.0] - 2026-10-31

### Added
- `Cart.sort_by_title()`: sắp xếp các đĩa theo tên theo thứ tự chữ cái A-Z.
- `Cart.sort_by_cost()`: sắp xếp các đĩa theo giá tiền tăng dần.
- `search_by_category()`: tìm kiếm đĩa theo thể loại (không phân biệt chữ hoa/thường).
- Bổ sung bộ kiểm thử tìm kiếm trong `tests/test_search.py`.

## [1.0.0] - 2026-10-31

### Added
- `Cart.print_cart()`: hiển thị danh sách đĩa và tổng tiền trong giỏ hàng.
- `search_by_title()`: tìm kiếm đĩa DVD theo tiêu đề trong danh mục.
- `Cart.apply_discount()`: tính tổng tiền giỏ hàng sau khi áp dụng mã giảm giá.
- Bộ kiểm thử đơn vị tự động trong thư mục `tests/`.

### Fixed
- Giỏ hàng từ chối thêm đĩa thứ 21 khi đã đạt giới hạn 20 đĩa (`MAX_NUMBERS_ORDERED`) (#8).
- Xung đột thông báo hiển thị đĩa được thêm vào giỏ hàng.
