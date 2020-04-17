import os
from redis import Redis
from rq import Connection, Queue, Worker


listen = ["mqtt_notification"]


if __name__ == "__main__":
    redis_host = os.environ.get("REDIS_HOST", "localhost")
    redis_port = int(os.environ.get("REDIS_PORT", 10379))

    with Connection(Redis(host=redis_host, port=redis_port)):
        worker = Worker(list(map(Queue, listen)))
        print("------------->", worker.__dict__)
        worker.work()
