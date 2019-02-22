import pymysql, sys
import bigquery


def get_conn(db):
  return pymysql.connect( 
        host = '34.85.124.225',
        user = 'root',
        password = '11' ,
        port = 3306 ,
        db = db ,
        charset = 'utf8' )


def get_songs():

    conn = get_conn('hjdb')

    with conn:
        cur = conn.cursor()
        select_query = "select s.*, a.rate as album_rate, a.album_likecnt as album_likecnt, a.type as type, a.agency as agency from SongInfo s inner join AlbumInfo a on s.album_id = a.album_id"
        cur.execute(select_query)
        
        Songs = cur.fetchall()
        columns = cur.description 

        result = [{columns[index][0]:column for index, column in enumerate(value)} for value in Songs] 

        rr = [ {'song_id' : dic['song_id'], 
                'likecnt' : dic['likecnt'], 
                'title' : dic['title'],
                'genre' : dic['genre'],
                'singer' : dic['singer'],
                'release_date': dic['release_date'],
                'album' : {'album_id' : dic['album_id'],
                            'album_name': dic['album_name'],
                            'album_rate': float(dic['album_rate']),
                            'album_likecnt': dic['album_likecnt'],
                            'type': dic['type'],
                            'agency' : dic['agency']
                          }
                } for dic in result ]

        return rr

DATABASE = "bqdb"
TABLE = "Song"

client = bigquery.get_client(json_key_file='./bigquery.json', readonly=False)

if not client.check_table(DATABASE, TABLE):
    print("Create table {0}.{1}".format(DATABASE, TABLE), file=sys.stderr)

    client.create_table(DATABASE, TABLE, [
        {'name': 'song_id', 'type': 'string', 'description': 'song id'},
        {'name': 'title', 'type': 'string', 'description': 'song title'},
        {'name': 'singer', 'type': 'string', 'description': 'singer'},
        {'name': 'release_date', 'type': 'string', 'description': 'release date'},
        {'name': 'likecnt', 'type': 'string', 'description': 'song like count'},
        {'name': 'genre', 'type': 'string', 'description': 'song genre'},
        {'name': 'album', 'type': 'RECORD', 'description':'album information', 'fields' : [
                    {'name': 'album_name', 'type': 'string', 'description': 'album title'},
                    {'name': 'album_likecnt', 'type': 'string', 'description': 'album like count'},
                    {'name': 'album_rate', 'type': 'FLOAT', 'description': 'album rate'},
                    {'name': 'album_id', 'type': 'string', 'description': 'album id'},
                    {'name': 'agency', 'type': 'string', 'description': 'agency'},
                    {'name': 'type', 'type': 'string', 'description': 'album type'}
                    ] }
        ]
    )

ttt = get_songs()

pushResult = client.push_rows(DATABASE, TABLE, ttt, insert_id_key='songno')
print("Pushed Result is", pushResult)


