import paho.mqtt.client as mqtt
from datetime import datetime

COUNT = 0
# Install and utilize with Eclipse Mosquitto Broker
BROKER = 'localhost'
# Use unencrypted TCP port
PORT = 1883


# Define Callback functions to perform operation based on acknowlegements or responses from broker
def on_connect(client, userdata, flags, reason, properties):
    print(f'Connection Reason Code {reason}')
 
def on_subscribe(client, userdata, mid, reason, properties):
    print(f'Subscribe Message ID: {mid} Reason Code {reason}')

def on_message(client, userdata, msg):
    global COUNT
    if COUNT < 6:
        print(f'Message attributes -- Topic: {msg.topic}, QOS: {msg.qos}, Retain: {msg.retain}')
        print(f'Time: {datetime.fromtimestamp(msg.timestamp)} -- Temp Value: {msg.payload.decode("utf-8")}')
        COUNT += 1
    else:
        print(f'Message attributes -- Topic: {msg.topic}, QOS: {msg.qos}, Retain: {msg.retain}')
        print(f'Temp Value: {msg.payload.decode("utf-8")}')
        client_sub.disconnect()

def on_disconnect(client, userdata, flags, reason, properties):
    print(f'Connection Closed Reason Code {reason}')
    client_pub.loop_stop()

def on_log(client, userdata, level, buf):
    print(f'Debugging --> Level: {level} - Message: {buf}')


# Create Subscriber client instance and implement callback functions for client
client_sub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='User-Device')
#client_sub.on_log = on_log #Uncomment for debugging purposes
client_sub.on_connect = on_connect
client_sub.on_subscribe = on_subscribe
client_sub.on_message = on_message

# Connect to broker and subscribe to designated topic (must match topic set by Publisher)
client_sub.connect(BROKER, port=PORT)
client_sub.subscribe('TEMP-COMP216')

# Implement blocking loop function
client_sub.loop_forever()