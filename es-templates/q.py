from __future__ import print_function
import json
import pprint as pp
from elasticsearch import Elasticsearch


HOSTS = ['command.tlr.io']
PORT = 9200
SNIFF = False
TIMEOUT = 120

INDEX = 'stoploggingtoyourdbcom-1'
DOC_TYPE = 'post'
FILTER_PATH = ['hits.hits._id',
               'hits.hits._type',
               'hits.hits._source',
               'hits.hits._score',
               'aggregations']

hosts = ['{}:{}'.format(h, PORT) for h in HOSTS]
conn = Elasticsearch(hosts=hosts,
                     sniff_on_start=SNIFF,
                     sniff_on_connection_fail=SNIFF,
                     timeout=TIMEOUT)

res = {}
for q in ['match_all', 'filtered', 'search', 'aggregate', 'top_hits']:  # noqa
    res[q] = json.loads(open('queries/%s.json' % q).read())


pp.pprint(conn.search(index=INDEX,
                      doc_type=DOC_TYPE,
                      body=res['aggregate'],
                      filter_path=FILTER_PATH))
