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


some_album = get_album_by_id(cur, 1)
print(some_album)
con.close()
