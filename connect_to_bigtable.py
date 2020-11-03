from google.cloud import bigtable

client = bigtable.Client(project='dev-project', admin=True)
instance = client.instance('big-table-dev')
