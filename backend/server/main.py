import asyncio
import uvicorn
from api import app


def main():
    cfg = uvicorn.Config(app=app, host="127.0.0.1", port=8000)
    _app = uvicorn.Server(config=cfg)
    _app.run()


if __name__ == '__main__':
    main()
