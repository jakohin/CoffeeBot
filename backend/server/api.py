from fastapi import FastAPI
from paho.mqtt import client
import json


app = FastAPI()

client = client.Client()
client.connect("192.168.1.113")


def on_message(*args, **kwargs):

    pass


@app.get('/')
def index():
    return {"test": "test"}


@app.get('/get_coffee/')
def get_coffee(room_num):
    dispatch_robot(room_num)
    return {"room_num": room_num, "status": True}


def dispatch_robot(room_num):
    client.publish("bot", payload=json.dumps({"room": room_num}))
