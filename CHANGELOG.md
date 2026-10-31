# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [1.0.1] - 2026-10-31

### Fixed
- Tìm kiếm theo tiêu đề (`search_by_title`) không phân biệt chữ hoa/thường (Refs #21).

## [1.0.0] - 2026-10-31

### Added
- `Cart.print_cart()`: hiển thị danh sách đĩa và tổng tiền trong giỏ hàng.
- `search_by_title()`: tìm kiếm đĩa DVD theo tiêu đề trong danh mục.
- `Cart.apply_discount()`: tính tổng tiền giỏ hàng sau khi áp dụng mã giảm giá.
- Bộ kiểm thử đơn vị tự động trong thư mục `tests/`.

### Fixed
- Giỏ hàng từ chối thêm đĩa thứ 21 khi đã đạt giới hạn 20 đĩa (`MAX_NUMBERS_ORDERED`) (#8).
- Xung đột thông báo hiển thị đĩa được thêm vào giỏ hàng.
