import sqlite3
def create_connection(dbpath):
  conn = sqlite3.connect(dbpath)
  return conn



def create_artist(conn, artist_name):
  sql_query="""insert into artists(name) values(?)"""
  my_cursor=conn.cursor()
  my_cursor.execute(sql_query,(artist_name,))
  conn.commit()
  my_cursor.close()
  return my_cursor.lastrowid

  # do not have to return anything but can use try: inside this function

def read_artists(conn, limit):  # can add some extra parameters to limit
    sql_query="""SELECT artistid, name from artists order by artistid LIMIT ?"""
    my_cursor=conn.cursor()
    my_cursor.execute(sql_query,(limit,))
    artists_list=my_cursor.fetchall()
    my_cursor.close()
    return artists_list  # can return a list of tuples, or you can create a list of artist objects if you want


def read_artist_by_id(conn, id):  # can add some extra parameters to limit
  sql_query = """select name, ArtistId from artists where ArtistId = ?"""
  my_cursor = conn.cursor()
  my_cursor.execute(sql_query, (id,))
  artist = my_cursor.fetchone()
  my_cursor.close()
  return artist

def update_artist(id, new_name):
    sql_query = """update artists set name=? where artistid = ?"""
    my_cursor = conn.cursor()
    if id not in read_artist_by_id(conn,id):
      print(f'artist with {id=} not found in database')
    else:
      my_cursor.execute(sql_query, (new_name, id, ))
      conn.commit()
      print(f'{my_cursor.rowcount} rows were updated.')
    my_cursor.close()
    return my_cursor.lastrowid

def delete_artist(id=None, name="None"):
  sql_query = """delete from artists where artistid = ?"""
  my_cursor = conn.cursor()
  if id not in read_artist_by_id(conn,id):
    print(f'artist with {id=} not found in database')
  else:
    my_cursor.execute(sql_query, (id,))
    conn.commit()
    print(f'{my_cursor.rowcount} rows were deleted.')
  my_cursor.close()
  return my_cursor.lastrowid
   # provide deletion by id AND/OR name

conn=create_connection('chinook.db')
print(read_artists(conn,-1))
id = (create_artist(conn,'Regīna'))
update_artist(id,'Saule')
delete_artist(id)

