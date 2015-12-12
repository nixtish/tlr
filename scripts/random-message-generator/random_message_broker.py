import nltk
import random
import requests
import string
from datetime import datetime
from pykafka import KafkaClient

KAFKA_HOST = "127.0.0.1:9042"
RESOURCES = {'Pride and Prejudice': "http://www.gutenberg.org/cache/epub/1342/pg1342.txt",
             "Alices Adventures in Wonderland": "http://www.gutenberg.org/cache/epub/11/pg11.txt",
             "The Adventures of Sherlock Holmes": "http://www.gutenberg.org/cache/epub/1661/pg1661.txt"}


nltk.download('punkt')
client = KafkaClient(hosts=KAFKA_HOST)

for k, v in RESOURCES.items():
    r = requests.get(v).content
    tokens = nltk.word_tokenize(r.translate(None, string.punctuation))
    topic = client.topics[''.join(k.split()).lower()]
    with topic.get_producer() as producer:
        for token in tokens:
            rand = random.randint(1, 1000000)
            now = datetime.utcnow().isoformat()
            msg = "||".join([token, str(rand), now])
            producer.produce(msg)
