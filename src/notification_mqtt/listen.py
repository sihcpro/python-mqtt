from .connection import connect_mqtt


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + ":" + str(msg.payload))


def listen_all_message_to_notification():
    client = connect_mqtt()
    client.on_message = on_message

    client.subscribe("notification_center")
    client.loop_forever()


if __name__ == "__main__":
    listen_all_message_to_notification()
