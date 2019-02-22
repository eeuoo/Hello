from google.cloud import bigquery as bigq
from pprint import pprint

client2 = bigq.Client()

QUERY = ('SELECT song_id, title, singer, release_date, likecnt, genre, album.album_name FROM `precise-passkey-221515.bqdb.Song` LIMIT 1000')

query_job = client2.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row)