import json
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import helpers

ES_CLUSTER = "elastic.tlr.io"
ES_PORT = 9200
ES_INDEX = "weather"
ES_DOC_TYPE = "default"
ES_TTL = "400d"

es = Elasticsearch([{"host": ES_CLUSTER, "port": ES_PORT}])


# Change this to bulk update later
with open('hourly_16.json', 'r') as infile:
    for line in infile:
        record = json.loads(line)
        city = record['city']
        city['city'] = city['name']
        data = record['data']
        for i in data:
            i.update(city)
            i['dt_es'] = datetime.utcfromtimestamp(i['dt'])
            i['location'] = str(i['coord']['lat']) + ',' + str(i['coord']['lon'])
            es.index(index=ES_INDEX, doc_type=ES_DOC_TYPE, body=i, ttl=ES_TTL)
