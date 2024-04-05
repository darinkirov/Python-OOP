class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[''] * 4 for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = (photos_count + 3) // 4
        return cls(pages)

    def add_photo(self, label):
        for i in range(self.pages):
            for j in range(4):
                if self.photos[i][j] == '':
                    self.photos[i][j] = label
                    return f"{label} photo added successfully on page {i + 1} slot {j + 1}"
        return "No more free slots"

    def display(self):
        result = ""
        for page in self.photos:
            result += "-----------\n"
            for photo in page:
                if photo:
                    result += f"[{photo}] "
                else:
                    result += "[] "
            result += "\n"
        return result.rstrip()

# Example usage:
album = PhotoAlbum(2)
print(album.add_photo("Photo1"))  # Output: Photo1 photo added successfully on page 1 slot 1
print(album.add_photo("Photo2"))  # Output: Photo2 photo added successfully on page 1 slot 2
print(album.add_photo("Photo3"))  # Output: Photo3 photo added successfully on page 1 slot 3
print(album.add_photo("Photo4"))  # Output: Photo4 photo added successfully on page 1 slot 4
print(album.add_photo("Photo5"))  # Output: Photo5 photo added successfully on page 2 slot 1
print(album.display())
# Output:
# -----------
# [Photo1] [Photo2] [Photo3] [Photo4]
# [Photo5] [] [] []
# -----------
