# Câu hỏi thảo luận – Lab 04

**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm  
**Sinh viên:** Dương Đức Anh – MSSV: 202416126  
**Bài thực hành:** Lab 04 – Release flow & phiên bản phát hành  

---

### Câu 1: Vì sao không nên dùng lightweight tag cho việc đánh dấu phiên bản phát hành?

Trong Git có hai loại thẻ đánh dấu (tag):

1. **Lightweight tag (Thẻ rút gọn):**
   * **Bản chất:** Chỉ đơn thuần là một con trỏ trỏ trực tiếp đến một commit object cụ thể (tương tự như một con trỏ nhánh nhưng không tự động di chuyển khi có commit mới).
   * **Đặc điểm:** Không lưu trữ bất kỳ siêu dữ liệu (metadata) nào khác: không có tên người tạo, không có email, không có ngày giờ tạo thẻ, và không có thông điệp ghi chú lý do gắn thẻ.

2. **Annotated tag (Thẻ có chú giải - `git tag -a`):**
   * **Bản chất:** Được lưu trữ dưới dạng một đối tượng độc lập đầy đủ (*tag object*) trong cơ sở dữ liệu đối tượng của Git.
   * **Bao gồm:**
     * Tên và email của người gắn thẻ (*tagger*).
     * Dấu thời gian chính xác thời điểm gắn thẻ (*timestamp*).
     * Thông điệp giải thích phát hành (*release message / release notes*).
     * Chữ ký số mã hóa GPG (nếu dùng cờ `-s` để xác thực tính toàn vẹn và chống giả mạo).

#### Lý do bắt buộc dùng Annotated tag cho phiên bản phát hành:
* **Yêu cầu của Kiểm toán cấu hình (Configuration Audit):** Trong quản lý cấu hình phần mềm SCM, phiên bản phát hành là một mốc chuẩn cấu hình (Baseline) chính thức được bàn giao cho khách hàng hoặc triển khai lên môi trường vận hành (Production). Do đó, cần phải xác minh và truy cứu trách nhiệm rõ ràng: *Ai là người ký duyệt phát hành bản dựng này? Vào thời điểm nào? Nội dung phát hành gồm những gì?*
* **Tích hợp hệ thống phân phối phần mềm:** Các công cụ CI/CD và nền tảng như GitHub Releases phụ thuộc vào Annotated tag để tự động trích xuất thông điệp ghi chú phát hành (*release notes*) và tạo bản lưu trữ (*tarball/zip*) chuẩn xác.

---

### Câu 2: Sự khác biệt cốt lõi giữa `git describe` và `git log` là gì?

| Tiêu chí so sánh | `git log` | `git describe` |
| :--- | :--- | :--- |
| **Mục đích sử dụng** | Duyệt và hiển thị chi tiết toàn bộ lịch sử các commit theo trình tự thời gian hoặc đồ thị DAG. | Định vị vị trí hiện tại của commit so với mốc chuẩn cấu hình (tag có chú giải) gần nhất. |
| **Định dạng kết quả** | Danh sách các commit (mã SHA, tác giả, ngày giờ, commit message, diff). | Một chuỗi phiên bản ngắn gọn, duy nhất: `<tag_gần_nhất>-<số_commit_đi_trước>-g<sha_rút_gọn>`. |
| **Đối tượng tiếp nhận** | Phục vụ con người (lập trình viên) tra cứu lịch sử sửa đổi mã nguồn. | Phục vụ máy móc và quy trình tự động hóa (CI/CD build pipeline) để gắn nhãn bản dựng tự động (*build metadata*). |

#### Ví dụ thực tế từ bài thực hành:
* Sau khi gắn tag `v1.0.0` và merge tính năng `feature/sort-cart` vào `master`:
  * Lệnh `git describe --tags` trả về kết quả: `v1.0.0-1-gcdb7673`.
  * Ý nghĩa: Trạng thái hiện tại của nhánh `master` đang đứng trước tag `v1.0.0` đúng **1 commit**, và commit mới nhất có mã băm rút gọn là `cdb7673` (chữ `g` viết tắt của `git`).
* Nhờ `git describe`, hệ thống build tự động có thể ngay lập tức sinh số hiệu phiên bản nightly-build mà không cần phải cấu hình thủ công.

---

### Câu 3: Lợi ích của việc duy trì tệp `CHANGELOG.md` theo chuẩn Keep a Changelog so với việc chỉ đọc `git log`?

1. **Khác biệt về đối tượng độc giả (Target Audience):**
   * `git log` được viết bởi lập trình viên dành cho chính họ, thường chứa nhiều thông tin mang tính kỹ thuật sâu, các commit vụn vặt trong quá trình phát triển (*"fix typo"*, *"merge master"*, *"update deps"*), gây khó hiểu cho người ngoài.
   * `CHANGELOG.md` theo chuẩn *Keep a Changelog* được biên soạn hướng đến người sử dụng cuối, khách hàng, chuyên viên kiểm thử (QA) và các bên liên quan, chỉ tập trung vào những thay đổi mang lại giá trị thực tế cho người dùng.

2. **Cấu trúc phân loại rõ ràng và khoa học:**
   * Chuẩn *Keep a Changelog* quy định phân tách rõ các nhóm thay đổi:
     * `Added`: Tính năng mới được bổ sung.
     * `Changed`: Thay đổi hành vi của tính năng hiện có.
     * `Deprecated`: Tính năng cũ sắp bị loại bỏ trong tương lai.
     * `Removed`: Tính năng đã bị xóa bỏ hoàn toàn.
     * `Fixed`: Lỗi phần mềm đã được khắc phục.
     * `Security`: Các bản vá lỗ hổng bảo mật.
   * Cung cấp mục `[Unreleased]` ở đầu tệp giúp theo dõi liên tục các thay đổi đang phát triển trước khi một phiên bản mới chính thức được đóng gói.

3. **Cảnh báo thay đổi phá vỡ tính tương thích ngược (Breaking Changes):**
   * Người dùng khi nâng cấp thư viện/ứng dụng có thể nhanh chóng tra cứu `CHANGELOG.md` để biết phiên bản mới có làm hỏng mã nguồn cũ của họ hay không, điều mà việc đọc hàng trăm dòng `git log` hỗn độn không thể đáp ứng được một cách hiệu quả.
