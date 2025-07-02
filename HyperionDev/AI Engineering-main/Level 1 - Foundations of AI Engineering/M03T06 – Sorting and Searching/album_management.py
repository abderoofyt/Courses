class Album:
    def __init__(self, album_name, number_of_songs, album_artist):
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"

# Creating the albums1 and albums2 lists
albums1 = [
    Album("Album One", 10, "Artist A"),
    Album("Album Two", 8, "Artist B"),
    Album("Album Three", 15, "Artist C"),
    Album("Album Four", 12, "Artist D"),
    Album("Album Five", 20, "Artist E")
]

albums2 = [
    Album("Album Six", 18, "Artist F"),
    Album("Album Seven", 9, "Artist G"),
    Album("Album Eight", 7, "Artist H"),
    Album("Album Nine", 14, "Artist I"),
    Album("Album Ten", 11, "Artist J")
]

# Copying albums from albums1 into albums2
albums2.extend(albums1)

# Adding two new albums to albums2
albums2.append(Album("Dark Side of the Moon", 9, "Pink Floyd"))
albums2.append(Album("Abbey Road", 17, "The Beatles"))

# Sorting albums2 alphabetically by album_name
albums2.sort(key=lambda album: album.album_name)

# Sorting albums1 by number_of_songs
albums1.sort(key=lambda album: album.number_of_songs)

# Swapping the element at index 0 with the element at index 1 in albums1
albums1[0], albums1[1] = albums1[1], albums1[0]

#print albums1
for album in albums1:
    print(album)

# Printing the list of albums1 after swapping
print("Albums1 after swapping elements at index 0 and 1:")

# Printing the sorted list of albums2 by album_name
print("\nSorted list of albums2 alphabetically by album name:")
for album in albums2:
    print(album)

# Searching for "Dark Side of the Moon" and printing its index
dark_side_index = next((index for index, album in enumerate(albums2) if album.album_name == "Dark Side of the Moon"), None)
print(f"Index of 'Dark Side of the Moon': {dark_side_index}")
