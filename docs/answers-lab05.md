# Câu hỏi thảo luận – Lab 05

**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm  
**Sinh viên:** Dương Đức Anh – MSSV: 202416126  
**Bài thực hành:** Lab 05 – Hotfix flow & bảo trì nhiều phiên bản  

---

### Câu 1: Ưu và nhược điểm của chiến lược *upstream first* so với *release first* là gì?

Trong quản trị cấu hình mã nguồn và xử lý bản vá khẩn cấp (Hotfix), hai chiến lược phổ biến là:

#### 1. Chiến lược *Upstream First* (Sửa trên `master`/`main` trước, sau đó cherry-pick về các nhánh release):
* **Bản chất:** Được áp dụng phổ biến trong các dự án quy mô lớn như Microsoft, Linux Kernel hay Chromium. Mọi bản sửa lỗi bắt buộc phải được chấp thuận và tích hợp vào dòng phát triển chính (`master`) trước tiên, sau đó mới lựa chọn (*backport / cherry-pick*) đưa về các nhánh phát hành đang cần bảo trì.
* **Ưu điểm:**
  * **Tránh lỗi tái phát vĩnh viễn (*Never Regress*):** Đảm bảo nhánh chính không bao giờ bị "bỏ quên" bản sửa lỗi. Bản vá chắc chắn sẽ có mặt trong tất cả các bản phát hành tương lai của sản phẩm.
  * **Kiểm thử toàn diện:** Bản sửa lỗi được kiểm thử cùng với phiên bản mới nhất của hệ thống và toàn bộ bộ testsuite hiện đại nhất.
* **Nhược điểm:**
  * **Thời gian phản ứng chậm hơn (*Time-to-Production*):** Trong tình huống khẩn cấp trên Production, việc chờ bản vá đi qua toàn bộ quy trình review và kiểm thử trên `master` có thể làm chậm trễ việc cung cấp bản vá nóng cho khách hàng.
  * **Nguy cơ xung đột khi cherry-pick ngược:** Nếu nhánh `master` đã phát triển quá xa so với nhánh release cũ, việc cherry-pick ngược về quá khứ có thể gặp nhiều xung đột mã nguồn phức tạp.

#### 2. Chiến lược *Release First* (Sửa trực tiếp trên nhánh release bị lỗi, sau đó lan truyền về `master`):
* **Bản chất:** Là mô hình được sử dụng trong học phần Lab 05. Khi phát hiện sự cố trên bản phát hành cụ thể (ví dụ: `release/lab04` - v1.0.0), nhánh hotfix được tạo trực tiếp từ dòng phát hành đó để vá lỗi, đóng gói và phát hành bản vá ngay (`v1.0.1`), sau đó dùng `cherry-pick -x` để lan truyền bản vá về `master` và các nhánh release khác (`release/lab05`).
* **Ưu điểm:**
  * **Phản ứng khẩn cấp tức thì:** Khách hàng nhận được bản vá trong thời gian ngắn nhất mà không làm xáo trộn các tính năng đang phát triển dang dở trên `master`.
  * **Độ tương thích cao tại thời điểm sửa:** Bản vá được kiểm thử trực tiếp trên đúng snapshot mã nguồn và các thư viện phụ thuộc của phiên bản đang gặp sự cố.
* **Nhược điểm:**
  * **Nguy cơ bỏ quên lan truyền (*Forgotten Backport / Hotfix Regression*):** Lập trình viên sau khi vá xong trên release và bàn giao cho khách hàng rất dễ quên không đưa bản vá về `master` hoặc các nhánh release song song khác, khiến lỗi xuất hiện trở lại ở phiên bản tiếp theo.
  * **Đòi hỏi kiểm toán cấu hình nghiêm ngặt:** Bắt buộc phải duy trì quy trình kiểm toán thường xuyên (`git cherry`, đối chiếu commit) để bảo đảm mọi bản vá đều được tích hợp đầy đủ.

---

### Câu 2: Nếu lỡ quên lan truyền bản sửa lỗi sang nhánh `release/lab05`, lệnh kiểm toán nào ở Phần F sẽ giúp phát hiện ra thiếu sót?

Để kiểm toán cấu hình và phát hiện thiếu sót lan truyền commit giữa các nhánh, ta có thể sử dụng các lệnh sau:

#### 1. Lệnh `git cherry`:
* **Cú pháp:**
  ```bash
  git cherry -v release/lab05 release/lab04
  ```
* **Nguyên lý hoạt động:** Lệnh `git cherry` so sánh các commit giữa hai nhánh dựa trên nội dung thay đổi thực tế (*patch-id*), chứ không phụ thuộc vào mã SHA của commit.
* **Dấu hiệu phát hiện:**
  * Nếu commit sửa lỗi trên `release/lab04` chưa có mặt trên `release/lab05`, Git sẽ hiển thị commit đó kèm dấu cộng `+`:
    ```text
    + <FIX_SHA> fix(search): make title search case-insensitive
    ```
  * Nếu commit đã được cherry-pick sang `release/lab05`, Git sẽ đánh dấu trừ `-` hoặc không liệt kê, cho biết trạng thái đồng bộ đã đạt chuẩn.

#### 2. Lệnh `git log` kết hợp lọc theo thông điệp commit:
* **Cú pháp:**
  ```bash
  git log --all --oneline --decorate --grep="make title search case-insensitive"
  ```
* **Dấu hiệu phát hiện:** Đầu ra sẽ liệt kê tất cả các ref (nhánh/tag) đang chứa commit sửa lỗi. Nếu trong danh sách ref không có `release/lab05` (hoặc `origin/release/lab05`), kiểm toán viên sẽ phát hiện ngay việc quên lan truyền.

#### 3. Kịch bản chạy kiểm thử tự động đa phiên bản (Multi-version Matrix Audit):
* **Cú pháp:**
  ```bash
  for ref in v1.0.1 v1.1.0 master; do
      git switch --detach -q $ref
      printf "%-8s " $ref
      python -c "from aims.dvd import DigitalVideoDisc as D; from aims.search import search_by_title; print(len(search_by_title([D('The Lion King')], 'lion')))"
  done
  git switch -q master
  ```
* **Dấu hiệu phát hiện:** Kết quả mong đợi trên tất cả các phiên bản đều phải là `1`. Nếu quên lan truyền sang `release/lab05` (`v1.1.0`), kết quả in ra của `v1.1.0` sẽ là `0` thay vì `1`, ngay lập tức chỉ ra sự thiếu sót trong quy trình bảo trì.
