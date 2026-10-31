# Câu hỏi thảo luận – Lab 02

**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm  
**Sinh viên:** Dương Đức Anh – MSSV: 202416126  
**Bài thực hành:** Lab 02 – Feature/Topic flow & Pull Request  

---

### Câu 1: Khi nào nên dùng Merge commit? Khi nào nên dùng Squash? Khi nào nên dùng Rebase?

Trong GitHub và quy trình Git Flow / GitHub Flow, 3 chiến lược hợp nhất nhánh (Merge strategies) phục vụ các mục đích quản trị lịch sử khác nhau:

1. **Merge commit (`git merge --no-ff`):**
   * **Bản chất:** Tạo ra một commit hợp nhất (merge commit) có 2 nhánh cha, bảo toàn trọn vẹn mọi commit riêng lẻ cùng hình thái đồ thị (branch topology) của nhánh tính năng.
   * **Khi nào nên dùng:**
     * Hợp nhất các nhánh tính năng lớn (*epic features*), các bản phát hành (*release branches*) hoặc khi hoàn tất một giai đoạn phát triển quan trọng có nhiều người cùng đóng góp.
     * Khi nhóm phát triển cần giữ nguyên lịch sử phát triển chi tiết và thời điểm cụ thể của từng commit thành phần để phục vụ kiểm toán cấu hình (*Configuration Audit*).
   * **Nhược điểm:** Đồ thị Git (`git log --graph`) sẽ có nhiều nhánh đan xen phức tạp (mạng nhện) nếu lạm dụng cho các nhánh nhỏ.

2. **Squash and merge (`git merge --squash`):**
   * **Bản chất:** Gộp toàn bộ các commit trên nhánh tính năng thành đúng 1 commit duy nhất trên nhánh đích (`master`). Lịch sử commit chi tiết trên nhánh tính năng bị cô đọng lại.
   * **Khi nào nên dùng:**
     * Các nhánh tính năng nhỏ, nhánh sửa lỗi ngắn hạn hoặc các PR có nhiều commit vụn vặt, commit thử nghiệm trong quá trình làm việc (như *"wip"*, *"fix typo"*, *"test again"*).
     * Khi muốn giữ lịch sử nhánh `master` tuyến tính (linear history), gọn gàng, mỗi commit trên `master` đại diện trọn vẹn cho đúng một tính năng hoàn chỉnh, giúp việc `git revert` hoặc `git bisect` cực kỳ thuận tiện.
   * **Nhược điểm:** Mất chi tiết lịch sử từng bước thực hiện nhỏ; tác giả của từng commit con trong quá trình phát triển không được lưu riêng biệt trong Git log của `master`.

3. **Rebase and merge (`git rebase`):**
   * **Bản chất:** Đặt lại gốc của nhánh tính năng lên đỉnh mới nhất của nhánh đích, sau đó tua nhanh (fast-forward). Tất cả commit con được giữ nguyên nhưng được tạo lại với các mã SHA mới, tạo nên lịch sử hoàn toàn thẳng hàng (tuyến tính) mà không có commit gộp chung hay merge commit.
   * **Khi nào nên dùng:**
     * Khi các commit trên nhánh tính năng đã được trau chuốt kỹ lưỡng (mỗi commit đều atomic, pass test, message chuẩn conventional commit) và đội ngũ muốn lưu giữ chi tiết từng commit mà vẫn giữ lịch sử `master` hoàn toàn tuyến tính.
     * Sử dụng trong các dự án nguồn mở lớn hoặc các nhóm kỹ thuật yêu cầu nghiêm ngặt về linear history.
   * **Nhược điểm:** Viết lại mã băm commit (commit SHAs thay đổi), không giữ được ngữ cảnh nhánh tính năng từng tồn tại và phân nhánh ở thời điểm nào.

---

### Câu 2: Vì sao cần bật tùy chọn *Dismiss stale approvals*?

Trong cấu hình bảo vệ nhánh (Branch Protection Rules) trên GitHub:
* **Nguyên lý hoạt động:** Khi tùy chọn *Dismiss stale approvals when new commits are pushed* được kích hoạt, bất kỳ lượt phê duyệt (Approve) nào trước đó của Reviewer sẽ tự động bị hủy (reset về trạng thái chờ review) ngay khi có một commit mới được đẩy (push) lên nhánh của Pull Request.
* **Lý do bắt buộc phải bật:**
  1. **Ngăn chặn mã độc hoặc lỗi phát sinh sau khi đã duyệt:** Nếu không bật tính năng này, một lập trình viên có thể nhận được sự chấp thuận (Approve) cho một PR an toàn, nhưng sau đó đẩy thêm các commit chứa lỗi logic chưa kiểm thử, vi phạm kiến trúc, hoặc mã độc. PR đó vẫn sẽ được phép merge tự động vào `master` vì trạng thái phê duyệt cũ vẫn còn hiệu lực.
  2. **Đảm bảo tính toàn vẹn của quá trình Kiểm soát thay đổi (Change Control):** Bất kỳ sự thay đổi mã nguồn nào dù là nhỏ nhất cũng phải được xem xét lại bởi người có thẩm quyền để đảm bảo chất lượng phần mềm cao nhất.

---

### Câu 3: Pull Request đóng vai trò gì trong mô hình quản lý cấu hình SCM?

Pull Request (PR) không chỉ là một thao tác gộp mã đơn thuần trên Git, mà là một thành phần trọng tâm trong quy trình **Kiểm soát thay đổi (Change Control)** của Quản lý cấu hình phần mềm (SCM):

1. **Cổng kiểm soát chất lượng (Quality Gate):** PR đóng vai trò là "chốt kiểm soát" trước khi bất kỳ thay đổi nào được đưa vào Baseline (mã nguồn chuẩn trên `master`/`main`). PR tích hợp các công cụ CI tự động (chạy kiểm thử unit test, linting, kiểm tra bảo mật) để đảm bảo không đưa mã lỗi vào hệ thống.
2. **Không gian rà soát và phản biện mã nguồn (Peer Review / Code Inspection):** PR cung cấp giao diện trực quan hiển thị diff giữa nhánh tính năng và nhánh đích, là nơi diễn ra thảo luận, phản biện kiến trúc, phát hiện lỗi tiềm ẩn giữa các thành viên trước khi thay đổi được phê duyệt.
3. **Lưu vết và kiểm toán cấu hình (Configuration Audit Trail):**
   * Mọi quyết định thay đổi đều được ghi lại: Ai đề xuất? Ai phê duyệt? Lý do thay đổi là gì? Đã qua những bước kiểm thử nào?
   * PR liên kết trực tiếp với Issue (ví dụ: `Fixes #6`), tạo nên một chuỗi truy vết khép kín từ yêu cầu bài toán $\rightarrow$ thảo luận $\rightarrow$ hiện thực mã nguồn $\rightarrow$ kiểm thử $\rightarrow$ bản phát hành.
