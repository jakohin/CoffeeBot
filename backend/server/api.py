from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json

# from backend.util.mqtt_client import get_client


app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# client = get_client()
# client.connect("192.168.1.113")


@app.get('/')
def index():
    return {"status": "running"}


@app.post('/get_coffee/{room_num}')
def get_coffee(room_num):
    dispatch_robot(room_num)
    return {"room_num": room_num, "status": True}


def dispatch_robot(room_num):
    # client.publish("bot", payload=json.dumps({"room": room_num}))
    pass
