def search_by_title(items, title):
    """Tìm kiếm danh sách DVD khớp với tiêu đề (không phân biệt chữ hoa/thường)."""
    if not title:
        return []
    return [dvd for dvd in items if dvd.title and title.lower() in dvd.title.lower()]
