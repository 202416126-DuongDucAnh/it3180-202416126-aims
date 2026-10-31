# Câu hỏi thảo luận – Lab 01

**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm  
**Sinh viên:** Dương Đức Anh – MSSV: 202416126  
**Bài thực hành:** Lab 01 – Thiết lập môi trường & Refactor flow  

---

### Câu 1: Cấu hình `--global` được lưu ở đâu? Khác gì so với `--local`?
* **Vị trí lưu trữ:**
  * `--global`: Được lưu trong tệp `.gitconfig` tại thư mục Home của người dùng (ví dụ trên Windows: `C:\Users\<Tên_User>\.gitconfig` hoặc `~/.gitconfig`).
  * `--local`: Được lưu trong tệp `.git/config` tại thư mục gốc của repository cụ thể.
* **Phạm vi áp dụng:**
  * `--global`: Áp dụng cho tất cả các repository của người dùng hiện tại trên máy tính nếu repository đó không có cấu hình cục bộ riêng.
  * `--local`: Chỉ có hiệu lực đối với riêng repository hiện tại.
* **Mức độ ưu tiên:**
  * Thứ tự ưu tiên của Git: `--local` > `--global` > `--system`.
  * Khi cùng một thiết lập (ví dụ `user.name` hoặc `user.email`) được định nghĩa ở nhiều cấp khác nhau, Git sẽ luôn ưu tiên sử dụng giá trị ở cấp có phạm vi hẹp hơn (`--local`).

---

### Câu 2: Vì sao sử dụng `git mv`? `release/lab01` có phải baseline không? Vì sao không commit trực tiếp lên `master` dù chỉ làm việc một mình?

#### 1. Lý do sử dụng `git mv`:
* **Bảo toàn lịch sử thay đổi:** `git mv` giúp Git tự động theo dõi và ghi nhận việc đổi tên hoặc di chuyển tệp mà không làm đứt đoạn lịch sử commit. Khi cần xem lại quá trình phát triển của tệp (ví dụ với `git log --follow -- aims/cart.py`), toàn bộ commit trước và sau khi di chuyển vẫn được bảo toàn nguyên vẹn.
* **Tiện lợi và an toàn:** Lệnh `git mv` tương đương với việc thực hiện đồng thời 3 bước: di chuyển tệp trên hệ điều hành, xóa đường dẫn cũ khỏi Git (`git rm`), và đưa tệp ở đường dẫn mới vào vùng chuẩn bị (`git add`). Toàn bộ thay đổi được đưa thẳng vào Staging Area mà không sợ bỏ sót.

#### 2. Vai trò của nhánh `release/lab01`:
* **`release/lab01` chính là một Baseline (mốc chuẩn cấu hình):**
  * Trong quản lý cấu hình phần mềm (SCM), Baseline là một phiên bản phần mềm đã được thống nhất, kiểm thử đạt chuẩn và được đóng băng tại một thời điểm cụ thể.
  * Nhánh `release/lab01` đánh dấu trạng thái hoàn thành và ổn định của bài Lab 01, dùng làm căn cứ nộp bài đánh giá và làm mốc tham chiếu cho các bài thực hành tiếp theo.

#### 3. Lý do không commit trực tiếp lên `master` dù chỉ làm việc một mình:
* **Bảo vệ tính ổn định của nhánh chính:** Nhánh `master` đại diện cho sản phẩm đang hoạt động ổn định (production-ready). Việc tách riêng nhánh `refactor/*` giúp cô lập các thay đổi đang trong quá trình thử nghiệm, tránh làm hỏng trạng thái hoạt động của mã nguồn chính.
* **Rèn luyện quy trình kiểm soát thay đổi (Change Control):** Tạo thói quen làm việc chuẩn trong môi trường chuyên nghiệp. Mọi thay đổi đều được đóng gói theo mục đích rõ ràng, đi qua Pull Request để kiểm tra tích hợp, review mã nguồn trước khi hợp nhất.
* **Tương thích với các ràng buộc CI/CD:** Khi áp dụng các quy tắc bảo vệ nhánh (Branch Protection Rules) và pipeline tự động hóa CI/CD, việc bắt buộc đi qua Pull Request là điều kiện tiên quyết để hệ thống chạy kiểm thử và đảm bảo chất lượng phần mềm.
