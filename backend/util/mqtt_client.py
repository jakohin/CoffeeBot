import os

from paho.mqtt.client import Client
from paho.mqtt.client import MQTTMessage

from ast import literal_eval
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

HOST = str(os.environ.get('HOST'))
PORT = int(os.environ.get('PORT'))
TOPICS = literal_eval(os.environ.get('TOPICS'))


print(f"Host:\t{HOST}:{type(HOST)}\nPort:\t{PORT}:{type(PORT)}\nTopics:\t{TOPICS}:{type(TOPICS)}")


def on_message(client, userdata, message: MQTTMessage):
    print(message.payload)


def on_subscribe(client, userdata, mid, granted_qos):
    print(client)


def get_client():
    _cl = Client()
    _cl.connect(HOST, PORT)
    _cl.on_message = on_message
    _cl.on_subscribe = on_subscribe

    for topic in TOPICS:
        _cl.subscribe(topic)

    return _cl


if __name__ == '__main__':
    cl = get_client()
    cl.loop_forever()
