#MIT License
#
#Copyright (c) 2024 Kaspars Graudiņš
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import signal
import json
import paho.mqtt.client as mqtt

host = os.environ['MQTT_HOSTNAME']
port = int(os.environ['MQTT_PORT'])
user = os.environ['MQTT_USERNAME']
password = os.environ['MQTT_PASSWORD']

# Set user, password
mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.username_pw_set(user, password)

# Connect to MQTT
mqttc.connect(host, port, 60)

remote_topic = os.environ['MQTT_REMOTE_TOPIC']
remote_topic_list = remote_topic.split(",")

remote_action = os.environ['MQTT_REMOTE_ACTION']
remote_action_list = remote_action.split(",")

switch_action = os.environ['MQTT_SWITCH_ACTION']
switch_topic = os.environ['MQTT_SWITCH_TOPIC']
switch_topic_list = switch_topic.split(",")

def signal_handler(sig, frame):
  print("Exiting program and closing mqtt connection...")
  mqttc.disconnect()
  sys.exit(0)

def on_disconnect(client, userdata, rc):
  if rc != 0:
    print("Unexpected MQTT disconnection. Will auto-reconnect")

def process_click(client, userdata, message):
  payload = json.loads(message.payload)
  action = payload["action"]

  if action in remote_action_list:
    for topic in switch_topic_list:
      # Toogle the switch
      client.publish(topic, switch_action);
      print("Publish '" + switch_action + "' with topic '" + topic + "'")

# Process SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Process disconnect
mqttc.on_disconnect = on_disconnect

# Add message callback to the remote actions
for topic in remote_topic_list:
  print("Subscribe to topic '" + topic + "'")
  mqttc.on_message = process_click
  mqttc.subscribe(topic, 0)

# Loop forever
mqttc.loop_forever()
