import os
import time

from . import client


MQTT_HOST = os.environ.get("MQTT_HOST", "localhost")
MQTT_PORT = int(os.environ.get("MQTT_PORT", 11883))

ALIVE_TIME = int(os.environ.get("ALIVE_TIME", 60))
RETRY_TIME = int(os.environ.get("RETRY_TIME", 10))


def connect_mqtt():
    client.connect(MQTT_HOST, MQTT_PORT, ALIVE_TIME)
    retry_count = 0
    while not client.connected_flag and retry_count < RETRY_TIME:
        client.loop()
        retry_count += 1
        print("Retry", retry_count, "time")
        time.sleep(1)  # wait for connection

    return client


async def async_connect_mqtt():
    await client.connect(MQTT_HOST, MQTT_PORT, ALIVE_TIME)
    retry_count = 0
    while not client.connected_flag and retry_count < RETRY_TIME:
        client.loop()
        retry_count += 1
        print("Retry", retry_count, "time")
        time.sleep(1)  # wait for connection

    return client
