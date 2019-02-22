from google.cloud import bigquery

client = bigquery.Client()

QUERY = ('SELECT * FROM `precise-passkey-221515.bqdb.test` LIMIT 1000')
query_job = client.query(QUERY)
rows = query_job.result()

for row in rows:
    print(row)