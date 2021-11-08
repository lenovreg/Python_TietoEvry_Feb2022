import sqlite3

# https://docs.python.org/3/library/sqlite3.html

con = sqlite3.connect('chinook.db')  # absolute or relative path to database
# Once you have a Connection, you can create a Cursor object and call its execute() method to perform SQL commands:
cur = con.cursor()
row_it = cur.execute('SELECT * FROM albums LIMIT 10')  # returns a row iterator
results_list = [row for row in row_it]  # just list(row_it) would work here as well
print(results_list)


def get_album_by_id(cur, id):
    cur.execute('SELECT * FROM albums WHERE AlbumId = ?', (id,))
    return cur.fetchone()


def insert_album(cur, album: tuple):
    cur.execute('INSERT INTO albums (Title, ArtistId) VALUES (?, ?)',
                album)  # parameters must be in the same order as in the SQL statement


def update_album_title(cur, album: tuple):  # so tuple should have Title first and AlbumId second
    cur.execute('UPDATE albums SET Title = ? WHERE AlbumId = ?',
                album)  # parameters must be in the same order as in the SQL statement


# new_albums = get_album_by_name(cur, "Valdis greatest hits 2")
# print(new_albums)
insert_album(cur, ("Valdis greatest hits 2", 277))  # album id is auto-incremented, 277 is artist id


def get_album_by_name(cur, name):
    cur.execute('SELECT * FROM albums WHERE Title LIKE ?', (name,))
    # return cur.fetchone()
    return cur.fetchall()


def delete_album_by_id(cur, id):  # so no need to pass in a tuple
    cur.execute('DELETE FROM albums WHERE AlbumId = ?', (id,))


update_album_title(cur, ("Valdis greatest hits 3 now!", 349))
delete_album_by_id(cur, 350)

new_albums = get_album_by_name(cur, "Valdis greatest hits%")
print(new_albums)

some_album = get_album_by_id(cur, 1)
print(some_album)
con.commit()  # this should save the database transactions
con.close()
