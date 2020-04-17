# ! c:\python34\python.exe
# !/usr/bin/env python
# demo code provided by Steve Cope at www.steves-internet-guide.com
# email steve@steves-internet-guide.com
# Free to use for any purpose
# If you like and use this code you can
# buy me a drink here https://www.paypal.me/StepenCope
"""
Client Connection status demo code
"""
import paho.mqtt.client as mqtt  # import the client
import time


def on_disconnect(client, userdata, flags, rc=0):
    m = "DisConnected flags" + "result code " + str(rc)
    print(m)
    client.connected_flag = False


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK Returned code=", rc)
        client.connected_flag = True  # Flag to indicate success
    else:
        print("Bad connection Returned code=", rc)
        client.bad_connection_flag = True


def on_log(client, userdata, level, buf):
    print("log: ", buf)


def on_subscribe(client, userdata, mid, granted_qos):
    print("client has subcribe")


def on_message(client, userdata, message):
    print("message received  ", str(message.payload.decode("utf-8")))


if __name__ == "__main__":
    keep_alive = 5
    QOS1 = 1
    QOS2 = 0
    CLEAN_SESSION = False
    port = 11883
    # broker = "broker.mqttdashboard.com"
    broker = "127.0.0.1"  # use cloud broker
    cname = "sensor1"
    connection_status_topic = "sensor1"

    mqtt.Client.connected_flag = False  # create flags
    mqtt.Client.bad_connection_flag = False
    mqtt.Client.retry_count = 0

    client = mqtt.Client("cname",)  # create new instance
    client.on_message = on_message
    client.on_log = on_log  # client logging
    client.on_connect = on_connect  # attach function to callback
    client.on_disconnect = on_disconnect
    # client.on_subscribe = on_subscribe
    print("publising on ", connection_status_topic)
    print("Setting will message")
    # set will message
    client.will_set(
        connection_status_topic, "Wellcome to Notification center", 0, True
    )
    print("connecting ", broker)
    client.connect(broker, port, keep_alive)
    retry_count = 0
    while not client.connected_flag and retry_count < 5:
        client.loop()
        retry_count += 1
        print("Retry", retry_count, "time")
        time.sleep(1)  # wait for connection

    client.subscribe(connection_status_topic, 0)
    # use retain flag
    client.publish(connection_status_topic, "You got new message", 0)
    client.loop_start()
    time.sleep(keep_alive)
    client.loop_stop()
    print("updating status and disconnecting")
    client.publish(connection_status_topic, "Disconnect", 0, True)
    client.disconnect()
