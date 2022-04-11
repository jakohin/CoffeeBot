from paho.mqtt.client import Client
from paho.mqtt.client import MQTTMessage


def on_message(client, userdata, message: MQTTMessage):
    print(message.payload)


def on_subscribe(client, userdata, mid, granted_qos):
    print(client)


def get_client():
    c = Client()
    c.connect("192.168.1.113")
    c.on_message = on_message
    c.on_subscribe = on_subscribe

    c.subscribe("bot")

    return c


if __name__ == '__main__':
    c = get_client()
    c.loop_forever()
