#SCYLLA / CASSANDRA
from cassandra.cluster import Cluster
#cluster = Cluster(['scylla'])
cluster = Cluster(['cassandra'])
session = cluster.connect('')
rows = session.execute('SELECT * FROM system_schema.keyspaces;')
for user_row in rows:
    print(user_row[0])