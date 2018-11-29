import paho.mqtt.publish as publish

topic = "golffflon/iriot"

while True:
    msg = str(input("MSG : ")) 
    publish.single(topic, msg , hostname="iot.eclipse.org")
