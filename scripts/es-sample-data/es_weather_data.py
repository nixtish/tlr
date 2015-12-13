import json
from datetime import datetime
from elasticsearch import Elasticsearch

ES_CLUSTER = "elastic.tlr.io"
ES_PORT = 9200
ES_INDEX = "weather"
ES_DOC_TYPE = "default"
ES_TTL = "400d"

es = Elasticsearch([{"host": ES_CLUSTER, "port": ES_PORT}])


with open('/Users/peterevanvolgas/Downloads/hourly_16.json', 'r') as infile:
    for line in infile:
        record = json.loads(line)
        city = record['city']
        data = record['data']
        for i in data:
            i.update(city)
            i['dt_es'] = datetime.utcfromtimestamp(i['dt'])
            es.index(index=ES_INDEX, doc_type=ES_DOC_TYPE, body=i, ttl=ES_TTL)
