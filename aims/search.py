def search_by_category(items, category):
    """Tìm kiếm danh sách DVD khớp với thể loại."""
    if not category:
        return []
    return [dvd for dvd in items if dvd.category and category.lower() in dvd.category.lower()]


def search_by_title(items, title):
    """Tìm kiếm danh sách DVD khớp với tiêu đề."""
    if not title:
        return []
    return [dvd for dvd in items if title in dvd.title]
