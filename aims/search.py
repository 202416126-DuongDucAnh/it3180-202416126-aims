def search_by_title(items, title):
    \"\"\"Tìm kiếm danh sách DVD khớp với tiêu đề.\"\"\"
    if not title:
        return []
    return [dvd for dvd in items if title in dvd.title]
