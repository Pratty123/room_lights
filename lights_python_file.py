from paho.mqtt import client as mqtt_client
import time
from datetime import datetime
from flask import Flask, render_template

app = Flask(__name__)

def on_connect(client, userdata, flags, rc):
	client.subscribe("topicName/pir")

def on_message(client, userdata, msg):
	global detection
	detection = get(msg.payload)
	@app.route('/', methods=['GET'])

def check_detection():
	client = mqtt.client()
	client.on_connect()
	client.on_message()
	client.connect("broker.emqx.io")

	for i in range(0, 10):
		time.sleep(5)
		print(detection)
		return render_template('index.html')

	loop_stop()

if __name__ == "__main__":
    app.run(port=5001)
