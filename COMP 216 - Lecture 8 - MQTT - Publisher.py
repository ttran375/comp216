import paho.mqtt.client as mqtt
from random import uniform
import time

# Install and utilize with Eclipse Mosquitto Broker
BROKER = 'localhost'
# Use unencrypted TCP port
PORT = 1883


# Define Callback functions to perform operation based on acknowlegements or responses from broker 
def on_connect(client, userdata, flags, reason, properties):
    print(f'Connection Reason Code {reason}')

def on_publish(client, userdata, mid, reason, properties):
    print(f'Publish Reason Code {reason} for Message ID: {mid}')
    
def on_disconnect(client, userdata, flags, reason, properties):
    print(f'Connection Closed Reason Code {reason}')
    client_pub.loop_stop()


# Create Publisher client instance and implement callback functions for client
client_pub = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id='COMP-216-2024')
client_pub.on_connect = on_connect
client_pub.on_publish = on_publish
client_pub.on_disconnect = on_disconnect

# Connect to broker
client_pub.connect(BROKER, port=PORT)

# Implement non-blocking loop function
client_pub.loop_start()
for i in range(7):
    random_value = uniform(10.0, 32.0)
    client_pub.publish('TEMP-COMP216', random_value)
    print(f'Publishing {random_value} to Topic: TEMP-COMP216')
    time.sleep(2)

client_pub.disconnect()