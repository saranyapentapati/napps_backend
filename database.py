from couchbase.cluster import Cluster, ClusterOptions
from couchbase.auth import PasswordAuthenticator

cluster = Cluster('couchbase://localhost', ClusterOptions(
    PasswordAuthenticator('saranya', 'aaradhya')))
bucket = cluster.bucket('napps')
collection = bucket.default_collection()
