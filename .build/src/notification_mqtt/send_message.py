from .connection import connect_mqtt


def send_message(topic, payload):
    client = connect_mqtt()
    client.publish(topic, payload)
    client.disconnect()
    client.connected_flag = False
