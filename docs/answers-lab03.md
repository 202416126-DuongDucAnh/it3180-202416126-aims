# Câu hỏi thảo luận – Lab 03

**Học phần:** IT3180 – Nhập môn Công nghệ phần mềm  
**Sinh viên:** Dương Đức Anh – MSSV: 202416126  
**Bài thực hành:** Lab 03 – Bugfix flow, xung đột & hoàn tác  

---

### Câu 1: Merge base là gì và Git dùng merge base như thế nào để phát hiện xung đột?

#### 1. Định nghĩa Merge base:
* **Merge base** là commit tổ tiên chung gần nhất (*best common ancestor*) giữa hai nhánh (hoặc hai commit) bất kỳ trong đồ thị có hướng không chu trình (DAG) của Git.
* Ta có thể tìm commit merge base giữa hai nhánh bằng lệnh:
  ```bash
  git merge-base <nhanh_A> <nhanh_B>
  ```

#### 2. Cơ chế Three-way Merge (Hợp nhất ba chiều) và phát hiện xung đột:
Khi thực hiện hợp nhất hai nhánh (ví dụ: gộp nhánh `Theirs` vào `Ours`), Git không chỉ so sánh trực tiếp hai trạng thái đầu cành với nhau, mà sử dụng thuật toán **Three-way Merge** đối chiếu 3 trạng thái:
1. **Trạng thái Base ($B$):** Snapshot mã nguồn tại commit Merge Base (điểm xuất phát chung).
2. **Trạng thái Ours ($A$):** Snapshot mã nguồn trên nhánh hiện tại đang đứng (nhánh nhận thay đổi).
3. **Trạng thái Theirs ($C$):** Snapshot mã nguồn trên nhánh được gộp vào.

Git so sánh sự biến động của từng khối mã (*hunk*) từ $B \rightarrow A$ và từ $B \rightarrow C$:
* **Trường hợp 1 (Không xung đột):** Chỉ có $A$ thay đổi so với $B$, còn $C$ không đổi $\rightarrow$ Git tự động giữ nguyên thay đổi của $A$.
* **Trường hợp 2 (Không xung đột):** Chỉ có $C$ thay đổi so với $B$, còn $A$ không đổi $\rightarrow$ Git tự động áp dụng thay đổi của $C$ vào kết quả gộp.
* **Trường hợp 3 (Không xung đột):** Cả $A$ và $C$ đều thay đổi so với $B$ nhưng nội dung thay đổi hoàn toàn giống hệt nhau $\rightarrow$ Git hợp nhất bình thường.
* **Trường hợp 4 (Xung đột - Conflict):** Cả $A$ và $C$ đều cùng sửa đổi trên cùng một vùng dòng mã (hoặc một bên sửa một bên xóa) và nội dung thay đổi **khác nhau** so với trạng thái gốc $B$.  
  Lúc này, Git không thể tự suy diễn ý đồ của lập trình viên bên nào là đúng. Git sẽ tạm dừng quá trình merge và chèn các thẻ đánh dấu xung đột (`<<<<<<< HEAD`, `=======`, `>>>>>>>`) để buộc người phát triển phải can thiệp giải quyết thủ công.

---

### Câu 2: Vì sao trên các nhánh chung như `master` hay `release/*` bắt buộc phải hoàn tác bằng `revert` thay vì `reset`?

#### 1. Tác hại nghiêm trọng của `git reset` trên nhánh công khai:
* **Cơ chế:** `git reset` (đặc biệt là `--hard`) trực tiếp di chuyển con trỏ nhánh lùi về một commit trong quá khứ và loại bỏ các commit sau đó khỏi lịch sử cục bộ.
* **Hậu quả khi áp dụng cho nhánh công khai:**
  * Khi các commit này đã được chia sẻ lên remote repository (`master` hoặc `release/*`), việc xóa commit cục bộ buộc lập trình viên phải dùng lệnh phá hoại `git push --force`.
  * Điều này viết lại lịch sử (*rewrite history*) của dự án, làm sai lệch cây commit của tất cả các thành viên khác trong nhóm. Khi những người khác thực hiện `git pull`, họ sẽ gặp hàng loạt lỗi xung đột phức tạp, hoặc vô tình đẩy ngược lại những commit đã bị xóa lên server, gây nhiễu loạn toàn bộ hệ thống quản lý cấu hình.

#### 2. Tính an toàn và chuẩn mực SCM của `git revert`:
* **Cơ chế:** `git revert` không xóa bỏ hay sửa đổi bất kỳ commit nào trong quá khứ. Thay vào đó, nó tính toán phần bù (nghịch đảo diff) của commit cần hủy và tạo ra một **commit mới** đưa trạng thái mã nguồn trở lại như cũ.
* **Lý do bắt buộc sử dụng trong môi trường chuyên nghiệp:**
  1. **Lịch sử chỉ tiến về phía trước (*Forward-only / Append-only history*):** Lịch sử commit luôn tăng trưởng một cách nhất quán, không làm đứt gãy môi trường làm việc của đồng nghiệp và không bao giờ phải dùng `--force`.
  2. **Minh bạch và bảo toàn dấu vết kiểm toán cấu hình (*Configuration Audit Trail*):** Mọi hành động trong quá trình phát triển (bao gồm việc đưa vào một thay đổi sai và việc nhận diện để hoàn tác thay đổi đó) đều được ghi nhận rõ ràng: ai hoàn tác, thời điểm nào, mã commit là gì và lý do hoàn tác là gì thông qua Pull Request.
