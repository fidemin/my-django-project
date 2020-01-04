import json
from logging import StreamHandler

from kafka import KafkaProducer


class LogKafkaProducer(KafkaProducer):
    def __init__(self, brokers, topic):
        self._topic = topic
        self._producer = KafkaProducer(bootstrap_servers=brokers)

    def send(self, msg):
        self._producer.send(self._topic, value=bytes(msg, 'utf-8'))


class KafkaStreamHandler(StreamHandler):
    def __init__(self, brokers, topic):
        StreamHandler.__init__(self)
        self._brokers = brokers
        self._topic = topic
        self._log_kafka_producer = LogKafkaProducer(brokers, topic)

    def emit(self, record):
        msg = self.format(record)
        json_msg = {'provider': 'Yunhong', 'message': msg}
        self._log_kafka_producer.send(json.dumps(json_msg))
