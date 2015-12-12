from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

sc = SparkContext()
ssc = StreamingContext(sc, 1)  # 1 second window

ZK = '127.0.0.1:2181'
TOPIC = "prideandprejudice0"
PARTITIONS = 5
kafka_topic = {TOPIC: PARTITIONS}


kvs = KafkaUtils.createStream(ssc, ZK, "spark-streaming-consumer", kafka_topic)
lines = kvs.map(lambda x: x[1])
lines.pprint()

ssc.start()
ssc.awaitTermination()
