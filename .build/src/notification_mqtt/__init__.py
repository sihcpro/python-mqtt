import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
        client.connected_flag = True  # Flag to indicate success
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


client = mqtt.Client()
client.connected_flag = False
client.on_connect = on_connect

__all__ = (
    "client",
    "config",
    "logger",
)
